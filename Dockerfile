# Python 베이스 이미지 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 환경 구축
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# src 디렉토리의 모든 파일을 컨테이너로 복사
COPY src/ /app/

# scripts 디렉토리 복사
COPY scripts/ /scripts/

# main.py 실행
CMD ["python", "main.py"]
