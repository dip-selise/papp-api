FROM python:3.10-alpine
WORKDIR /app

ADD requirments.txt .
RUN pip install -r requirments.txt
COPY ./src /app/src

ENTRYPOINT [ "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8888" ]