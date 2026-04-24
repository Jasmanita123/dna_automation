import time

from UI_Automation.pages.create_pursuit_page import CreatePursuitPage
from UI_Automation.utils.logger import get_logger
from UI_Automation.utils.test_data import CLIENT_DATA, CREATE_PURSUIT_REQUIRED_ERRORS, PURSUIT_DATA
import UI_Automation.utils.test_data as test_data

logger = get_logger(__name__)

def test_create_pursuit(logged_in_page):
    try:
        logger.info("Test started: Create Pursuit")
    
        create_pursuit_page = CreatePursuitPage(logged_in_page)

        client_name = f"AutoClient_{int(time.time())}"
        pursuit_name = f"AutoPursuit_{int(time.time())}"
        test_data.CREATED_PURSUIT_NAME = pursuit_name

        #Create a pursuit by clicking on the create pursuit option available in the side pane
        logger.info("Opening Create Pursuit page")
        create_pursuit_page.click_create_pursuit()

        #Click on the create button without providing any details and validate
        logger.info("Validating required field errors")
        create_pursuit_page.click_create_without_data()
        #validate if the error messages are displayed for all the required fields that are not provided.
        create_pursuit_page.validate_required_errors(CREATE_PURSUIT_REQUIRED_ERRORS)
        create_pursuit_page.click_create_pursuit()

        #Validate if 2 buttons are displayed at the bottom (Cancel and Create)
        logger.info("Validating footer buttons")
        create_pursuit_page.validate_footer_buttons()

        #Add a new client using the + icon available
        logger.info("Adding new client")
        create_pursuit_page.click_add_client_icon()
        create_pursuit_page.add_new_client(
            client_name,
            CLIENT_DATA["industry"],
            CLIENT_DATA["sector"]
        )
    
        # Fill pursuit details
        logger.info("Filling pursuit details")
        create_pursuit_page.fill_pursuit_details(
            pursuit_name=pursuit_name,
            #client_name=client_name,
            proposal_type=PURSUIT_DATA["proposal_type"],
            project_type=PURSUIT_DATA["project_type"],
            country=PURSUIT_DATA["country"],
            billing_arrangement=PURSUIT_DATA["billing_arrangement"],
            start_date=PURSUIT_DATA["start_date"],
            end_date=PURSUIT_DATA["end_date"],
            jupiter_id=PURSUIT_DATA["jupiter_id"],
        )
        logger.info("Creating pursuit")
        create_pursuit_page.click_create()

        #Validate the message displayed after creating a pursuit successfully
        logger.info("Validating success message")
        create_pursuit_page.validate_success_message()   

        logger.info("Test passed: Create Pursuit completed successfully")

    except Exception as e:
        logger.exception(f"Test failed: Create Pursuit failed due to: {e}")
        raise