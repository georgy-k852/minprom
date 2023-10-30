FROM python:3.10-slim

WORKDIR /opt/bot

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY bot/requirements.txt requirements.txt
RUN  pip install --upgrade pip \
     && pip install -r requirements.txt
COPY bot/. .

RUN ["chmod", "+x", "/opt/bot/run.sh"]

ENTRYPOINT ["sh", "run.sh"]