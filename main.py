import os, argparse
import types
from prompts import system_prompt
from google import genai
from google.genai import types as gtypes
from dotenv import load_dotenv
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from functions.function_calling import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError('Please insert your Gemini API key in the .env file in the "GEMINI_API_KEY" variable')
client = genai.Client(api_key=api_key)

def main():
    print("Hello from youssef-ai!")
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [gtypes.Content(role="user",parts=[gtypes.Part(text=args.prompt)])]
    available_functions = gtypes.Tool(function_declarations=[schema_get_files_info(),schema_get_file_content(),schema_write_file(),schema_run_python_file()])
    for step in range(20):
        try:
            response = client.models.generate_content(model="gemini-2.5-flash",contents=messages,config=gtypes.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt))
            for cand in response.candidates:
                if cand.content:
                    messages.append(cand.content)
            if response.function_calls:
                Parts = []
                for fn in response.function_calls:
                    result_message = call_function(fn, args.verbose)
                    tool_output = result_message.parts[0].function_response.response
                    if not tool_output:
                        raise Exception("Fatal Error")
                    if args.verbose:
                        print(f"-> {tool_output}")
                    Parts.append(tool_output)
                messages.append(gtypes.Content(role="user",parts=[gtypes.Part(text=str(Parts))]))
                continue 
            if response.text:
                print("Final response:\n" + response.text)
                break
        except Exception as e:
            print(f"Error: {e}")
            break
if __name__ == "__main__":
    main()
