import os
from pathlib import Path

class InputManager:
    def __init__(self):
        self.file_path = Path(__file__).parent.parent / "scripts"

    def get_file_path(self, num: int):
        if num not in range(1,5):
            raise ValueError(f"잘못된 파일 번호입니다. 1에서 4로 정해주세요.")

        file_name = f"script{num}.txt"

        return self.file_path / file_name
    
    def read_file(self, num):
        try:
            file_path = self.get_file_path(num)
            with open(file_path, 'r') as file:
                content = file.read()
                return content
            
        except FileNotFoundError:
            return f"파일을 찾을 수 없습니다: {content}"
        except Exception as e:
            return f"알 수 없는 오류 발생: {e}"
    
if __name__ == "__main__":
    input_manager = InputManager()
    try:
        for i in range(1,6):
            try:
                content = input_manager.read_file(i)
                print(content)
            except ValueError as ve:
                print(ve)
            except FileExistsError as fnfe:
                print(fnfe)
    except Exception as e:
        print(e)