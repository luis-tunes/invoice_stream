import streamlit as st
import tempfile
from PIL import Image
from main import process_invoice

schema_path = 'schema.json'
prompts_path = 'prompts.json'

st.title('Invoice Processor')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    clicked = st.button('Process Invoice')

    if clicked:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as f:
            image.save(f, "JPEG")
            invoice_image_path = f.name

        result = process_invoice(invoice_image_path, schema_path, prompts_path)
        st.write(result)