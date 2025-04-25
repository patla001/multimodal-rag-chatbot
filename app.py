import chainlit as cl
from PIL import Image
from handlers import generate_diagnosis

@cl.on_message
async def handle_message(message: cl.Message):
    symptoms = message.content.strip()

    # Chainlit v2.0 does NOT have message.files – we use message.elements
    image_element = next((e for e in message.elements if e.mime and e.mime.startswith("image")), None)

    if not image_element:
        await cl.Message(content="❌ Please upload an image along with your message.").send()
        return

    if not symptoms:
        await cl.Message(content="❌ Please describe your symptoms in the message.").send()
        return

    image = Image.open(image_element.path)
    result = generate_diagnosis(image, symptoms)

    await cl.Message(content=result).send()

