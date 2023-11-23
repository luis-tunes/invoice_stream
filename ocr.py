import os
from google.cloud import vision
from error_handlers import handle_vision_errors

class Ocr:
    def __init__(self, path):
        self.path = path
        self._client = None

    @property
    def client(self):
        if self._client is None:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'
            self._client = vision.ImageAnnotatorClient()
        return self._client

    def read_image(self):
        with open(self.path, "rb") as image_file:
            content = image_file.read()
        return vision.Image(content=content)

    @handle_vision_errors
    def detect_text(self):
        """Extracts text from image."""
        image = self.read_image()
        response = self.client.text_detection(image=image)
        texts = response.text_annotations # text_annotations
        all_texts = ' '.join([text.description for text in texts])
        return all_texts