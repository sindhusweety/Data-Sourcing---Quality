

def get_manufact_with_most_afvs():
    endpoint = f"/v1/light_duty_automobiles.xml"
    #response = make_api_request(endpoint)



print("hi")
# Question 1
manufacturer_with_most_afvs = get_manufact_with_most_afvs()
print("Manufacturer with the most light-duty AFVs in the model year 2020:", manufacturer_with_most_afvs)