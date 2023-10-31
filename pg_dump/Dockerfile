FROM python:3.10-slim

WORKDIR /opt/pg_dump

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY pg_dump/requirements.txt requirements.txt
RUN  pip install --upgrade pip \
     && pip install -r requirements.txt
COPY pg_dump/. .

RUN ["chmod", "+x", "/opt/pg_dump/run.sh"]

ENTRYPOINT ["sh", "run.sh"]