# Fake news over time

Working repo, for a project on analyzing the language of fake news over time (2007-2024). Researchers: Nele Põldvere (University of Oslo/Lund University), Silje Susanne Alvestad (University of Oslo), Maite Taboada (Simon Fraser University). RAs: Jodie Lee, [Adam Podoxin](https://adampodoxin.github.io/) (SFU).

## Data

## Analysis

We use mainly spacy and NLTK to conduct the analysis on the corpus based on multiple linguistic features. The dataset is grouped by year and the analysis is done on each group so that we can compare how these features changed throughout the years.

- All-caps: proportion of all-uppercase words to total words in a text, excluding punctuation, per year
- Keyness: analysis of "most important" words per year as per the `corpus_toolkit` module's keyness analysis
- Lexical density: proportion of lexical words (proper nouns, nouns, verbs, adjectives, adverbs) to total words, excluding punctuation
- Lexical diversity: ratio of number of types to number of total tokens, including punctuation
- LIWC: we run LIWC-22 on the data and get all of the stats provided, then pick out the summary stats to get a general idea of the psycholinguistic features in the texts
- Named entity recognition: we extract the most frequent named entities from each year
- N-grams: we extract the most frequent 1- to 5-grams from each year
- Parts of speech: we track the frequency of spacy's universal parts of speech across the years
- Quotes: we extract direct and indirect quotes using code from the Gender Gap Tracker, then track the number of quotes per article and the proportion of quote tokens to total tokens
- Sentiment: polarity and subjectivity

## Visualization

# Notes

- Most of the social media articles don't have a headline (which makes sense)
  - It seems that for Fakespeak headlines, there are no proper noun entities in social media text type
