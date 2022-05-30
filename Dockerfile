FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /lab7
WORKDIR /lab7
COPY requirements.txt /lab7/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /lab7/