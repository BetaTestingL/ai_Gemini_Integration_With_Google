# developer Anubhav

import google.generativeai as gen
import os
from dotenv import load_dotenv

load_dotenv()

# Configure the api key

gen.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = gen.GenerativeModel('gemini-1.5-pro-latest')

response = model.generate_content("code to find fibonacci series in python")

print(response.text)