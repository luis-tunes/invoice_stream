import os
from typing import Optional
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from ocr import handle_vision_errors

class OpenAi:
    """
    Provides a lazy initialization wrapper around the ChatOpenAI model.
    """
    def __init__(self):
        self._gpt: Optional[ChatOpenAI] = None

    @property
    def gpt(self):
        if self._gpt is None:
            load_dotenv()
            self._gpt = self.initialize_model()
        return self._gpt

    def initialize_model(self):
        return ChatOpenAI(
            temperature = 0,
            api_key = os.getenv('OPENAI_API_KEY'),
            model = 'gpt-3.5-turbo',
        )
    
    @handle_vision_errors
    def predict(self, text):
        response = self.gpt.predict(text)
        return response