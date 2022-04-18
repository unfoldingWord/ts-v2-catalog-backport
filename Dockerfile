FROM python:3

COPY . /code
WORKDIR /code

# Upgrade pip3 and install the requirements
RUN pip3 install --requirement requirements.txt

CMD [ "python3", "main.py" ]
