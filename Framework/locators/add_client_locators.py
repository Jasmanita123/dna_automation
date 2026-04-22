class AddClientLocators:
   

    MODAL = ".ant-modal-content"
    CLIENT_INPUT = "input[name='Client']"

    INDUSTRY_DROPDOWN = "xpath=(//div[contains(@class,'ant-select-selector')])[6]"
    INDUSTRY_OPTION = "xpath=//div[contains(@class,'ant-select-item-option') and @title='{}']"
    SECTOR_DROPDOWN = "xpath=(//div[contains(@class,'ant-select-selector')])[7]"
    SECTOR_OPTION = "xpath=//div[contains(@class,'ant-select-item-option') and @title='{}']"
    DROPDOWN_OPTION = "xpath=//div[contains(@class,'ant-select-item-option')]"
    
    DROPDOWN_POPUP = ".ant-select-dropdown:visible"
    DROPDOWN_SEARCH_INPUT = "input.ant-select-selection-search-input"
    SAVE_BUTTON = "button:has-text('Save')"