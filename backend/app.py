import re
url = input("URL: ")

def get_product_id(url):
    product = {}
    '''
    This is a function which takes in the url and rerturns a dict containing
    the e-commerce service name and product id
    '''
    product["name"] = re.findall("^(?:https?://)?(?:www\.)?([a-zA-Z0-9]+)(?:\.*)", url)[0]
    
    if product["name"].lower() in ["ebay", "amazon", "etsy", "walmart", "aliexpress", "target"]:
        if product["name"] == "walmart":
            id = re.findall("(?:/)([a-zA-Z0-9]+)", url)[3]
        else:
            id = re.findall("(?:/)([a-zA-Z0-9]+)", url)[2] 
        product["id"] = id  

    print(product)
    return product
    

get_product_id(url)