import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from prompts import system_prompt
from call_function import call_function, available_functions


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    MAX_ITERATIONS = 20

    try:
        for i in range(MAX_ITERATIONS):
            if verbose:
                print(f"\n--- Iteration {i+1} ---")

            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt,
                ),
            )

            if verbose:
                print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                print("Response tokens:", response.usage_metadata.candidates_token_count)

            # Add LLM's reasoning message(s)
            for candidate in response.candidates:
                if candidate.content:
                    messages.append(candidate.content)

            # ✅ Improved: stop only if it's truly a final response
            if response.text and not response.function_calls:
                print("\nFinal response:")
                print(response.text)
                break


            # Handle function calls (tool use)
            if response.function_calls:
                for function_call_part in response.function_calls:
                    function_call_result = call_function(function_call_part, verbose)

                    if (
                        not function_call_result.parts
                        or not function_call_result.parts[0].function_response
                    ):
                        raise Exception("empty function call result")

                    if verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")

                    # Add tool output to conversation
                    messages.append(function_call_result)
            else:
                print("No function calls and no final response. Exiting.")
                break
        else:
            print("Max iterations reached without a final response.")

    except Exception as e:
        print(f"Error during content generation: {e}")



if __name__ == "__main__":
    main()