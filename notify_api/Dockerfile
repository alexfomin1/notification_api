FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
RUN python manage.py makemigrations
RUN python manage.py migrate