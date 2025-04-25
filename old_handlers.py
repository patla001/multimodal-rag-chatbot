import os
import base64
from io import BytesIO
from PIL import Image
from pymongo import MongoClient
from dotenv import load_dotenv
import openai  # Correct import

from prompts import generate_prompt

# Load environment variables
load_dotenv()

# Set up API keys and database
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")

# Configure OpenAI API
openai.api_key = OPENAI_API_KEY

# Connect to MongoDB
client = MongoClient(MONGODB_URI)
db = client["symptom_checker"]
collection = db["records"]

def save_case(image_data: str, symptoms: str, output: str):
    collection.insert_one({
        "image": image_data,
        "symptoms": symptoms,
        "response": output
    })

def generate_diagnosis(image: Image.Image, symptoms: str) -> str:
    # Convert image to base64 string
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # Prepare prompt
    prompt = generate_prompt(symptoms)

    # Call GPT-4 Vision
    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "user", "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_str}"}}
            ]}
        ],
        max_tokens=1000
    )

    result = response['choices'][0]['message']['content']
    save_case(img_str, symptoms, result)
    return result

