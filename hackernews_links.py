import logging
import time
import json
from openai import OpenAI

import webql
from webql.sync_api.web import PlaywrightWebDriver

#logging.basicConfig(level=logging.DEBUG)
#log = logging.getLogger(__name__)

URL = "https://news.ycombinator.com/"

if __name__ == "__main__":
    driver = PlaywrightWebDriver(headless=False)
    session = webql.start_session(URL, web_driver=driver)

QUERY = """
{
    articles[] {
        title_link
    }
}
"""

response = session.query(QUERY)

#Print the first link
first_link = print(response.articles[0].title_link.get_attribute('href'))
print(first_link)


#grab all the links, put it in a list and print it
links = [ article.title_link.get_attribute('href') for article in response.articles ]
print(links)

