import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from available_functions import available_functions
from call_function import call_function
from config import MAX_ITERS, SYSTEM_PROMPT


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    if verbose:
        args = [arg for arg in sys.argv[1:-1]]
    else:
        args = [arg for arg in sys.argv[1:]]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    try:
        print(generate_content(client, available_functions, messages, verbose))
    except Exception as e:
        print(f"Error in generate_content: {e}")


def generate_content(client, available_functions, messages, verbose):
    for _ in range(MAX_ITERS):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=SYSTEM_PROMPT
            ),
        )

        if verbose:
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)
            print()

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if not response.function_calls:
            return response.text

        function_responses = []
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose)
            if function_call_result.parts:
                if not function_call_result.parts[0].function_response:
                    raise Exception("Function response doesn't exist")
                if verbose:
                    print(
                        f"-> {function_call_result.parts[0].function_response.response}"
                    )
                function_responses.append(function_call_result.parts[0])

        if not function_responses:
            raise Exception("no function responses generated, exiting.")

        messages.append(types.Content(role="tool", parts=function_responses))

    return f"Maximum iterations ({MAX_ITERS}) reached."


if __name__ == "__main__":
    main()
