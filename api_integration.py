# Import required libraries for integration
import requests
import json

# Define a function to fetch and understand customer's profile and chat history from GoHighLevel
def fetch_customer_profile_chat_history_from_GoHighLevel(customer_id):
    # Define the API endpoint for fetching customer profile and chat history
    api_endpoint = "https://www.gohighlevel.com/api/v1/customers/{}/chat".format(customer_id)
    
    # Define the required headers for authentication and authorization
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer <access_token>"
    }
    
    # Send a GET request to the API endpoint
    response = requests.get(api_endpoint, headers=headers)
    
    # Convert the response to JSON format
    response_json = json.loads(response.content)
    
    # Extract the relevant information from the response JSON
    customer_profile = response_json["customer_profile"]
    chat_history = response_json["chat_history"]
    
    # Return the extracted customer profile and chat history
    return customer_profile, chat_history

# Define a function to fetch the user's business details from Hubspot
def fetch_user_business_details_from_Hubspot(user_id):
    # Define the API endpoint for fetching user's business details
    api_endpoint = "https://api.hubspot.com/owners/v2/owners/{}".format(user_id)
    
    # Define the required headers for authentication and authorization
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer <access_token>"
    }
    
    # Send a GET request to the API endpoint
    response = requests.get(api_endpoint, headers=headers)
    
    # Convert the response to JSON format
    response_json = json.loads(response.content)
    
    # Extract the relevant information from the response JSON
    business_details = response_json["properties"]
    
    # Return the extracted business details
    return business_details
