class AddClientLocators:
   

    

    MODAL = ".ant-modal-content"
    FIRST_INPUT = "input"
    SAVE_BUTTON = "button:has-text('Save')"

    FORM_ITEM_BY_LABEL = (
        "xpath=.//*[normalize-space(text())='{label}']"
        "/ancestor::div[contains(@class,'ant-form-item')][1]"
    )
    SELECTOR_IN_FORM_ITEM = ".ant-select-selector"