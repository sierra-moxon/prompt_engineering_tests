import openai
import os


APIKEY_SUFFIX = "apikey.txt"
APIKEY_ENV_SUFFIX = "API_KEY"


def demo():
    api_key = os.environ["OPENAPI_API_KEY"]
    openai.api_key = api_key


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


if __name__ == '__main__':
    demo()
