FROM nvidia/cuda:12.3.2-cudnn9-runtime-ubuntu22.04

RUN apt-get update -y && apt-get install -y \
    python3 python3-pip

WORKDIR /app

COPY requirements_nogpu.txt /app
RUN pip install -r requirements_nogpu.txt --no-cache-dir

COPY . .

RUN python3 manage.py collectstatic --noinput

EXPOSE 8000