import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

load_dotenv()

# Get your own API key from https://aistudio.google.com/app/apikey
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

class LLMModule:
    
    # Function to send ingredients to the Gemini API and retrieve recipes
    def call_gemini(self, input_text):
        #print(f"user said: ", input_text)
        # Define the prompt to send to the API
        prompt = f"""You are an agent for an app that takes input from users that wants to dispnse water, either they will request cold or hot water. This is the voice input from the user: "{input_text}"
        ### Instructions:
        - You need to make sure that they ask nicely (if not, make them ask again and dont provide them with water).
        - They need to say thank you or please.
        - Sometimes you are allowed to be very harsh (they need to greet you, call you sir and say thank you/please) and sometimes only a thank you is enough.
        - Do not include any text, explanations, or markdown formatting.
        - The JSON array must follow this structure exactly:
        {{
            "allowedWater": "<boolean>",
            "answer": "<text>",
            "typeOfWater": "<hot/cold>",
        }}
        """

        # Send the request to the Gemini API
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            response_text = response.text.strip()
            if response_text.startswith("```json") and response_text.endswith("```"):
                response_text = response_text[7:-3].strip()  # Remove ```json and ```

            # Parse the response as JSON directly
            answer = json.loads(response_text)
            #print(answer)
            return answer
        except:
            return json.loads({{"allowedWater": "False"}})

# if __name__ == "__main__":
#     example = LLMModule()
#     response = example.call_gemini("give me water")
#     if response["allowedWater"]:
#         type = response["typeOfWater"]
#         print(f"{type}")
#     else:
#         reason = response["answer"]
#         print(f"{reason}")