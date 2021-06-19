FROM python:3.7-alpine

RUN adduser -D covidviewer

WORKDIR /home/covidviewer

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY covidviewer app
COPY main.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP main.py 

RUN chown -R covidviewer:covidviewer ./
USER covidviewer

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]