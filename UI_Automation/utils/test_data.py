
#Profile details 
EXPECTED_NAME = "hashedintestuser109LastN, hashedintestuser109FirstN"
EXPECTED_EMAIL = "hashedintestuser109@deloitte.com"


CREATE_PURSUIT_REQUIRED_ERRORS = [
    "Client name is required",
    "Pursuit name is required",
    "Proposal type is required",
    "Project type is required",
    "Country is required",
    "Industry is required",
    "Sector is required",
    "Billing arrangement is required",
    "Date range is required",
    "Resolve all the errors to proceed"

]

CLIENT_DATA = {
    "client_name": "AutoClient_1776826609",
    "industry": "Cross Industry",
    "sector": "Others"
}

PURSUIT_DATA = {
    "proposal_type": "RFP",
    "project_type": "Test Automation",   
    "country": "Albania",                 
    "billing_arrangement": "T&M",       
    "start_date": "01/05/2026",
    "end_date": "31/05/2026",
    "jupiter_id": "JUP-12345",
    "description": "Created through automation",
}

CREATED_PURSUIT_NAME = "AutoPursuit_1777003318"
CLIENT_NAME_CELL="AutoClient_1..."
class DemandPursuitData:
    UPDATED_STATUS = "In Progress"
    UPDATED_DESCRIPTION = "Updated through Playwright automation."
    UPDATED_REFERENCE = "REF-AUTO-001"
    COMMENT_TEXT = "Automation comment added for pursuit update validation."
