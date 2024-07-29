FROM python:3.11.9-bookworm

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip "poetry==1.8.2"
RUN poetry config virtualenvs.create false --local

RUN useradd -rms /bin/bash artyombn && chmod 777 /opt /run

WORKDIR /app

COPY --chown=artyombn:artyombn . .

RUN poetry install

RUN chmod +x /app/run_all.sh

USER artyombn

CMD ["bash", "/app/run_all.sh"]
