FROM python:3.9

ARG USERNAME
ARG PASSWORD
ARG DB_NAME
ARG TABLE_NAME
ARG URL
ARG PORT

COPY main.py requirements.txt app/
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE $PORT
CMD python /app/main.py