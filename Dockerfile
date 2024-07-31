FROM python:3.11.9-bookworm

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip "poetry==1.8.2"

RUN poetry config virtualenvs.create false --local

RUN useradd -rms /bin/bash artyombn && chmod 777 /opt /run

RUN poetry install
RUN pip list

COPY --chown=artyombn:artyombn . /app

RUN chmod +x /app/run_all.sh

USER artyombn

RUN python manage.py collectstatic --noinput

CMD ["bash", "/app/run_all.sh"]
