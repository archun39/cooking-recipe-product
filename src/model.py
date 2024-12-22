import openai
import os
from dotenv import load_dotenv
import setting

class ModelManager:
    def __init__(self, setting=setting):
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')

        if self.api_key is None:
            raise ValueError("OPENAI_API_KEY를 설정해 주세요.")
        
        openai.api_key = self.api_key
        self.MAX_TOKENS = 500
        self.model_setting = {
            "model": setting.model,
            "role_message": {
                "role": "system",
                "content": setting.prompt
            }   
        }

    def get_summary(self, data: str) -> str:
        try:
            response = openai.chat.completions.create(
                model=self.model_setting["model"],
                messages=[
                    self.model_setting["role_message"],
                    {"role": "user",
                     "content": data
                    }
                ],
                temperature=0,
                max_tokens=self.MAX_TOKENS
            )
            result = response.choices[0].message.content
            return result
        
        except openai.error.OpenAIError as e:
            print(f"OpenAI 오류: {e}")
            return "오류 발생"
        
