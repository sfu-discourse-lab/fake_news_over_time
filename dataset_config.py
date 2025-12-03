BASE_CONFIG = {
    "sheet_name": "Working",
    "text_col": "originalBodyText",
    "headline_col": "originalHeadline",
    "year_col": "originalDateYear",
    "type_col": "originalTextType",
    "output_dir": "Analysis_output"
}

BASE_FAKESPEAK_CONFIG = BASE_CONFIG | {
    "name": "Fakespeak",
    "dir": "./data/Fakespeak-ENG",
    "input_path": "./data/Fakespeak-ENG/Fakespeak-ENG modified.xlsx",
    "usecols": ["ID", "originalTextType", "originalBodyText", "originalHeadline", "originalDateYear"],
    "id_col": "ID"
}

BASE_MISINFOTEXT_CONFIG = BASE_CONFIG | {
    "name": "MisInfoText",
    "dir": "./data/MisInfoText",
    "input_path": "./data/MisInfoText/PolitiFact_original_modified.xlsx",
    "usecols": ["factcheckURL", "originalTextType", "originalBodyText", "originalHeadline", "originalDateYear"],
    "id_col": "factcheckURL"
}
