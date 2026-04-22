class CreatePursuitLocators:
    CREATE_BUTTON = "button:has-text('Create')"
    CANCEL_BUTTON = "button:has-text('Cancel')"
    ADD_CLIENT_ICON = "button:has-text('Add New Client')"
    ADD_CLIENT_BUTTON_TEXT = "Add New Client"

    #PURSUIT_NAME = "input[name='pursuitName']"
    #CLIENT_FIELD = "input[name='client']"
    #OPPORTUNITY_TYPE = "select[name='opportunityType']"
    #DESCRIPTION = "textarea[name='description']"

    SUCCESS_MESSAGE = "text=Pursuit created successfully"

    CREATE_PURSUIT_BUTTON = "text=Create Pursuit"
    CREATE_WITHOUT_DATA_BUTTON = "text=Create without data"
    ADD_CLIENT_ICON = "button[aria-label='add client']"
    SUBMIT_BUTTON = "button:has-text('Submit')"

    CLIENT_DROPDOWN = "xpath=(//*[normalize-space()='Client']/ancestor::div[contains(@class,'ant-form-item')][1]//div[contains(@class,'ant-select-selector')])[1]"
    PURSUIT_NAME = "xpath=(//*[normalize-space()='Pursuit Name']/ancestor::div[contains(@class,'ant-form-item')][1]//input)[1]"
    PROPOSAL_TYPE_DROPDOWN = "xpath=(//*[normalize-space()='Proposal Type']/ancestor::div[contains(@class,'ant-form-item')][1]//div[contains(@class,'ant-select-selector')])[1]"
    PROJECT_TYPE_DROPDOWN = "xpath=(//*[normalize-space()='Type of Project']/ancestor::div[contains(@class,'ant-form-item')][1]//div[contains(@class,'ant-select-selector')])[1]"
    COUNTRY_DROPDOWN = "xpath=(//*[normalize-space()='Country']/ancestor::div[contains(@class,'ant-form-item')][1]//div[contains(@class,'ant-select-selector')])[1]"
    BILLING_ARRANGEMENT_DROPDOWN = "xpath=(//*[normalize-space()='Billing Arrangement']/ancestor::div[contains(@class,'ant-form-item')][1]//div[contains(@class,'ant-select-selector')])[1]"
    PROJECT_DURATION = "xpath=(//*[normalize-space()='Project Duration']/ancestor::div[contains(@class,'ant-form-item')][1]//input)[1]"
    JUPITER_ID = "xpath=(//*[normalize-space()='Jupiter ID']/ancestor::div[contains(@class,'ant-form-item')][1]//input)[1]"