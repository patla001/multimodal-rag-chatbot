import openai
from openai import OpenAI
from PIL import Image
import base64
from io import BytesIO
import os

from prompts import generate_prompt
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_diagnosis(image: Image.Image, symptoms: str) -> str:
    # Convert image to base64
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    prompt = generate_prompt(symptoms)

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{img_str}"}
                    }
                ]
            }
        ],
        max_tokens=1000
    )

    return response.choices[0].message.content

