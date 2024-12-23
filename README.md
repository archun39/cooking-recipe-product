# Cooking Recipe Product

## 📖 개요
`Cooking Recipe Product`는 요리 영상의 스크립트에서 **재료**와 **조리 과정**을 자동으로 추출하는 AI 기반 애플리케이션입니다.  
이 애플리케이션은 요리 콘텐츠 제작자나 요리 애호가들에게 효율적인 레시피 관리 도구를 제공합니다.

---

## 🎯 주요 기능
- **재료 추출**: 영상 스크립트에서 요리 재료를 자동으로 식별.
- **조리 과정 추출**: 조리 단계와 관련된 주요 단계를 요약.
- **간단한 실행**: 숫자 입력으로 분석할 스크립트를 간편하게 선택.

---

## 🚀 설치 및 실행

### 1. 시스템 요구사항
- Python 3.9 이상
- Docker (선택사항)
- OpenAI API Key

---

### 2. 설치

#### 2.1. 로컬 환경에서 실행
1. 리포지토리 클론:
    ```bash
    git clone https://github.com/archun39/cooking-recipe-product.git
    cd cooking-recipe-product
    ```

2. Python 종속성 설치:
    ```bash
    pip install -r requirements.txt
    ```

3. 환경 변수 설정:
    - `.env` 파일 생성:
      ```bash
      cp .env.example .env
      vi .env
      ```
    - OpenAI API 키를 설정합니다.
      ```plaintext
        OPENAI_API_KEY=your_openai_api_key
      ```

4. 실행:
    ```bash
    python src/main.py
    ```

#### 2.2. Docker로 실행
1. Docker 이미지 빌드:
    ```bash
    docker build -t cooking-recipe-product:1.0 .
    ```

2. 컨테이너 실행:
    ```bash
    docker run -p 8000:8000 --env-file .env cooking-recipe-product:1.0
    ```

---

### 3. 사용 방법

#### 스크립트 설정
`main.py` 파일에서 숫자를 변경하여 분석할 스크립트를 선택합니다:
```python
import input, model

def main():
    # 숫자를 변경하여 분석할 스크립트를 선택합니다 (1~4).
    script = input.InputManager().read_file(2)  # 1번 스크립트를 읽음
    gpt = model.ModelManager()
    res = gpt.get_summary(script)
    print(res)

if __name__ == "__main__":
    main()
```

### 4. 출력 예제
```plaintext
콩나물 비빔밥 (1인용)
[재료]
- 밥 4스푼
- 버섯 (아무 종류) 적당량
- 콩나물 1주
- 간장 2수저
- 고춧가루 1수저
- 참기름 1수저
- 다진 마늘 0.5수저
- 알룰로스 0.5수저
- 대파 적당량
- 고추 적당량
- 깨 적당량

[조리 과정]
1. 먼저 그릇에 밥을 크게 4스푼 담는다.
2. 그 다음, 버섯을 아무 종류로 준비하여 작게 잘라 놓는다.
3. 잘라 놓은 버섯을 밥 위에 올리고, 콩나물을 크게 한 주 올린다.
4. 그릇에 랩을 씌우고, 랩에 구멍을 뚫는다.
5. 전자레인지를 이용하여 3분 동안 돌린다.
6. 양념장을 만들기 위해, 간장 2수저, 고춧가루 1수저, 참기름 1수저, 다진 마늘 0.5수저, 알룰로스 0.5수저를 준비한다.
7. 대파와 고추를 적당량 썰어 양념장에 넣는다.
8. 마지막으로 깨를 적당량 뿌리고, 모든 재료를 잘 섞는다.
9. 전자레인지에서 나온 콩나물 비빔밥에 양념장을 뿌려서 잘 비벼서 맛있게 먹는다.
```

### 5. 프로젝트 구조
```plaintext
cooking-recipe-product/
│
├── src/
│   ├── main.py           # 애플리케이션 진입점
│   ├── input.py          # InputManager 클래스
│   ├── model.py          # ModelManager 클래스
├── requirements.txt      # Python 종속성 파일
├── Dockerfile            # Docker 설정 파일
├── .env.example          # 환경 변수 예시
└── README.md             # 프로젝트 설명 파일
```

    
