# Import necessary libraries
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

class AI_Agent:
    def __init__(self):
        self.gpt_model = "text-davinci-004"
        self.codex_model = "codex"

    def create_email_draft(self, sender_name, recipient_name, email_subject, email_body):
        # Create email draft using GPT model
        prompt = f"From: {sender_name}\nTo: {recipient_name}\nSubject: {email_subject}\n\nDear {recipient_name},\n{email_body}\n\nBest,\n{sender_name}"
        response = openai.Completion.create(
            engine=self.gpt_model,
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()

    def generate_code(self, language, instructions):
        # Generate code using Codex model
        prompt = f"{instructions} in {language}"
        response = openai.Completion.create(
            engine=self.codex_model,
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()

    def generate_natural_language_explanation(self, code):
        # Generate a natural language explanation for a piece of code using GPT model
        prompt = f"Explain the following code:\n{code}"
        response = openai.Completion.create(
            engine=self.gpt_model,
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()

    def translate_code(self, source_language, target_language, code):
        # Translate code from one programming language to another using Codex model
        prompt = f"Translate the following {source_language} code to {target_language}:\n{code}"
        response = openai.Completion.create(
            engine=self.codex_model,
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()
