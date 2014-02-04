## January 14
Build tool beginnings

Today I took my first stab at a build tool. I installed the [Python Markdown processor](http://pythonhosted.org//Markdown/), [Python Mustache processor](https://github.com/defunkt/pystache), and started using both. I'm trying to figure out the directory structure that I want to use, as well as a good divide between JSON data and Markdown content.

## January 15

## January 16
Ugly screenshots

After my first couple days, I have this to show for it:

> <img src="this-website/screenshot-1.png" width="537" height="444" alt="screenshot 1" />
> Very beginnings of a homepage, listing out sprints from the directory structure

> <img src="this-website/screenshot-2.png" width="537" height="444" alt="screenshot 2" />
> Dumping all sprint info onto the page

Not pretty at all, but I'm making pages and that's a good start!

## January 17
Colors and fonts

Today I spent some time looking at colors and fonts. I want a colorful page, but I'm wary of it not seeming cohesive. But with a white background, and each section having its own color, I think it can work.

Here are the colors I picked:

<div class="colorize blue inline" style="width:50px;height:50px;"></div>
<div class="colorize green inline" style="width:50px;height:50px;"></div>
<div class="colorize purple inline" style="width:50px;height:50px;"></div>
<div class="colorize yellow inline" style="width:50px;height:50px;"></div>
<div class="colorize pink inline" style="width:50px;height:50px;"></div>

They'll rotate through in that order on the homepage as I add more sprints, and then each sprint page (like this one) will be just that color.

I also picked two fonts to use, both from [Google Web Fonts](http://www.google.com/fonts):

- <p class="serif"><a href="http://www.google.com/fonts/specimen/Quando">Quando</a> for headings</p>
- <p class="sans-serif"><a href="http://www.google.com/fonts/specimen/Average+Sans">Average Sans</a> for body text</p>

## January 18

## January 19

## January 20

## January 21

## January 22

## January 23
Focus on navigation

Today I focused on the navigation, both design and content.

I played out a few options, including having current and/or future sprints listed in the nav, but ultimately decided that I liked a small list of pages better. These pages would have content that doesn't fit cleanly into a sprint.

The important non-sprint content seems to be:

- Information about me
- Information about sprints and what I'm doing with this site
- Future sprint ideas
- Miscellaneous other things I work on that aren't a sprint

I worked on the design at the same time, designing out ideas that I didn't end up liking, before landing on the above content laid out beneath a logo.

## January 24

## January 25
Calendar idea

Up until now, I'd just been creating a big page of progress through a sprint (see the [screenshots](#january-16 "calendar") from last week). But today I thought of this calendar idea, which required a total reworking of the sprint data/content and the build tool.

However, after a few hours spent on those two tasks, both are much, *much* better now. Plus the sprint pages are prettier and more interesting too.

## January 26
Focus on mobile

Today I started looking at the site on my phone, and adding some media queries to make it look a lot better.

Basically my strategy is just to have mostly default styles, with a few that are either specific to screens wider than 480px, and a few that are overrides for screens between 320px and 480px wide.

## January 27
Adding generic pages

After decided that I wanted some pages for general information in the navigation (see the [navigation details](#january-23 "calendar") from a couple days ago), I still hadn't actually made those pages.

Today I worked on the following pages:

- Future sprints
- Miscellaneous things I've made
- More information about me
- Rules for sprints, and a description of what I'm doing here

I still have content to work on, but I did add functionality to my build tool to grab this content from the correct files and create the pages.

## January 28

## January 29
A new writing environment

I've been working entirely in Sublime Text, and I absolutely love Sublime for coding. However, for writing, it's not the best.

I've heard a lot of really good things about [Byword](http://bywordapp.com) and I decided to take the leap and buy it. It's absolutely perfect for my needs. It does everything I want a Markdown editor to do, making my writing look really nice while I'm working.

> <img src="this-website/screenshot-3.png" width="450" height="450" alt="screenshot of writing" />

## January 30

## January 31
Calendar functionality

Today I made the calendar on the sprint pages actually functional, so you can click the dates and interact with it, and it behaves all as expected with regards to the hash in the URL.

## February 01
Content and loose ends

Today I worked on writing content and finishing up some loose ends that are required before I publish my site. These include:

- Google Analytics
- Adding needed links and images to posts
- Adding contact information
- Designing some little things that haven't been designed yet