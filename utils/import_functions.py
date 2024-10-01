import requests


def import_cars_by_brand(brand: str):
    '''
    Function to import cars by brand
    '''

    # uppercase the brand
    brand_upper = brand.upper()

    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    # execute the request
    response = requests.get(endpoint)

    # get the data from the response
    data = response.json()

    return data