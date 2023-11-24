import json
import logging
from dotenv import load_dotenv
from llm import OpenAi
from ocr import Ocr

import secrets as st

def process_invoice(invoice_image_path, schema_path, prompts_path):
    try:
        llm = OpenAi().gpt
        ocr = Ocr(invoice_image_path)
        invoice_text = ocr.detect_text()

        with open(schema_path, 'r') as f: 
            schema = json.load(f)

        with open(prompts_path) as f:
            prompts = json.load(f)

        input_data = {
            "text": invoice_text,
            "prompts": prompts,
            "schema": schema
        }

        response = llm.predict(json.dumps(input_data))
        return response

    except Exception as e:
        logging.error(f"Error processing invoice: {e}")
        return None

if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    invoice_image_path = st.secrets["INVOICE_IMAGE_PATH"]
    # invoice_image_path = os.getenv('INVOICE_IMAGE_PATH')
    schema_path = st.secrets['SCHEMA_PATH']
    # schema_path = os.getenv('SCHEMA_PATH')
    prompts_path = st.secrets['PROMPTS_PATH']
    # prompts_path = os.getenv('PROMPTS_PATH')

    response = process_invoice(invoice_image_path, schema_path, prompts_path)
    if response:
        print(response)
    else:
        print("Failed to process invoice.")