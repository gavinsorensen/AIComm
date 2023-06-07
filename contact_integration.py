import requests

# Establish connection with GoHighLevel API
api_key = "<insert api key>"
base_url = "https://api.gohighlevel.com/v1"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Get all contacts from GoHighLevel
def get_contacts():
    url = f"{base_url}/contacts"
    response = requests.get(url, headers=headers)
    return response.json()

# Add contact to GoHighLevel
def add_contact(name, email, phone):
    url = f"{base_url}/contacts"
    data = {
        "name": name,
        "emails": [{"address": email}],
        "phones": [{"number": phone}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Update contact in GoHighLevel
def update_contact(id, name, email, phone):
    url = f"{base_url}/contacts/{id}"
    data = {
        "name": name,
        "emails": [{"address": email}],
        "phones": [{"number": phone}]
    }
    response = requests.put(url, headers=headers, json=data)
    return response.json()

# Delete contact from GoHighLevel
def delete_contact(id):
    url = f"{base_url}/contacts/{id}"
    response = requests.delete(url, headers=headers)
    return response.json()

# Establish connection with Hubspot API
hapikey = "<insert api key>"
hubspot_url = "https://api.hubapi.com"

hubspot_headers = {
    "Authorization": f"Bearer {hapikey}",
    "Content-Type": "application/json"
}

# Get all contacts from Hubspot
def get_hubspot_contacts():
    url = f"{hubspot_url}/contacts/v1/lists/all/contacts/all"
    response = requests.get(url, headers=hubspot_headers)
    return response.json()

# Add contact to Hubspot
def add_hubspot_contact(firstname, lastname, email, phone):
    url = f"{hubspot_url}/contacts/v1/contact/"
    data = {
        "properties": [
            { "property": "firstname", "value": firstname },
            { "property": "lastname", "value": lastname },
            { "property": "email", "value": email },
            { "property": "phone", "value": phone }
        ]
    }
   
