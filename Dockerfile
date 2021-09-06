FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY . /code/
RUN pip install -r requirements.txt

EXPOSE 8000
CMD gunicorn ecom.wsgi:application --bind 0.0.0.0:8000
