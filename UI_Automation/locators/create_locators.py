class CreatePursuitLocators:
    CREATE_BUTTON = "button:has-text('Create')"
    CANCEL_BUTTON = "button:has-text('Cancel')"
    ADD_CLIENT_ICON = "button:has-text('Add New Client')"
    ADD_CLIENT_BUTTON_TEXT = "Add New Client"

    SUCCESS_MESSAGE = "text=Successfully submitted"
    PURSUIT_NAME = "input[placeholder='Enter pursuit name']"
    JUPITER_ID = "input[placeholder='Enter jupiter ID']"

    DATE_DONE_BUTTON = ".ant-picker-ok button, button:has-text('Done')"
    VISIBLE_DROPDOWN = ".ant-select-dropdown:not(.ant-select-dropdown-hidden)"
    OPTION_BY_TITLE = ".ant-select-item-option[title='{value}']"
    OPTION_BY_TEXT = ".ant-select-item-option >> text='{value}'"


# For Date durations :
    PROJECT_DURATION = "input[placeholder='Start date']"

    DATE_PICKER_POPUP = ".ant-picker-dropdown:visible"

    @staticmethod
    def date_cell(date_iso: str) -> str:
        return f"td[title='{date_iso}']:not(.ant-picker-cell-disabled)"