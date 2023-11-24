import requests
import json
import xml.etree.ElementTree as ET

# Define the API base URL
base_url = "https://developer.nrel.gov/api/vehicles"

# Replace with your API key if required
api_key = "7iBnQl5GMBgun0YcmqG1N2k4gfK9jwvi7klwdalv"


# Helper function to make API requests
def make_api_request(endpoint, params=None):
    headers = {"Content-Type": "application/json"}
    if api_key:
        params = params or {}
        params["api_key"] = api_key

    print(params)
    print(f"{base_url}{endpoint}")
    print("https://developer.nrel.gov/api/vehicles/v1/light_duty_automobiles.xml?api_key=7iBnQl5GMBgun0YcmqG1N2k4gfK9jwvi7klwdalv")
    response = requests.get(f"{base_url}{endpoint}", params=params, headers=headers)
    response.raise_for_status()
    print(response)
    return response


# Question 1: Find the manufacturer with the most light-duty AFVs in the model year 2020 (Output format: XML)
def get_manufacturer_with_most_afvs():
    print("hiiiiiiiiiiiiiiiiiiiiiiiii")
    endpoint = f"/v1/light_duty_automobiles.xml"
    response = make_api_request(endpoint)
    root = ET.fromstring(response.text)
    max_afvs = 0
    manufacturer_name = ""

    for vehicle in root.findall(".//vehicle"):
        model_year = vehicle.find("model_year").text
        if model_year == "2020":
            afvs_count = len(vehicle.findall(".//afvs/afv"))
            if afvs_count > max_afvs:
                max_afvs = afvs_count
                manufacturer_name = vehicle.find("make").text

    return manufacturer_name


# Question 2: Find alternative fuel types supported by the most current light-duty vehicle categories (Output format: JSON)
def get_fuels_supported_by_current_categories():
    endpoint = "/v1/fuels.json"
    response = make_api_request(endpoint)
    fuels_data = response.json()

    fuels_by_category = {}

    for category in fuels_data["categories"]:
        if category["vehicle_class"] == "LDV" and category["status"] == "current":
            fuels_by_category[category["category_name"]] = category["fuels"]

    # Find the category with the most fuels
    max_fuel_category = max(fuels_by_category, key=lambda k: len(fuels_by_category[k]))
    supported_fuels = fuels_by_category[max_fuel_category]

    return supported_fuels




# Question 1
manufacturer_with_most_afvs = get_manufacturer_with_most_afvs()
print("Manufacturer with the most light-duty AFVs in the model year 2020:", manufacturer_with_most_afvs)

# Question 2
fuels_supported_by_current_categories = get_fuels_supported_by_current_categories()
print("Alternative fuels supported by the most current light-duty vehicle categories:",
      fuels_supported_by_current_categories)

