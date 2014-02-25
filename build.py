import os, shutil, sys, json
from datetime import *

import pystache
import markdown


colors = ['blue', 'green', 'purple', 'yellow', 'pink']
excluded_files = ['.DS_Store']


def urlify(s):
	s = s.lower().replace(' ', '-')
	s = s.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
	return s.replace('\'', '').replace('\"', '')


class Sprint:
	def __init__(self, path):
		self.json = {
			'path': path,
			'progress': []
		}
		self.functions = {
			'config': self.config,
			'intro': self.beginning,
			'middle': self.middle,
			'outcome': self.end
		}

	def add_details(self, stage, contents):
		self.functions[stage](contents.decode('utf-8'))

	def process_dates(self, start, end):
		self.start_date = datetime.strptime(start, '%b %d, %Y')
		self.end_date = datetime.strptime(end, '%b %d, %Y')
		self.json['dates'] = {
			'start': self.start_date.strftime('%b %d, %Y'),
			'end': self.end_date.strftime('%b %d, %Y'),
			'daysbefore': range(self.start_date.isoweekday()%7),
			'daysafter': range(7-(self.end_date.isoweekday()+1)%7)
		}
		self.start_date_of_month = datetime.strftime(self.start_date, '%d')
		self.end_date_of_month = datetime.strftime(self.end_date, '%d')

	def config(self, data):
		data = json.loads(data)
		self.process_dates(data['start'], data['end'])
		self.json['title'] = data['title']
		self.json['escapedtitle'] = urlify(data['title'])

	def add_progress_data(self, content, summary, date_of_month, date, is_start=False, is_end=False):
		is_middle = is_empty = False
		if not is_start and not is_end:
			is_middle = True
		if not content:
			is_empty = True
		self.json['progress'].append({
			'content': content,
			'summary': summary,
			'dateofmonth': date_of_month,
			'date': date,
			'class': urlify(date),
			'isstart': is_start,
			'isend': is_end,
			'ismiddle': is_middle,
			'isempty': is_empty
		})

	def beginning(self, data):
		self.add_progress_data(markdown.markdown(data), "start", self.start_date_of_month, datetime.strftime(self.start_date, '%B %d'), is_start=True)

	def middle(self, data):
		for section in data.split('##'):
			if section.strip():
				split = section.split('\n')
				date = split[0].strip()
				summary = split[1].strip()
				content = '\n'.join(split[2:])
				self.add_progress_data(markdown.markdown(content), summary, date.split(' ')[1].replace('\n', ''), date)

	def end(self, data):
		self.add_progress_data(markdown.markdown(data), "end", self.end_date_of_month, datetime.strftime(self.end_date, '%B %d'), is_end=True)

	def get_json(self):
		return self.json


class Sprints:
	def __init__(self, sprint_dir):
		self.sprint_dir = sprint_dir
		self.json = {
			'sprints': []
		}
		self.traverse_sprints()

	def traverse_sprints(self):
		for f in os.listdir(self.sprint_dir):
			path = os.path.join(self.sprint_dir, f)
			if os.path.isdir(path):
				sprint = Sprint(path)
				self.json['sprints'].append(sprint.get_json())
				for s in os.listdir(path):
					if s not in excluded_files:
						stage_path = os.path.join(path, s)
						if not os.path.isdir(stage_path):
							with open(stage_path, 'r') as opened_file:
								sprint.add_details(s.split('.')[0], opened_file.read())

		self.json['sprints'] = sorted(self.json['sprints'], cmp=self.sort_by_date)
		sprint_count = len(self.json['sprints'])
		for index, sprint in enumerate(self.json['sprints']):
			sprint['index'] = index
			if index == 0:
				sprint['iscurrent'] = True
			if index == 1:
				sprint['islastcompleted'] = True
			sprint['color'] = colors[(sprint_count - index) % len(colors)]


	def process_future_sprints(self, path):
		with open(path, 'r') as opened_file:
			self.future_sprints = opened_file.read().split('\n')

	def sort_by_date(self, first, second):
		first_date = datetime.strptime(first['dates']['end'], '%b %d, %Y')
		second_date = datetime.strptime(second['dates']['start'], '%b %d, %Y')
		if first_date < second_date:
			return 1
		elif first_date > second_date:
			return -1
		return 0

	def get_json(self):
		return self.json


class Page:
	def __init__(self, path):
		self.json = {}
		self.path = os.path.basename(path).split('.')[0] + '.html'
		self.process_page(path)

	def process_page(self, path):
		with open(path, 'r') as opened_file:
			contents = opened_file.read()
			self.json['title'] = contents.split('---')[0]
			self.json['escapedtitle'] = os.path.basename(path).split('.')[0]
			self.json['content'] = markdown.markdown(contents)

	def get_json(self):
		return self.json


class Site:
	def __init__(self):
		self.template_dir = 'templates'
		self.static_dir = 'static'
		self.output_dir = 'site'
		self.sprints_dir = 'sprints'
		self.pages_dir = 'pages'
		self.renderer = pystache.Renderer()

		self.setup_site_dir()
		self.process_sprints()

	def setup_site_dir(self):
		shutil.rmtree(self.output_dir)
		self.move_static_files(self.static_dir, self.output_dir)

	def process_sprints(self):
		self.sprints = Sprints(self.sprints_dir)
		self.save_pages()

	def move_static_files(self, source, destination):
		if not os.path.exists(destination):
			os.makedirs(destination)

		for f in os.listdir(source):
			full_path = os.path.join(source, f)
			if os.path.isfile(full_path):
				shutil.copy(full_path, destination)
			elif os.path.isdir(full_path):
				new_path = os.path.join(destination, f)
				if not os.path.exists(new_path):
					os.makedirs(new_path)
				self.move_static_files(full_path, new_path)

	def save_pages(self):
		def save_templated_file(template_path, data, saved_path):
			with open(template_path) as template:
				content = self.renderer.render(template.read(), data)
				self.save_file(saved_path, content)

		# Save the index file
		save_templated_file(os.path.join(self.template_dir, 'home.mustache'), self.sprints.get_json(), os.path.join(self.output_dir, 'index.html'))

		# Save each sprint file
		for sprint in self.sprints.get_json()['sprints']:
			self.move_static_files(os.path.join(sprint['path'], 'images'), os.path.join(self.output_dir, sprint['path']))
			save_templated_file(os.path.join(self.template_dir, 'sprint.mustache'), sprint, os.path.join(self.output_dir, sprint['path']+'.html'))

		# Save other pages
		for f in os.listdir(self.pages_dir):
			if f not in excluded_files:
				page = Page(os.path.join(self.pages_dir, f))
				save_templated_file(os.path.join(self.template_dir, 'blank.mustache'), page.get_json(), os.path.join(self.output_dir, page.path))

	def save_file(self, path, content):
		if not os.path.exists(os.path.dirname(path)):
			os.makedirs(os.path.dirname(path))
		new_file = open(path, 'w')
		new_file.write(content.encode('utf-8'))
		new_file.close()


if __name__ == '__main__':
	site = Site()
