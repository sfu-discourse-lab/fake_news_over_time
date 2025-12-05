FAKESPEAK-ENG CORPUS

=====================

The Fakespeak-ENG corpus is a collection of fake and genuine news in English built by the Fakespeak team at the University of Oslo (https://www.hf.uio.no/ilos/english/research/projects/fakespeak/), with funding from The Research Council of Norway (project-ID: 302573).
The texts have been collected from and fact-checked by two fact-checkers based in the USA: PolitiFact and Snopes. Only genuine news was collected from Snopes, while PolitiFact includes both genuine and fake news.
The veracity labels used by PolitiFact are: True, Mostly True, Half True, Mostly False, False, Pants on Fire. The labels used by Snopes are: True, Mostly True, Mixture, Correct Attribution, Legit.
In Fakespeak-ENG, we have standardised the labels, taking PolitiFact as the starting point, to allow for them to be used together. True and Mostly True are the same, while Snopes' Mixture was re-labelled as Half True, and Correct Attribution and Legit as True.
In the counts below, fake news is considered to consist of the labels False, Mostly False, Pants on Fire, and genuine news consists of True, Mostly True, Half True.
We have also made available detailed metadata about the fact-checks and the text types, sources, authors and dates of the original texts, both the body texts and their headlines.

The Fakespeak-ENG corpus consists of two versions, the original version and the balanced version, depending on the users' preferences.

The counts of both versions are as follows (the word counts have been determined in AntConc):

The original version:
--------------------------------------------
#Texts
	#Fake	2964
	#Genuine	1148
#Words
	#Fake	469328
	#Genuine	175481
--------------------------------------------

The balanced version:
--------------------------------------------
#Texts
	#Fake	641
	#Genuine 653
#Words
	#Fake	97952
	#Genuine	97846
--------------------------------------------

The balanced version is balanced in terms of the number of words across fake and genuine news and in terms of the distribution of the news and blog (74%) and social media (26%) text types.
It is also restricted to the labels False, Mostly False, Pants on Fire (fake news) and True, Mostly True (genuine news).

Below we have provided further information about the column headings and content in the spreadsheets (asterisk indicates that the column exists in both versions):

------------------------------------------------------------------------
<ID>* - unique identifier assigned by the Fakespeak team
<factcheckService> - PolitiFact or Snopes
<factcheckURL>* - link to the fact-check
<factcheckAuthor> - author of the fact-check
<factcheckDate> - date when the fact-check was published (Day-Month-Year)
<factcheckCategories> - categories and topics assigned by PolitiFact and Snopes
<factcheckLabel>* - veracity labels assigned by PolitiFact and Snopes
<combinedLabel>* - standardised labels by Fakespeak
<politifactSource> - source category assigned by PolitiFact, NA for Snopes
<politifactSourceDetails> - further source details by PolitiFact, NA for Snopes
<factcheckClaim> - central claim from the original text that was fact-checked
<factcheckHeadline> - headline of the fact-check
<originalURL>* - link to the original text
<originalTextType>* - text type of the original text assigned by Fakespeak: news and blog, social media, press release (note that there are no press releases in the balanced version)
<originalSource>* - name of the source of the original text
<originalBodyText>* - body text of the original text
<originalHeadline>* - headline of the original text
<originalPoster>* - poster or author of the original text
<originalDate>* - date when the original text was published (Day-Month-Year)
-------------------------------------------------------------------------

Note that the earlier version of the Fakespeak-ENG corpus was called the PolitiFact-Oslo Corpus, since that one was based on PolitiFact only. The reference article of the earlier corpus is available open access at: https://doi.org/10.3390/info14120627

We are currently writing up a reference article about the Fakespeak-ENG corpus:

Nele Põldvere, Zia Uddin and Silje Susanne ALvestad.
Out of balance, out of sight: Issues with the design and accessibility of a corpus of fake and genuine news.

The Fakespeak-ENG corpus is distributed under the Attribution-NonCommercial-NonDerivatives (CC BY-NC-ND) license, the most restricted license.