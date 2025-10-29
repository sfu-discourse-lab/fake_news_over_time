BASE_CONFIG = {
    "sheet_name": "Working",
    "text_col": "originalBodyText",
    "year_col": "originalDateYear",
    "type_col": "originalTextType"
}

BASE_FAKESPEAK_CONFIG = BASE_CONFIG | {
    "input_path": "./data/Fakespeak-ENG/Fakespeak-ENG modified.xlsx",
    "usecols": ["ID", "combinedLabel", "originalTextType", "originalBodyText", "originalDateYear"],
    "save_cols": ["ID", "combinedLabel", "originalTextType", "originalBodyText"],
    "id_col": "ID"
}

BASE_MISINFOTEXT_CONFIG = BASE_CONFIG | {
    "input_path": "./data/MisInfoText/PolitiFact_original_modified.xlsx",
    "usecols": None,
    "save_cols": ["factcheckURL", "originalURL", "originalTextType", "originalBodyText"],
    "id_col": "factcheckURL"
}
