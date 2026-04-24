class DemandPursuitLocators:
    DEMAND_PURSUIT_MENU = "text=Demand Pursuit"
    ALL_CATEGORY_TAB = "role=tab[name='All']"
    SEARCH_INPUT = "input[placeholder='Search Client, Pursuit, JupiterID']"
    SEARCH_ICON = "button.pursuit-search-button"

    PURSUIT_TABLE = "table"
    PURSUIT_TABLE_ROWS = "table tbody tr"

    
    CLIENT_NAME_CELL = "td:nth-child(1)"
    PURSUIT_NAME_CELL = "td:nth-child(2)"
    COUNTRY_CELL = "td:nth-child(5)"

    # Table columns - update these if your app is different
    #PURSUIT_NAME_CELL = "td:nth-child(1)"
    STATUS_CELL = "td:nth-child(7)"
    DESCRIPTION_CELL = "td:nth-child(3)"
    REFERENCE_CELL = "td:nth-child(4)"

    # Details page
    PURSUIT_TITLE = "h1"
    STATUS_DROPDOWN = "select[name='status']"
    DESCRIPTION_TEXTAREA = "textarea[name='description']"
    REFERENCE_INPUT = "input[name='reference']"
    SAVE_BUTTON = "button:has-text('Save')"

    COMMENTS_TEXTAREA = "textarea[name='comment']"
    POST_COMMENT_BUTTON = "button:has-text('Post Comment')"
    COMMENT_LIST = ".comment-item"

    # Category tabs - example names, update as per your application
    OPEN_CATEGORY_TAB = "text=Open"
    IN_PROGRESS_CATEGORY_TAB = "text=In Progress"
    CLOSED_CATEGORY_TAB = "text=Closed"

    SUCCESS_TOAST = "text=success"