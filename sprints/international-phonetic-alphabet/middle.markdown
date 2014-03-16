## February 25

## February 26
Starting with fonts

Tonight I wanted to find a font so that I could type the IPA. Particularly I wanted to figure out a way to type the IPA here on my site, which would require you to have an IPA font on your computer. Fortunately, CSS web fonts can solve this problem! But before I could find an IPA web font, I got caught up in just figuring out how local fonts can work.

So instead of getting that problem solved, I started putting together a site to organize all the information I was finding about IPA fonts. Here's what that looks like so far:

> [<img src="international-phonetic-alphabet/fonts.png" />](international-phonetic-alphabet/fonts.png)

Definitely not done - barely even started, actually! But I did implement a little tool that I think I'll use a lot. There are a lot of words that I don't know in this field, so I think a good way to remedy that is an inline definition. So if you click on that yellow highlighted word ("diacritics"), the definition will appear right there next to the word.

The other somewhat related thing I did today was submit my application to the [Computational Linguistics grad program](http://www.compling.uw.edu) at the University of Washington!

## February 27
Typing the IPA locally and online

Successfully figured out IPA font stuff tonight. <a href="/ipa/fonts.html">I documented it all</a>, so go check that out if you're interested. For the purposes, of this sprint, figuring this part out allows me to continue with the other stuff I want to do. Tomorrow, I'm going to start documenting all the IPA characters and what sounds the map to and such.

During this research, I found the following really excellent IPA and linguistics resources:

- [ScriptSource](http://scriptsource.org/cms/scripts/page.php?&id=)
- [SIL International](http://www.sil.org)
- [LingTranSoft](http://tiki.lingtransoft.info/ipa)

And finally, here's what it looks like when I type the IPA now:

Before (web fonts):

[krūŋ tʰêːp mahǎː nákʰɔ̄ːn]

After:

<span class="ipa">[krūŋ tʰêːp mahǎː nákʰɔ̄ːn]</span>

(That's the Thai pronunciation of the Thai word for Bangkok.)

## February 28

## March 1

## March 2

## March 3
IPA chart

This weekend was busy, but I started on an interactive and more descriptive version of the [official IPA chart](http://www.langsci.ucl.ac.uk/ipa/IPA_chart_(C)2005.pdf). This has been slow moving, but tonight I pushed my updates to Github, and I'm posting the beginnings of [my version](http://alexburrell.com/ipa/chart.html).

Tonight, as I was reading the definitions of the types of consonents and trying to learn the words, I just sat in front of the mirror watching my lips and tongue as I repeated words. That got pretty bizarre after a while, and now hours later, I'm still uncomfortably aware of my tongue.

## March 4

## March 5
IPA practice

Thinking about pronunciation this much has really been messing with me. Not only am I suffering from "repeat a word enough times and it starts to sound weird" but I'm not sure if I'm saying words right at all anymore. I've been thinking a lot about how my tongue and lips are moving when I talk, and I'm sure I must be talking a little unusually.

After working some more on the consonant and vowel character charts, I started trying to transcribe some English words. Here's what my evening looked like:

> [<img src="international-phonetic-alphabet/ipa-practice.jpg" width="500" height="750" alt="IPA transcription practice" />](international-phonetic-alphabet/ipa-practice.jpg)

Here's my method for this:

- Try to transcribe a word on my own
- Look up the word in the [Dictionary app](https://itunes.apple.com/us/app/dictionary.com-dictionary/id308750436?mt=8) on my phone
- Correct my IPA transcription

So in the image above, you can see that I very seldom got it exactly right on my own. But a bunch of times (all the "!" that I drew) I got it *almost* right. My biggest problem is diacritics - the little symbols before, after, and between the letters.

And one note on that last one, I actually think my transcription is better than theirs. Mine says something like *mih-shih-gin*. Theirs says *mish-ih-gun*. But I say the former, not the latter, in normal speech.

So what's next? Definitely more work to do on the [IPA chart](http://alexburrell.com/ipa/chart.html). I need to learn the diacritics, and a bunch more letters. And I'd like to try IPA transcription for Chinese and Thai, but I'll need a source of truth to correct myself there.

## March 6
Reusable IPA data

I've been thinking about better ways to display the IPA, in ways that would help me understand it better. Ultimately I'd like to tie it together with some interesting language stuff too (e.g. what sounds exist in what languages). So what I really need, instead of a static chart, is a data set describing the IPA. Then I'll be able to process that data, find patterns, and display it in different ways.

And that's what I started tonight! Go check it out: [https://github.com/alexburrell/ipa-info/blob/master/ipa.json](https://github.com/alexburrell/ipa-info/blob/master/ipa.json)

I also did a little more transcription practice, but not much more than what I did [yesterday](#march-5 "calendar"). Putting the IPA into the JSON data format is pretty time consuming. But I'm finding that the more I work with the IPA in general, even doing a menial task, the more comfortable I'm becoming.

## March 7

## March 8
A new view of the IPA

Today I started working on a new tool for viewing the IPA. Here are the priorities:

- Looks good on my phone
- Provides inline definitions for words I might not know yet
- Organized in alphabetical order, based on the English letter that the character looks like, so I'll be able to quickly find characters
- For each letter, group information about:
	- Pronunciation (with examples)
	- How to type it with the [IPA keyboard](/ipa/fonts.html)
	- What languages use that sound

To build this, I'm using the [dataset](https://github.com/alexburrell/ipa-info/blob/master/ipa.json) that I started building a couple days ago. Not all of this information is included yet, but I'll keep building on it as I work.

And here's a screenshot of what this looks like so far:

> [<img src="international-phonetic-alphabet/progress.png" width="259" height="460" alt="screenshot" />](international-phonetic-alphabet/progress.png)

## March 9
Mandarin and the IPA

Today I started looking into how Mandarin is transcribed using the IPA, and any resources out there for this purpose. Here's what I found:

- [Wikipedia's page listing the characters used for Mandarin transcription](http://en.wikipedia.org/wiki/Help:IPA_for_Mandarin)
- [Wikipedia's page on Mandarin phonology](http://en.wikipedia.org/wiki/Standard_Chinese_phonology)
- [A chart mapping pinyin to IPA](http://talkbank.org/pinyin/Trad_chart_IPA.php)
- [A converter between characters and IPA](http://learn-foreign-language-phonetics.com/chinese-pinyin-phonetic-transcription-converter.php?site_language=english)

I also found a lot of discussion about whether the IPA is useful at all for Mandarin. The main argument against seems to be that pinyin can fill that role, and is more specific to Mandarin. This is true - I know pinyin and I would never use the IPA in place of pinyin.

However, I think the IPA serves a different role entirely. The IPA is fantastic for comparing sounds in Mandarin to similar sounds in other languages (or other Chinese dialects), and that's my primary interest. And I think for people learning Mandarin who know the IPA, it could be a useful tool for learning pronunciation. That doesn't replace pinyin as the best way to transcribe characters, or write when you don't know the characters.

I also found this awesome [downloadable Chinese dictionary](http://www.mdbg.net/chindict/chindict.php?page=cedict) that provides data for characters, meanings, and pinyin pronunciation.

## March 10
Thai and the IPA

When I was in Thailand, I lived in an area where the people tended to speak Lao in informal conversation. So inevitably, I did pick up a little Lao, but I didn't realize until just now that Thai and Lao pronunciations are similar enough to [share a page on Wikipedia](http://en.wikipedia.org/wiki/Help:IPA_for_Thai_and_Lao).

I also just learned that there is the [Royal Thai General System of Transcription](http://en.wikipedia.org/wiki/Royal_Thai_General_System_of_Transcription) that describes the official rules for transcribing Thai in the Latin alphabet. Though from [this table](http://en.wikipedia.org/wiki/Thai_alphabet#Alphabetic) the RTGS mostly matches the IPA, with the most notable exceptions being combonation sounds, or sounds that the RTGS transcribes with more than one letter.

There is one consonant sound in Thai that, try as I might, I never did learn to distinguish. There are to *b*-sounding consonants, and I always pronounced them exactly the same. In looking into Thai pronunciation though, I've learned a little more about what the difference is. One is voiced and unaspirated (just a regular *b* sound), while the other is unvoiced and unaspirated (I've heard this described as the *p* in *spin*). I don't know that this will help me distinguish, but it is interesting to know what the physical difference is in what the mouth is doing to pronounce the two.

Another really interesting thing about Thai is that the consonants provide approximately 21 initial sounds, when the same consonants come at the end of a syllable, there are only 8 possible sounds. For example, the consonants that make the *l* and *r* sound at the beginning of a word both make an *n* sound when at the end.

## March 11
Boyfriend thinks I talk funny

I've had more than a few instances in my life, traveling to other parts of the United States, where people ask if I'm from Michigan based purely on my accent. Apparently there's a Michigan accent, which I think is pretty cool. And at least once a week, I'll say a word in conversation with Boyfriend that he thinks is just too funny not to point out.

Here are some of the words he thinks I pronounce strangely:

- **Balance**

> [<img src="international-phonetic-alphabet/balance.jpg" width="450" height="450" alt="pronunciation of balance" />](international-phonetic-alphabet/balance.jpg)
> This is probably the most frequent one he teases me about. While most people, I think, say the first syllable with the same vowel as *cat*, I apparently use an unusual [diphthong](http://en.wikipedia.org/wiki/Diphthong). I say is something like "bey-uhl" for the first syllable.

> And for the second syllable, the dictionary says it should be an "uhns" sound, but I say it with an "i" sound. I think that's more common though.

- **Vigilante**

> [<img src="international-phonetic-alphabet/vigilante.jpg" width="450" height="450" alt="pronunciation of vigilante" />](international-phonetic-alphabet/vigilante.jpg)
> The thirt syllable of this word is almost the exact same situation as above with *balance*, but also for the second syllable, I say an "i" sound where the dictionary says it should be the same as the first syllable of *above*.

- **Mouth**

> [<img src="international-phonetic-alphabet/mouth.jpg" width="450" height="450" alt="pronunciation of mouth" />](international-phonetic-alphabet/mouth.jpg)
> This is another big one that Boyfriend loves to hear me say. He thinks I sound something like a cat when I say it. But the weird thing is, the way he says it almost sound like "mahlth" with an "l" in the middle there.

- **Mountain**

> [<img src="international-phonetic-alphabet/mountain.jpg" width="450" height="450" alt="pronunciation of mountain" />](international-phonetic-alphabet/mountain.jpg)
> The [t-glottalization](http://en.wikipedia.org/wiki/T-glottalization) in the second syllable is definitely not unique to me. However it is different from the official dictionary pronunciation. And my first syllable has the same cat-like quality as *mouth* above.

- **Shut up!**

> [<img src="international-phonetic-alphabet/shutup.jpg" width="450" height="450" alt="pronunciation of shut up" />](international-phonetic-alphabet/shutup.jpg)
> Given that I'm usually saying this in response to Boyfriend mocking the way I say one of the above words, it becomes that much more frustrating when he also mocks this one!

> Here, I'm kind of combining the two words into one, there's an *extremely* exaggerated glottal stop in place of the "t", and I actually think both syllables should have the primary stress marker.

- **Ypsilanti**

> [<img src="international-phonetic-alphabet/ypsilanti.jpg" width="450" height="450" alt="pronunciation of ypsilanti" />](international-phonetic-alphabet/ypsilanti.jpg)
> Ypsilanti is a city in Eastern Michigan, and the name has always entertained Boyfriend. Although my pronunciation differs from the dictionary's opinion, I think I'm actually right in this case. I don't think anyone is ever pronouncing this the way the dictionary says, since the people in Michigan (i.e. the only people every saying Ypsilanti) have my same accent, more or less.

- **Coupon**

	My pronunciation of this is not unusual - it's actually one of the two pronunciations that the dictionary lists for this word: [ˈku pɒn] and [ˈkyu pɒn]. I say the second one, but because that doesn't exactly fit the spelling, Boyfriend still claims I'm wrong.

*Note: All Boyfriend's mocking is in good humor - it doesn't upset me. On the contrary, I think it's really cool when my pronunciation catches his attention enough to comment. I like having a Michigan accent!*

## March 12

## March 13
Language data from Wikipedia

As I mentioned when talking about [Mandarin and the IPA](#march-9 "calendar"), Wikipedia has these awesome pages that list the IPA characters used by different languages.

- [Mandarin](http://en.wikipedia.org/wiki/Help:IPA_for_Mandarin)
- [French](http://en.wikipedia.org/wiki/Help:IPA_for_French)
- [English](http://en.wikipedia.org/wiki/Help:IPA_for_English)
- [Hindi](http://en.wikipedia.org/wiki/Help:IPA_for_Hindi_and_Urdu)

Of course these don't encompass every language, but it's a really great collection of information. What I would love to do is gather the data from these pages and include it in my [IPA json data](https://github.com/alexburrell/ipa-info/blob/master/ipa.json) so that I could create a tool for showing similarities and differences between pronunciation in different languages.

## March 14
Updated data and viewer on Github

Today I fixed up a lot of the JS and CSS that has gotten quite messy over the last couple weeks, and finally committed my latest stuff to Github. Check out [the code](https://github.com/alexburrell/ipa-info) or [the live site](/ipa/ipa.html)!

## March 15
