FROM python:latest

COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "main.py" ]