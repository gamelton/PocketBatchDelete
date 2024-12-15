# Pocket delete saved links
# https://getpocket.com/saves
# Documentation: https://getpocket.com/developer/docs/

import requests
import webbrowser
import time


# Step 1: Add ned application on web portal
# Add application to https://getpocket.com/developer/apps/new type: web, access: all
# Done once
CONSUMER_KEY = '111111-abcdb8fe0c1fcb4c70awxyz' # From https://getpocket.com/developer/apps/
REDIRECT_URI = 'https://getpocket.com/account'

# Step 2: Get request token
# Done once
response = requests.post('https://getpocket.com/v3/oauth/request', headers={'Content-Type': 'application/json; charset=UTF-8', 'X-Accept': 'application/json'}, json={'consumer_key': CONSUMER_KEY,'redirect_uri': REDIRECT_URI})
request_token = response.json()['code']
    
# Step 3: Authorize user
# Click accept request in opened browser
# Done once
auth_url = f'https://getpocket.com/auth/authorize?request_token={request_token}&redirect_uri={REDIRECT_URI}'
webbrowser.open(auth_url)
print("Please authorize the application in your browser and then press Enter here...")
input()

# Step 4: Get access token
# Requires accepted request
# You could set access token statically after first response
# Important to get request token, approve and access token - in one try, otherwise token is invalid
# Done once
response = requests.post('https://getpocket.com/v3/oauth/authorize', headers={'Content-Type': 'application/json; charset=UTF-8', 'X-Accept': 'application/json'}, json={'consumer_key': CONSUMER_KEY,'code': request_token})
access_token = response.json()['access_token']


# Step 5: Get saved links by query
# Requires access token
# Set query variable
query = 'your_query'
response = None
response = requests.post('https://getpocket.com/v3/get', headers={'Content-Type': 'application/json; charset=UTF-8', 'X-Accept': 'application/json'}, json={'consumer_key': CONSUMER_KEY, 'access_token': access_token, 'detailType':'simple','search': query})


# Step 6: Delete saved items
# Requires access token
# Query have to be the same as in Step 5
if response: 
    response_json = None
    response_json = response.json()
    if isinstance(response_json, dict) and 'list' in response_json and 'search_meta' in response_json:
        items = response_json['list']
        if items:
            # Iterate over all items
            for item_key in items:
                item_id = None
                item_id = items[item_key]["item_id"]
                response = requests.post('https://getpocket.com/v3/send', headers={'Content-Type': 'application/json; charset=UTF-8', 'X-Accept': 'application/json'}, json={'consumer_key': CONSUMER_KEY, 'access_token': access_token, 'actions': [{"action" : "delete","item_id" : item_id}]})
            
            # Handle pagination
            while response_json['search_meta']['has_more']:
                new_response = None
                new_response = requests.post('https://getpocket.com/v3/get', headers={'Content-Type': 'application/json; charset=UTF-8', 'X-Accept': 'application/json'}, json={ 'consumer_key': CONSUMER_KEY, 'access_token': access_token, 'detailType':'simple','search': query})
                if new_response:
                    new_response_json = new_response.json()
                    # Check for new items
                    if 'list' in new_response_json and new_response_json['list']:
                        for item_key in new_response_json['list']:
                            item_id = None
                            item_id = new_response_json["list"][item_key]["item_id"]
                            response = requests.post('https://getpocket.com/v3/send', headers={'Content-Type': 'application/json; charset=UTF-8', 'X-Accept': 'application/json'}, json={'consumer_key': CONSUMER_KEY, 'access_token': access_token, 'actions': [{"action" : "delete","item_id" : item_id}]})
                        response_json['search_meta']['has_more'] = new_response_json['search_meta']['has_more']
                        time.sleep(1)
                    else:
                        break
                else:
                    break
    
    else:
        print("Invalid response format or no items found.")
