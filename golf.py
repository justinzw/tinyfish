import os
import agentql
import pandas as pd

os.environ["AGENTQL_API_KEY"] = "add_your_key_here"

URL = "https://honmagolf.com/sea/product-list"

if __name__ == "__main__":

    PAGE_QUERY = """
    {
        page1
        page2
        page3
        page4
        page5
        next_page
    }"""

    PRODUCTS_QUERY = """
    {
        products[]
        {
            text1
            text2
            text3
        }
    }"""

    session = agentql.start_session(URL)

    #Grab the products in the first page
    response = session.query(PRODUCTS_QUERY)
    data = response.products.to_data()
    df1 = pd.DataFrame.from_dict(data)
    print(df1)

    # Go to next page
    response = session.query(PAGE_QUERY)
    response.next_page.click()

    #Grab the products in the second page

    response = session.query(PRODUCTS_QUERY)
    data2 = response.products.to_data()

    #print(data2)

    df2 = pd.DataFrame.from_dict(data2)
    print(df2)

    # Stop the session
    session.stop()
