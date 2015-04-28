## Telugu Language Research Project

Gathering data for a widely spoken but low resource language to help the statistical machine translation community

## Writeups
Every subdirectory (as listed below with point total adjacent) contains a file, writeup.md, that answers the questions posed at [http://mt-class.org/penn/language-research.html] for each extension. Each directory also contains a README that specifies it's contents

## File Structure

### Directories

`project-1/` [1pt] contains directions that describe how to access widely-available Telugu texts

`project-4/` [~1pt] contains a script to transliterate from Telugu script to romanized-Telugu text

`project-5/` [2pts] contains a script that determines the likelyhood that an input was in telugu.

`project-6/` [2pts] contains the .csv file of tweets authored from a region that speaks predominantly Telugu. It also contains a .txt file of the metadata associated with those tweets

`project-8/` [1pt] contains a script to obtain bilingual information from an online source and save it to files as it goes. Another script then combines the files to make one large dictionary file

### Files
`CoreRequirements.md` contains a brief summarization of the morphology and syntactical structure of Telugu

`InitialResearch.md` contains initial research conducted by Luke 'The MT TANK' Carlsson and his Swedish harem

## Writeups Section
Please see below for the text in each directory's writeup.md file.

### Bilingual Dictionary
To obtain the English-Telugu dictionary in this directory, I used information from [http://www.shabdkosh.com](http://www.shabdkosh.com). This website seemed to have the largest list of translated words as well as the easiest to crawl website. I was initially blocked on the site after making too many requests but then I added a wait time and obscured my crawler in order to get all the relevant information. In the end I got over three thousand five hundred for my dictionary.

### Language Identification
`telugu_lang_identifier.py` takes advantage of a very important concept: the telugu language is unique and shares no characters with other languages. Furthermore, the unicode representations of all unique characters exist in the same unicode block, or range, from 0C00–0C7F. This document by the UnicodeConstorium spells out the specifics: [U0C00 Chart](http://unicode.org/charts/PDF/U0C00.pdf). This block is dedicated solely to telugu so my script checks the numerical unicode value of each character from the input stream to determine the language.

    Officially, the language uses no latin characters but it is becoming more frequent to see punctuation integrated into informal writing. In order to handle this correctly, my script returns a probability [0.0 -> 1.0].

    I tested my script on english/french/german sentences, english words, telugu sentences, informal telugu (punctuation), and mixed telugu and english. The results indicated that this simple script was very effective at determining the likelyhood of the input containing telugu.

### Monolingual Data
The monolingual texts used to complete this portion of the assignment come from the wikipedia data dumps. We were able to find samples of language data by using Telugu words as search terms because Google indexes pages written in Telugu.

### Transliteration
Note: This transliterator is INCOMPLETE. The romanized characters for some Telugu script characters are not fully filled out and have been grouped as such in the telugu_transliterator file.
- The transliterator works by taking in a file, either by stdin or the '-f' flag and prints out the transliterated characters to the terminal.
- To Dos:
  - Complete the transliterations for vowels and combined consonants
  - Figure out how to combine all cross-combinations of vowels and vowel symbols (see [http://www.omniglot.com/writing/telugu.htm] for reference)

### Twitter Data
The files in this directory contain the data collected from Twitter to check whether or not Telugu had a significant presence on the social network. After running through all of the tweets, it was discovered that only 16/100 of the tweets collected contained Telugu (either the script or romanized form). This might be due to three possible reasons (copied and pasted from CoreRequirements.md).

> After using the tweepy twitter scraper to look for tweets in Telugu, we found a surprisingly small number of tweets in Telugu from the provinces where Telugu is most commonly spoken. This can be attributed to the fact that the twitter data was collected at ~4:30pm EST which is the middle of the night for the east cost of India. Another reason might be the fact that twitter is a fairly english-centric social network. A majority of the content created and shared on the site is written in english and it should be assumed that most users, regardless of their country of origin, would use english as their preferred language of communication.
