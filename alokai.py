"""This example demonstrates how to leverage to_data() method provided by AgentQL."""
import webql

# Importing the default PlaywrightWebDriver from AgentQL library
from webql.sync_api.web import PlaywrightWebDriver

import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


# Set the URL to the desired website
URL = "https://demo.vuestorefront.io/category/men/men-shoes-sneakers"

if __name__ == "__main__":

    # Set headless to False to see the browser in action
    driver = PlaywrightWebDriver(headless=False)

    # Define the queries to interact with the page
    QUERY = """
    {
        shoes[]
        {
            title
            price
        }
    }"""

    # Start a session with the specified URL and the custom driver
    session = webql.start_session(URL, web_driver=driver)

    # Make API call(s) to AgentQL server to fetch the query
    response = session.query(QUERY)

    # Leveraging to_data() method to extract the data from the response
    data = response.shoes.to_data()

    print(data)

    # Stop the session
    session.stop()