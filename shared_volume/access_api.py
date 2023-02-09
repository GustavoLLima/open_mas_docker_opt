#https://www.nylas.com/blog/use-python-requests-module-rest-apis/

import requests
# response = requests.get("http://api.open-notify.org/astros.json")
# print(response)

# query = {'lat':'45', 'lon':'180'}
# response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
# print(response.json())






try:
	#solicita_register('" ("m1") "'" "," (1) ", " (400) ")
    response = requests.post('http://localhost:5000/api/v1/resources/solicita_register', json = {"model":"m1", "min":1, "max":400}, timeout=5)
    response.raise_for_status()

    print(response)
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)


#from db_python_netlogo import testing_send
#testing_send('" (agent_id) "', '" tupla "', '" (updated_historic) "')
#agent_id, data, path
try:
	#solicita_register('" ("m1") "'" "," (1) ", " (400) ")
    response = requests.post('http://localhost:5000/api/v1/resources/model_to_router', json = {"agent_id":"12", "data":"[1 2 3]", "path":"1-1"}, timeout=5)
    response.raise_for_status()

    print(response)
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)

#from db_python_netlogo import receiving_agents
#receiving_agents('" ("m1") "')
try:
	#solicita_register('" ("m1") "'" "," (1) ", " (400) ")
    response = requests.get('http://localhost:5000/api/v1/resources/check_new_agents', params={"model":"m1"}, timeout=5)
    response.raise_for_status()
    
    str1 = ''.join(str(e) for e in response.json())
    print(str1)
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)






# response.content() # Return the raw bytes of the data payload
# response.text() # Return a string representation of the data payload
# response.json() # This method is convenient when the API returns JSON

# # Create a new resource
# response = requests.post('https://httpbin.org/post', data = {'key':'value'})

# import requests
# params = {"words": 10, "paragraphs": 1, "format": "json"}
# response = requests.get(f"https://alexnormand-dino-ipsum.p.rapidapi.com/", params=params,
#  headers={
#    "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
#    "X-RapidAPI-Key": "4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#  }
# )
# print (type(response.json()))
# print(response.json())