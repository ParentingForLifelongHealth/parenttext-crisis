
sheet_names = {
    # Data sources, IDs of Google Sheets where the core date is stored.
    # Specific for PCC.
    "localised_sheets" : "1M3ohkdFNWzYQdMBdlnPP2_pi3RttKGXAvCUBgYLvuHA",

    # Shared with all deployments.
    # Multiple content index for different types of content.
    "T_content" : "1hcH8pFdiHZN0UvZgyv3Zht9ARBTx-VXhNBI2o8L7fHU",
    "N_onboarding_data" : "1NujmHWbalM74U0Yl370MABtoYp6vfusUsrpq9a80n2Q",
    "T_onboarding" : "1Sl0Jl_N4cGQi2INmE_EnX_aYUMUrUB6cKbuWVPzirtY",
    "C_ltp_activities" :"1P8OmAMo7_KPVDGSBScRB6ml2e4psCeKS3deG75NFllw",
    "C_modules_all_ages" : "1kGl23QMmUHPUamKxMkNqivYi2zESE7hKX6xkL-WnEM0",
    "N_safeguarding_data" : "1da7Kiw8KJXc026Ydq0lp52m7nP3TjoyWTHuxa74u5Tg",
    "T_safeguarding" : "1bWOyM5yShTTJSaxwqRCrjUzkwbp7DF6_nSF_96YcZ2c",
    "T_delivery" : "1q6E2c4Bg_UvqTmhxAsTIQngwAtj0aFoqu8wsPHnqmaU",
    "N_delivery_data_response" : "1W5Z0usyFcxZo85nXjSbjUj0-mjf7bG646w0BCwlO1pU",
    "T_menu" : "1lIiFjZKS0eXzzo6XwDdqYv4e1A73WFCpWZg5ju-tCZE",
    "N_menu_data_response" : "1Mg1MuS3p2FNMVJl9Qu9ouU9rjzOrPiF3HWleMKHPK3Y",
    "N_menu_data_common" : "1maT0rZGZjm1cyqyr1U6wI3HULiVVyTEV0xqjkkXki8c",

    # Google Sheet ID containing AB testing data. (pre-translation edits)
    # Same for all deployments.
    "ab_testing_sheet_ID" : "1i_oqiJYkeoMsYdeFOcKlvvjnNCEdQnZlsm17fgNvK0s",
    # Crisis specific.
    "localisation_sheet_ID" : "1cyPKUKEkAgaxZMQAVdLqDt9OBEjYXHV2ciIzGKdRfd0", #remove??

    # Google Sheet ID containing dict edits data. (post-translation edits)
    # Same for all deployments.
    "eng_edits_sheet_ID" : "1Ab8H_s26EuOiS4nZ6HGADjD4CZw55586LL66fl8tEWI",
    # Crisis specific.
    "transl_edits_sheet_ID" : "1QxkFWdy56WDHopeHysRVDpEJdDA_b_dKFVQqaMCftrU"
}

creation_spreadsheet_ids = [
    "N_onboarding_data",
    "T_onboarding",
    "C_ltp_activities",
    "C_modules_all_ages",
    "T_content",
    "N_safeguarding_data",
    "T_safeguarding",
    "N_delivery_data_response",
    "T_delivery",
    "N_menu_data_common",
    "N_menu_data_response",
    "T_menu",
    "localised_sheets"
]

# Data used when modifying expiration times.
special_expiration = "./edits/specific_expiration.json"
default_expiration = 1440

# Model that is used as part of the process when the data is extracted from sheets.
models = "models.parenttext_models"

# Languages that will be looked for to localize back into the flows, "language" is the
# 3-letter code used in RapidPro, "code" is the 2 letter code used in CrowdIn.
languages = [
    {"language": "fra", "code": "fr"}
]

# Location where translations are stored, at the moment pointing to a locally cloned
# repo, should maybe be adapted so we can provide a link to an online repo.
translation_repo = "https://github.com/IDEMSInternational/plh-digital-content"
folder_within_repo = "translations/parent_text_crisis_global"

# In one of the latter stages we have the option to modify the quick replies:
# 1 - We may want to remove the quick replies and add them to message text and give
#     numerical prompts to allow basic phone users to use the app - for this use
#     reference code "move"
# 2 - We may want to reformat the quick replies so that long ones are added to the
#     message text as above - for this use reference code "reformat"
# 3 - We may not want to do anything, for this use reference code "none"
qr_treatment = "reformat"

# This is the default phrase we want to add in if the quick replies are being moved to
# message text.
select_phrases = "./edits/select_phrases.json"

# If we are in scenario 1 above, we may wish to add some basic numerical quick
# replies back in, if so we need to specify add_selectors as True
add_selectors = "yes"

# Words we always want to keep as full quick replies are specified in this file.
special_words = "./edits/special_words.json"

# In scenario 2 we set limits on the number of quick replies and the length of the
# quick replies.
#   count_threshold (relates to number of quick replies)
#   length_threshold (relates to length of the longest quick reply)
# If the number of QRs is below or equal the count_threshold and the longest QR is
# shorter than or equal to the length_threshold then the QR are to be left in place
# the node will not be changed.
# In places where the QR are too long. We will make the changes to make the QRs
# numbers and add the number references to the message text as example 1.
count_threshold = "3"
length_threshold = "18"

# Names of redirect flows to be modified as part of safeguarding process.
redirect_flow_names = (
    '['
    '    "safeguarding_redirect_to_topic_all", '
    '    "safeguarding_redirect_to_topic_start", '
    '    "safeguarding_redirect_to_topic_trigger"'
    ']'
)


def create_config():
    return {
        "meta": {
            "pipeline_version": "1.0.0",  # version of the pipeline (and thus config format) to be used
            "version": "1.2.3"  # version of the config itself
        },
        "parents": [
            {
                "repo_url": "",
                "commit_hash": "",
                "commit_tag": ""  # instead of commit_hash, to refer to a commit by tag
            }
        ],
        # The name prefix that will be used in filenames during processing.
        "flows_outputbasename": "parenttext_all",
        # Number of files to split the output into
        "output_split_number": 1,
        "sources": {
            # "flow_file": {
            #     "format": "json",
            #     "files_dict": {
            #         "flows": "excel_files/parenttext_all_1_load_from_sheets.json",
            #     }
            # },
            "flow_definitions": {
                "format": "sheets",
                "subformat": "google_sheets",
                # Name of the Python module containing data models describing the data sheets
                "files_list": creation_spreadsheet_ids,
                # "archive": "parenttext_all.zip",
                #"archive": "https://drive.usercontent.google.com/download?id=1V9fQZ9ZrzwRkQWBtlHJ1it0Fe3hdtHs2&export=download&authuser=0&confirm=t&uuid=f9d65ff1-b210-4b61-a030-cd4a231c22ca&at=APZUnTVzz2FLSi1riCmRjCFI5vCx:1696348063599",  # noqa: E501
            },
            "edits_pretranslation": {
                "format": "sheets",
                "subformat": "google_sheets",
                "files_list": [
                    "ab_testing_sheet_ID",
                    "localisation_sheet_ID",
                ],
            },
            "edits_posttranslation": {
                "format": "sheets",
                "subformat": "google_sheets",
                "files_list": [
                    "transl_edits_sheet_ID",
                    "eng_edits_sheet_ID",
                ],
            },
            "translation": {
                "format": "translation_repo",
                "translation_repo": translation_repo,
                "folder_within_repo": folder_within_repo,
                "commit_hash": "",
                "commit_tag": "",  # instead of commit_hash, to refer to a commit by tag
                "languages": languages,
            },
            "expiration_times": {
                "format": "json",
                "files_dict": {
                    # name of JSON file mapping flow names to expiration times
                    "special_expiration_file": special_expiration,
                }
            },
            "qr_treatment": {
                "format": "json",
                "files_dict": {
                    # Path to file with the default phrase (including translations) we want to add if quick replies are being moved to message text.
                    "select_phrases_file": select_phrases,
                    # Path to file containing words (including translations) we always want to keep as full quick replies.  
                    "special_words_file": special_words,
                }
            },
            "safeguarding": {
                # Hopefully to be deprecated soon
                "format": "safeguarding",
                # "filepath": None,
                "sources" : [
                    {
                        "key": "fra",
                        "path": "excel_files/safeguarding crisis.xlsx",
                    }
                ],
            },
            "goals_api": {   
                "format": "sheets",
                "subformat": "google_sheets",
                # TODO: This is for WashText, put the correct ID here for crisis
                "files_list": ["1TJ1YVSu87ubc5GvGea2hfRh4v234OyJUccQnZ90VUP4"]
            },
        },
        "steps": [
            # {   
            #     "id": "load_flows",
            #     "type": "load_flows",
            #     "sources": ["flow_file"],
            # },
            {   
                "id": "create_flows",
                "type": "create_flows",
                "models_module": models,  # Name of the Python module containing data models describing the data sheets
                "sources": ["flow_definitions"],
                # "archive": "parenttext_all.zip",
                #"archive": "https://drive.usercontent.google.com/download?id=1V9fQZ9ZrzwRkQWBtlHJ1it0Fe3hdtHs2&export=download&authuser=0&confirm=t&uuid=f9d65ff1-b210-4b61-a030-cd4a231c22ca&at=APZUnTVzz2FLSi1riCmRjCFI5vCx:1696348063599",  # noqa: E501
                "tags": [4,"response"],
                #"tags": [1,"onboarding",1, "safeguarding",1,"delivery",4,"response"],
            },
            {
                "id": "update_expiration_times",
                "type": "update_expiration_times",
                "sources": ["expiration_times"],
                "default_expiration_time": default_expiration,
            },
            # {   
            #     "id": "split_attachments",
            #     "type": "split_attachments",
            # },
            {   
                "id": "edits_pretranslation",
                "type": "edits",
                "sources": ["edits_pretranslation"],
            },
            {
                "id": "hasanyword_pretranslation",
                "type": "has_any_word_check",
            },
            {
                "id": "overall_integrity_check_pretranslation",
                "type": "overall_integrity_check",
            },
            {
                "id": "extract_texts_for_translators",
                "type": "extract_texts_for_translators",
            },
            {   
                "id": "translation",
                "type": "translation",
                "sources": ["translation"],
                "languages": languages,
            },
            {   
                "id": "edits_posttranslation",
                "type": "edits",
                "sources": ["edits_posttranslation"]
            },
            {
                "id": "hasanyword_posttranslation",
                "type": "has_any_word_check",
            },
            {
                "id": "fix_arg_qr_translation",
                "type": "fix_arg_qr_translation",
            },
            {
                "id": "overall_integrity_check_posttranslation",
                "type": "overall_integrity_check",
            },
            {
                "id": "qr_treatment",
                "type": "qr_treatment",
                "sources": ["qr_treatment"],
                # str: how to process quick replies
                # move: Remove quick replies and add equivalents to them to the message text, and give numerical prompts to allow basic phone users to use the app.
                # move_and_mod: As above but has additional functionality allowing you to replace phrases
                # reformat: Reformat quick replies so that long ones are added to the message text, as above.
                # reformat_china: Reformat quick replies to the standard as requested by China
                # wechat: All quick replies moved to links in message text as can be used in WeChat
                # none: Do nothing.
                "qr_treatment": qr_treatment,  
                # When qr_treatment is 'reformat', set limits on the number of quick replies that are processed.
                # If the number of quick replies is below or equal to count_threshold then the quick replies are left in place.
                "count_threshold": count_threshold,
                # When qr_treatment is 'reformat', set limits on the number of quick replies that are processed.
                # If the character-length of the longest quick reply is below or equal to length_threshold then the quick replies are left in place.
                "length_threshold": length_threshold,
                # If qr_treatment is 'move', add some basic numerical quick replies back in. Valid values are 'yes' or 'no'.
                "add_selectors": add_selectors,
            },
            {   
                "id": "safeguarding",
                "type": "safeguarding",
                "sources": ["safeguarding"],
                # "flow_uuid": "b83315a6-b25c-413a-9aa0-953bf60f223c",
                # "flow_name": "safeguarding_wfr_interaction",
                "redirect_flow_names": redirect_flow_names,
            }
        ]
    }
       
