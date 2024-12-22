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
        self.api_key = None
        
        self.MAX_TOKENS = 3000
        self.model_setting = {
            "model": setting.model,
            "role_message": {
                "role": "system",
                "content": setting.role_prompt
            } ,
            "check_message": {
                "role": "system",
                "content": setting.checking_prompt
            },
            "summary_message": {
                "role": "system",
                "content": setting.summary_prompt
            } 
        }

    # 스크립트가 요리 스크립트인지 판단
    def is_cooking_script(self, data: str) -> bool:
        try:
            response = openai.chat.completions.create(
                model=self.model_setting["model"],
                messages=[
                    self.model_setting["check_message"],
                    {"role": "user", "content": data}
                ],
                temperature=0,
                max_tokens=self.MAX_TOKENS
            )
            result = response.choices[0].message.content
            return (True if result == "True" else False)

        except openai.error.OpenAIError as e:
            print(f"OpenAI API 오류: {e}")
            return "오류 발생"

    # 재료 및 레시피 추출
    def get_summary(self, data: str) -> str:
        try:
            response = openai.chat.completions.create(
                model=self.model_setting["model"],
                messages=[
                    self.model_setting["summary_message"],
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
            print(f"OpenAI API 오류: {e}")
            return "오류 발생"