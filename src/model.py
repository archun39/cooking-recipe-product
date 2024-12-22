import openai
import os
from dotenv import load_dotenv
import setting

class ModelManager:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')

        if self.api_key is None:
            raise ValueError("OPENAI_API_KEY를 설정해 주세요.")
        
        openai.api_key = self.api_key
        self.max_tokens = 500
        self.model_setting = {
            
        }