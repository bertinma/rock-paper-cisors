# FROM python:3.9 
# WORKDIR /app
# COPY requirements.txt requirements.txt

# RUN apt-get update -y && apt-get upgrade -y && \
#     apt-get install xvfb -y

# RUN pip install -r requirements.txt
# COPY . .
# CMD ["python", "main.py"]

FROM fadawar/docker-pyqt5:latest

WORKDIR /app
COPY . . 

CMD ["python", "main.py"]
