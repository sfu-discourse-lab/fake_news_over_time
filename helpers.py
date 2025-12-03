import os
from typing import Any
import pandas as pd
from spacy.tokens.token import Token
from wordcloud import WordCloud
from scipy.stats import normaltest, levene, f_oneway, kruskal


def load_misinfotext():
    df = pd.read_excel(
        "./data/MisInfoText/PolitiFact_original_modified.xlsx", 
        sheet_name="Working",
        usecols=["factcheckURL", "originalBodyText", "originalHeadline", "originalTextType", "originalDateYear"]
    )

    df = df.rename(
        {
            "factcheckURL": "id",
            "originalBodyText": "text",
            "originalHeadline": "headline",
            "originalTextType": "text_type",
            "originalDateYear": "year",
        },
        axis="columns"
    )
    
    return df


def load_fakespeak():
    df = pd.read_excel(
        "./data/Fakespeak-ENG/Fakespeak-ENG modified.xlsx",
        sheet_name="Working",
        usecols=["ID", "originalBodyText", "originalHeadline", "originalTextType", "originalDateYear"]
    )

    df = df.rename(
        {
            "ID": "id",
            "originalBodyText": "text",
            "originalHeadline": "headline",
            "originalTextType": "text_type",
            "originalDateYear": "year",
        },
        axis="columns"
    )
    
    return df


def load_data():
    df = pd.concat([
        load_misinfotext(),
        load_fakespeak()
    ])

    # Removing 2007 and 2008 years because little data in them
    df = df[~(df["year"] == 2007) & ~(df["year"] == 2008)]

    return df


def get_years_dfs(file_path: str):
    """Get separate dataframes for each year in an analysis output. 
    Skip any summary-type sheet."""


    excel_file = pd.ExcelFile(file_path)

    return [
        pd.read_excel(excel_file, sheet_name=sheet)
        for sheet in excel_file.sheet_names
        if str(sheet).isdigit()
    ]
    

    # def generator():
    #     # Generator that goes through each year sheet,
    #     # adds a year column, then returns the dataframe
        
    #     for sheet in excel_file.sheet_names:
    #         if sheet == "Summary":
    #             continue
            
    #         df = pd.read_excel(excel_file, sheet_name=sheet)

    #         # Add year column
    #         df["year"] = sheet

    #         yield df
    
    # # Create a list from the generator and return
    # return list(generator())


def get_groups(df: pd.DataFrame, col: str):
    """Separate dataframes into groups. 
    Returns the group names and the separated dataframes."""
    
    grouped = df.groupby(by=col)

    keys = list(grouped.groups.keys())
    dfs = [grouped.get_group(key) for key in keys]

    return keys, dfs


def generate_wordclouds_for_years(filename: str, text_col: str, count_col: str):
    """This function is used in the word cloud generation notebooks."""

    excel_file = pd.ExcelFile(filename)

    for year in excel_file.sheet_names:
        df = pd.read_excel(excel_file, sheet_name=year)
        df = df.dropna(subset=[text_col])

        # Sometimes we don't have any entities in a file
        # (usually in the social media headlines).
        if df.shape[0] == 0:
            continue
        
        frequencies = dict(zip(df[text_col], df[count_col]))
        
        wordcloud = WordCloud(
            width=800, 
            height=400,
            font_path="./Lato-Regular.ttf", # Using the open source Lato font
            colormap="managua",
            background_color="white")\
            .generate_from_frequencies(frequencies)

        yield year, wordcloud


def is_word(token: Token):
    return not (token.is_punct or token.is_space)


def run_stats_test(dfs: list[pd.DataFrame], col: str):
    """Automatically decides whether to run a parametric or non-parametric test by 
    first checking if the given inputs are all normally distributed and have equal variance.
    Using p-value <= 0.05 for all tests."""
    
    samples = [df[col].dropna() for df in dfs]

    def run_non_normal():
        print("Running test for non-normal distributions")
        return kruskal(*samples)

    def run_normal():
        print("Running test for normal distributions")
        return f_oneway(*samples)


    if levene(*samples).pvalue <= 0.05:
        return run_non_normal()
    
    for sample in samples:
        # Minimum sample size for normaltest
        if len(sample) < 8:
            return run_non_normal()
        
        if normaltest(sample).pvalue <= 0.05:
            return run_non_normal()
    
    return run_normal()