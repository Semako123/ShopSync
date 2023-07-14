import re, requests

url = input("URL: ")


def get_product_id(url):
    product = {}
    """
    This is a function which takes in the url and rerturns a dict containing
    the e-commerce service name and product id
    """
    product["name"] = re.findall("^(?:https?://)?(?:www\.)?([a-zA-Z0-9]+)(?:\.*)", url)[
        0
    ]

    if product["name"].lower() in [
        "ebay",
        "amazon",
    ]:
        id = re.findall("(?:/)([a-zA-Z0-9]+)", url)[2]
        product["id"] = id

    return product


def fetch_product_data(id, name):
    headers = {
        "X-RapidAPI-Key": "695de67ec6mshaf2c2a7fd9d97c9p18ea2ejsndbca74d1e018",
    }

    store_api_detail = {
        "amazon": {
            "params": {"api_key": "3ba0325127417000e0b265200ab7ed34"},
            "url": "https://amazon-data-scraper124.p.rapidapi.com/products/",
        },
        "ebay": {
            "url": "https://ebay-search-result.p.rapidapi.com/search/",
            "params": {},
        },
    }

    store = product["name"]
    id = product["id"]
    url = store_api_detail[store]["url"]
    p_data = requests.get(
        url=url + id,
        headers=headers,
        params=store_api_detail[store]["params"],
    )

    print(p_data.json())


product = get_product_id(url)
fetch_product_data(product["id"], product["name"])
