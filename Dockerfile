FROM python:3.10.8
LABEL maintainer="ishanshrestha"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1 # tells python to not buffer the output to the console
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000

