import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    
    # check for prompt, if none print error and return error code
    if len(sys.argv) < 2:
        print("Error! No prompt provided. Usage: python3 main.py \"[ENTER PROMPT HERE]\"")
        exit(1)
    

    prompt = sys.argv[1]

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)]),]

    # loading the stored API key from the .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # passing the client our api_key and saving the client for use
    client = genai.Client(api_key=api_key)

    # get the response
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages,)

    # output response and metadata (i.e. the prompt tokens)
    
    if "--verbose" in sys.argv:
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}\n")

    print(f"Machine said:\n {response.text}")

if __name__ == "__main__":
    main()