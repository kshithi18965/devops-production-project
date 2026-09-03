# Multi-stage Dockerfile (Python example)
# Stage 1: build wheels
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip wheel --no-deps --wheel-dir /wheels -r requirements.txt

# Stage 2: runtime image
FROM python:3.11-slim
WORKDIR /app
RUN useradd --create-home appuser
COPY --from=builder /wheels /wheels
COPY requirements.txt ./
RUN pip install --no-index --find-links /wheels -r requirements.txt && rm -rf /wheels
COPY . /app
ENV PYTHONUNBUFFERED=1
USER appuser
CMD ["python", "main.py"]
