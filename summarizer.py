"""This example demonstrates how to leverage to_data() method provided by AgentQL."""
import webql
import logging
from openai import OpenAI

# Importing the default PlaywrightWebDriver from AgentQL library
from webql.sync_api.web import PlaywrightWebDriver

#logging.basicConfig(level=logging.DEBUG)
#log = logging.getLogger(__name__)

# Set the URL to the desired website
URL = "https://en.wikipedia.org/wiki/Pickleball"

if __name__ == "__main__":

    # Set headless to False to see the browser in action
    driver = PlaywrightWebDriver(headless=False)

    # Define the queries to interact with the page
    QUERY = """
    {
        text[]
    }"""

    # Start a session with the specified URL and the custom driver
    session = webql.start_session(URL, web_driver=driver)

    # Make API call(s) to AgentQL server to fetch the query
    response = session.query(QUERY)

    # Leveraging to_data() method to extract the data from the response
    data = response.text.to_data()

    #print(data)

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
        {"role": "system", "content": "You are a internet researcher, you are really good at reading webpages and summarizing content"},
        {"role": "user", "content": "Here is text from a webpage: " + ' '.join(data)},
        {"role": "user", "content": "Summarize this webpage for me"}
         ]
    )

    print(completion.choices[0].message.content)

    # Stop the session
    session.stop()
