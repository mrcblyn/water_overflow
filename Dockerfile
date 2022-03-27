FROM python:3.8-slim
ADD . /code
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python3", "-u", "app.py" ]
