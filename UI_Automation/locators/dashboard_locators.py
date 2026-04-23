class DashboardLocators:
    CATEGORY_ITEMS = "div.ant-card.dna-card-tab"   # replace with stable locator if possible
    PURSUIT_LIST_OPTION = "text=List of all Pursuits"

    #Profile locator
    PROFILE_CONTAINER = ".user-profile-container"
    PROFILE_TRIGGER = ".user-profile-trigger"
    PROFILE_NAME = ".user-profile-trigger-info"


    APPLICATIONS_ICON = "[title='Applications'], [aria-label='Apps']"
    NOTIFICATIONS_ICON = "[title='Notifications'], [aria-label='Notifications']"

    LEFT_PANE = "nav, aside, [aria-label='Navigation']"
    
    COLLAPSE_BUTTON = "[aria-label='Expand menu'], [title='Expand menu']"
    
    DEMAND_PURSUITS_OPTION = "[aria-label='Demand Pursuits'], [title='Demand Pursuits']"
    CREATE_PURSUIT_OPTION = "[aria-label='Create Pursuit'], [title='Create Pursuit']"