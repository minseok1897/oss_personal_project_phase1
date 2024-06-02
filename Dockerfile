FROM python:3.9

RUN apt-get update && apt-get install -y \
    python3-pip \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pygame


ENTRYPOINT ["python"]
CMD ["main.py"]
