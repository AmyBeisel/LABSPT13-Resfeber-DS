import http.client
import json

# Execute a request to the CDC Covid API
def get_gas_price_state(ste):
  """
    Awesome function
  """

  # Fetch the Covid API key from an environment variable
  MY_GAS_PRICE_API_TOKEN = os.getenv("GAS_API")

  # Set up an HTTP connection object
  conn = http.client.HTTPSConnection("api.collectapi.com")
  headers = {
      'content-type': "application/json",
      'authorization': "apikey " + MY_GAS_PRICE_API_TOKEN
      # 'authorization': "apikey 4UOowiehxUBAIpKW7urqFe:1MiseQe8cyBvfROjBTLagh"
      }

  # Execute the HTTP GET request
  conn.request("GET", "/gasPrice/stateUsaPrice?state=" + ste, headers=headers)
  res = conn.getresponse()
  data = res.read()

  # Convert the byte data to a json string
  data_json = data.decode("utf-8")
  # Load the json string into a python dict
  data_dict = json.loads(data_json)

  # Return the state level gas prices
  return data_dict['result']['state']
