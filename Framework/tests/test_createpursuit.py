import time

from Framework.pages.create_pursuit_page import CreatePursuitPage
from Framework.utils.test_data import CLIENT_DATA, CREATE_PURSUIT_REQUIRED_ERRORS, PURSUIT_DATA

def test_create_pursuit(logged_in_page):
    
    create_pursuit_page = CreatePursuitPage(logged_in_page)

    client_name = f"AutoClient_{int(time.time())}"
    pursuit_name = f"AutoPursuit_{int(time.time())}"

    create_pursuit_page.click_create_pursuit()

    create_pursuit_page.click_create_without_data()
    create_pursuit_page.validate_required_errors(CREATE_PURSUIT_REQUIRED_ERRORS)
    create_pursuit_page.validate_footer_buttons()

    create_pursuit_page.click_add_client_icon()

    #Add a new client using the + icon available
    create_pursuit_page.add_new_client(
        client_name,
        CLIENT_DATA["industry"],
        CLIENT_DATA["sector"]
    )
    
    # Fill pursuit details
    create_pursuit_page.fill_pursuit_details(
        pursuit_name=pursuit_name,
        client_name=client_name,
        proposal_type=PURSUIT_DATA["proposal_type"],
        project_type=PURSUIT_DATA["project_type"],
        country=PURSUIT_DATA["country"],
        billing_arrangement=PURSUIT_DATA["billing_arrangement"],
        start_date=PURSUIT_DATA["start_date"],
        end_date=PURSUIT_DATA["end_date"],
        jupiter_id=PURSUIT_DATA["jupiter_id"],
    )

    create_pursuit_page.submit_pursuit()
    create_pursuit_page.click_create()
    create_pursuit_page.validate_success_message()