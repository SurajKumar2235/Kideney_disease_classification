FROM 3.12.2-slim-bookworm

WORKDIR /app

COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt

COPY . .
CMD [ "python3", "main.py" ]