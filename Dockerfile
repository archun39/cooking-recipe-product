# 베이스 이미지 설정
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 프로젝트 파일 복사
COPY . /app

# 의존성 설치
RUN pip install -r requirements.txt

# 컨테이너 실행 시 기본 명령
CMD ["python", "src/main.py"]
