FROM python:3.11
FROM python:3.10
ENV PYTHONUNBUFFERED=1
RUN pip install poetry
WORKDIR /app/
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false && poetry install
COPY . /app/
