import os
from typing import Any
import pandas as pd
from wordcloud import WordCloud


def get_groups(df: pd.DataFrame, col: str):
    grouped = df.groupby(by=col)

    keys = list(grouped.groups.keys())
    dfs = [grouped.get_group(key) for key in keys]

    return keys, dfs


def make_output_path(dataset_config: dict[str, Any], linguistic_feature_name: str):
    return (
        f"{dataset_config['dir']}"
        f"/{dataset_config['output_dir']}"
        f"/{dataset_config['name']}"
        f"_{linguistic_feature_name}.xlsx"
    )


def make_output_path_for_type(dataset_config: dict[str, Any], type: str, linguistic_feature_name: str):
    type_str = "_".join(str(type).split()).lower()

    output_dir = (
        f"{dataset_config['dir']}"
        f"/{dataset_config['output_dir']}"
        f"/{type_str}"
    )

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print("Created directory", output_dir)

    output_path = (
        f"{output_dir}"
        f"/{dataset_config['name']}"
        f"_{type_str}"
        f"_{linguistic_feature_name}.xlsx"
    )

    return output_path


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