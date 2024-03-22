"""This example demonstrates how to leverage to_data() method provided by AgentQL."""
import logging
import time
#import pandas as pd

import webql

# Importing the default PlaywrightWebDriver from AgentQL library
from webql.sync_api.web import PlaywrightWebDriver

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


# Set the URL to the desired website
URL = "https://www.crunchbase.com/organization/tiny-fish"

if __name__ == "__main__":

    # Set headless to False to see the browser in action
    driver = PlaywrightWebDriver(headless=False)

    # Define the queries to interact with the page
    QUERY = """
    {
        investors
    }"""

    QUERY2 = """
    {
        investments
    }"""

    QUERY3 = """
    {
        organizations[]
        {
            name
            funding_round
        }
    }"""

    # Start a session with the specified URL and the custom driver
    session = webql.start_session(URL, web_driver=driver)

    # Make API call(s) to AgentQL server to fetch the query
    response = session.query(QUERY)

    data = response.investors.click()

    response = session.query(QUERY2)

    response.investments.click()

    response = session.query(QUERY3)
    data = response.organizations.to_data()
    print(data)

    # Going to the next page:
    
    # Create a query to get the element to click on e.g. QUERY4 = { page2_link } 

    # Write code to run the query and then click on the page
    #
    # response = session.query(QUERY4)
    # data = response.page2.click()
    #
    # Repeat this section of the code for each page
    #     response = session.query(QUERY3)
    #     data = response.organizations.to_data()
    #     print(data)




    # Stop the session
    session.stop()