import openai
openai.api_key = "INSERT_API_KEY_HERE"

def categorize_feedback(feedback, feedback_type):
    """
    Categorizes feedback based on the feedback type selected by the user.
    Utilizes OpenAI's GPT-3 natural language processing to classify the feedback.
    Returns a tuple of the feedback and its categorized tag.
    """
    prompt = f"Please categorize the following feedback as {feedback_type}: {feedback}"
    model = "text-davinci-002"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    feedback_tag = response.choices[0].text.strip()
    return (feedback, feedback_tag)
