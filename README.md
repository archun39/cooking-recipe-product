# Cooking Recipe Product

## 📖 개요
`Cooking Recipe Product`는 요리 영상의 스크립트로부터 **재료**와 **조리 과정**을 추출하는 AI 기반 애플리케이션입니다.  
이 프로젝트는 요리 콘텐츠 제작자나 요리 애호가들에게 더 효율적인 레시피 작성 및 관리 도구를 제공하는 것을 목표로 합니다.

---

## 🎯 주요 기능
- **재료 추출**: 영상 스크립트에서 사용된 요리 재료를 자동으로 식별.
- **조리 과정 추출**: 조리 과정과 관련된 주요 단계들을 텍스트 형태로 자동 생성.
- **높은 정확성**: 자연어 처리 모델을 사용하여 텍스트 분석.
- **간단한 API 제공**: API 호출을 통해 스크립트를 쉽게 분석.

---

## 🚀 설치 및 실행

### 1. 시스템 요구사항
- Python 3.9 이상
- Docker (선택사항)

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
        ```plaintext
        OPENAI_API_KEY=your_openai_api_key
        ```
    - `OPENAI_API_KEY`는 OpenAI API 키를 입력해야 합니다.

4. 실행:
    ```bash
    python app.py
    ```

#### 2.2. Docker로 실행
1. Docker 이미지 빌드:
    ```bash
    docker build -t cooking-recipe-product:1.0 .
    ```

2. 컨테이너 실행:
    ```bash
    docker run -p 8000:8000 cooking-recipe-product:1.0
    ```

---

## 🧑‍💻 사용 방법
### API 호출
1. **재료 및 조리 과정 추출**:
    - API Endpoint: `/extract`
    - Method: `POST`
    - Request Body:
        ```json
        {
            "script": "요리 영상 스크립트 내용"
        }
        ```
    - Response:
        ```json
        {
            "ingredients": ["재료1", "재료2", "재료3"],
            "steps": ["조리 과정 1", "조리 과정 2", "조리 과정 3"]
        }
        ```

### 예제
```bash
curl -X POST http://localhost:8000/extract \
-H "Content-Type: application/json" \
-d '{"script": "양파를 잘게 썰어 팬에 볶습니다. 소금을 추가하고, 물을 부어 끓입니다."}'
