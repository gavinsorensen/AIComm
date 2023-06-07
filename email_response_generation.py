import openai
from typing import List, Dict

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY_HERE"

def generate_personalized_email_responses(customer_inquiries: List[str], 
                                          customer_responses: List[str], 
                                          business_name: str) -> Dict[str, str]:
    """
    Function to automatically generate personalized email responses using natural language processing and OpenAI's GPT-3 
    based on customer inquiries and communications.
    
    Args:
    - customer_inquiries (List[str]): List of customer inquiries or messages
    - customer_responses (List[str]): List of business' responses to customer inquiries
    - business_name (str): Name of the business using the function
    
    Returns:
    - generated_responses (Dict[str, str]): A dictionary with the original customer inquiry/message as key and the 
        generated personalized email response as value
    """
    
    # Combine customer inquiries and business responses into a single prompt for GPT-3
    prompts = [f"Customer inquiry: {inquiry}\nBusiness response: {response}" 
               for inquiry, response in zip(customer_inquiries, customer_responses)]
    
    # Use GPT-3 to generate personalized email responses
    generated_responses = {}
    for index, prompt in enumerate(prompts):
        try:
            response = openai.Completion.create(
              engine="davinci",
              prompt=prompt,
              temperature=0.5,
              max_tokens=100,
              n = 1, # Only generate one response
              stop=None,
              timeout=10 # Set timeout in case GPT-3 takes too long
            ).choices[0].text.strip()
            generated_responses[customer_inquiries[index]] = response
        except Exception as e:
            # If GPT-3 encounters an error, return an error message instead of a response
            generated_responses[customer_inquiries[index]] = f"{business_name} encountered an error and cannot generate a response at this time. We apologize for the inconvenience."
            print(f"Error generating response for '{customer_inquiries[index]}': {e}")
    
    # Return generated responses
    return generated_responses
