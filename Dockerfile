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

RUN mkdir projects
WORKDIR ./projects

COPY . .

RUN export XDG_RUNTIME_DIR=/run/user/$(id -u)

ENTRYPOINT ["python"]
CMD ["main.py"]
