# Fake news over time

Working repo, for a project on analyzing the language of fake news over time (2007-2024). Researchers: Nele Põldvere (University of Oslo/Lund University), Silje Susanne Alvestad (University of Oslo), Maite Taboada (Simon Fraser University). RAs: Jodie Lee, [Adam Podoxin](https://adampodoxin.github.io/) (SFU).

We define "fake news" loosely as news that neglects evidence and facts, including Misinformation (unintentionally false information), Disinformation (intentionally false information), Propaganda, etc. We run several linguistic analyses on our fake news corpus, spanning many years, to see which properties have changed over time and how.

## Data

We combine two fake news corpora, MisInfoText and Fakespeak. They both contain fake news from three main source types, news and blog, press release, and social media. MisInfoText contains news from 2007-2018 while Fakespeak contains news from 2019-2024. The texts in both corpora are sourced from a large database belonging to U.S. fact-checking organization, PolitiFact, and contain exclusively fake news, with no instances of true news.

The two corpora can be found under the `./data` directory.

## Analysis

We use mainly spacy and NLTK to conduct the analysis on the corpus based on multiple linguistic features. The dataset is grouped by year and the analysis is done on each group so that we can compare how these features changed throughout the years. Analysis is done on only body texts, unless stated otherwise.

- All-caps: proportion of all-uppercase words to total words in a text, excluding punctuation, per year
- Keyness: analysis of "most important" words per year as per the `corpus_toolkit` module's keyness analysis
- Lexical density: proportion of lexical words (proper nouns, nouns, verbs, adjectives, adverbs) to total words, excluding punctuation
- Lexical diversity: ratio of number of types to number of total tokens, including punctuation
- LIWC: we run LIWC-22 on the data and get all of the stats provided, then pick out the summary stats to get a general idea of the psycholinguistic features in the texts
- Named entity recognition: we extract the most frequent named entities from each year. Analysis is done on both body texts and headline texts.
- N-grams: we extract the most frequent 1- to 5-grams from each year. Analysis is done on both body texts and headline texts.
- Parts of speech: we track the frequency of spacy's universal parts of speech across the years
- Quotes: we extract direct and indirect quotes using code from the [Gender Gap Tracker](https://github.com/sfu-discourse-lab/GenderGapTracker), then track the number of quotes per article and the proportion of quote tokens to total tokens
- Sentiment: polarity and subjectivity. Analysis is done on both body texts and headline texts.

We run analyses for the entire corpus as well as subsets corresponding to each text type. The analysis output can be found under the `./output` directory.

## Visualization

We use a variety of graphs to visualize our data, using the Matplotlib and Seaborn modules.

- All caps: trendlines with error bands
- Lexical density: trendlines with error bands
- Lexical diversity: trendlines with error bands
- LIWC: trendlines with error bands
- NER: trendlines the overall most frequent entities, as well as word clouds per year
- N-grams: trendlines the overall most frequent entities, as well as word clouds per year
- Parts of speech: trendlines
- Quotes: scatter & box plots for proportion of words in quotes to all words, as well as trendlines with error bands for average number of quotes per article
- Sentiment: trendlines with error bands for all polarities, only positive polarities, only negative polarities, and subjectivity

The visualizations can be found under the `./visualization` directory.

## Misc. Notes

- Most of the social media articles don't have a headline (which makes sense)
