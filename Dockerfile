FROM python:3.8.6
WORKDIR /code
COPY requirements.txt
RUN pip install -r requirements.txt
COPY src/ .
CMD [ "python", "./main.py" ]
EXPOSE 8080