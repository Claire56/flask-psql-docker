FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY . /code
WORKDIR /code
RUN pip3 install -r requirements.txt 
# RUN python3 model.py
# RUN python3 seed.py
# CMD python3 app.py
CMD gunicorn --bind 0.0.0.0:5000 -w 3 app:app
