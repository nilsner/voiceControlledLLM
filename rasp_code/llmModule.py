import os
#from dotenv import load_dotenv
import google.generativeai as genai
import json

#load_dotenv()

# Get your own API key from https://aistudio.google.com/app/apikey
#GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

GEMINI_API_KEY = GEMINI_API_KEY = 'xxxx'
genai.configure(api_key=GEMINI_API_KEY)

class LLMModule:
    # Function to send ingredients to the Gemini API and retrieve recipes
    def call_gemini(self, input_text):
        print(f"user said: ", input_text)
        # Define the prompt to send to the API
        prompt = f"""You are an agent for an app that takes input from users that wants to dispense water. The users will either request cold or hot water. Sometime they will specify the amount of water, sometimes they will not. This is the voice input from the user: "{input_text}"
        ### Instructions:
        - You MUST  make sure that the user asks nicely (if not, set the niceUserRequest boolean to False).
        - The value for the waterAmount should always be in mililiters. If the users use another unit of measurement be sure to convert it.
        - If no amount of water was specified by the user, then the waterAmount should be set to the default value of 200 mililiters.
        - If the water type is not specified by the user then set typeOfWater to the default value of "none" and you should NOT dispense any water. You should instead urge the user to ask again and specify what water type they want since you cannot dispense water without knowing what type. 
        - After dispensing the water please add a farewell response  the user. This should be an inspirational poem about drinking water/ feeling thirsty/ quenching thirst or something else which is water related. Remember: you will only create this final message if the user was nice in their request to you. 
        - Do not include any text, explanations, or markdown formatting.
        - If the user dont specificy which type of water they want, then you should give them an answer that you cannot fulfill their request and type of water should be none.
        - The JSON array must follow this structure exactly:
        {{
            "niceUserRequest": "<boolean>",
            "answer": "<text>",
            "typeOfWater": "<hot/cold/none>",
            "waterAmount": "<integer>"
            "finalResponse": <text>
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
            print(answer)
            return answer
        except:
            return json.loads({{"niceUserRequest": "False"}})

# if __name__ == "__main__":
#     example = LLMModule()
#     response = example.call_gemini("give me water")
#     if response["allowedWater"]:
#         type = response["typeOfWater"]
#         print(f"{type}")
#     else:
#         reason = response["answer"]
#         print(f"{reason}")
