# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11.9
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/app" \
    --uid "${UID}" \
    appuser

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install -r requirements.txt

# Install cron
RUN apt-get update && apt-get -y install cron
RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential

# Copy crontab file and set permissions
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN touch /var/log/cron.log

# Copy the source code into the container.
COPY . .
RUN chown -R appuser:appuser /app/notebooks
# Change ownership of the /app directory to the non-privileged user
RUN chown -R appuser:appuser /app

# Expose the ports that the applications will run on
EXPOSE 8008 8888

# Switch to the non-privileged user to run the application
USER appuser

# Set the default command to run both uvicorn and jupyter notebook
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8008 & jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --no-browser"]
