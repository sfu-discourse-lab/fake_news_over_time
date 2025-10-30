import os
from typing import Any
from pandas import DataFrame


def get_groups(df: DataFrame, col: str):
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