FROM 3.12.2-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt

COPY . /app
CMD [ "python3", "app.py" ]