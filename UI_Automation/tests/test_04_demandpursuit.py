from UI_Automation.pages.create_pursuit_page import CreatePursuitPage
from UI_Automation.pages.demand_pursuit_page import DemandPursuitPage
from UI_Automation.utils.logger import get_logger
from UI_Automation.utils.test_data import DemandPursuitData as D
import UI_Automation.utils.test_data as test_data

def test_demand_pursuit_update(logged_in_page):
    logger = get_logger("test_demand_pursuit_update")
    demand_pursuit_page = DemandPursuitPage(logged_in_page, logger)

    # Replace this with the actual pursuit name created in your previous test
    created_pursuit_name = test_data.CREATED_PURSUIT_NAME

    logger.info("Starting Demand Pursuit update test")

    # Step 1: Navigate to demand pursuit page
    demand_pursuit_page.navigate_to_demand_pursuit_page()

    # Step 2: Open All category and search pursuit
    # demand_pursuit_page.open_all_category()
    demand_pursuit_page.search_pursuit(created_pursuit_name)
    

    # Step 3: Validate pursuit in All category table
    demand_pursuit_page.validate_pursuit_details(
        expected_name= test_data.CLIENT_NAME_CELL
    )
    #row = demand_pursuit_page.validate_pursuit_present_in_table(test_data.CLIENT_NAME_CELL)
    #demand_pursuit_page.validate_table_details(
       # row=row,
       # expected_name= test_data.CLIENT_NAME_CELL
    #)

    # Step 4: Click pursuit and validate details page
    #demand_pursuit_page.click_pursuit_from_table(row)
    demand_pursuit_page.validate_pursuit_details_page(created_pursuit_name)

    