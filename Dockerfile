FROM python:3.9.12-slim-buster

RUN apt-get update && apt-get install -y \
    wget \
    xz-utils \
    pandoc \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz -O /tmp/ffmpeg.tar.xz \
    && tar -xf /tmp/ffmpeg.tar.xz -C /tmp

RUN mv /tmp/ffmpeg-master-latest-linux64-gpl/bin/* /usr/local/bin/
RUN rm -f /tmp/ffmpeg.tar.xz
RUN ffmpeg -version

WORKDIR /AudioBridge/bin

COPY ./requirements.txt /AudioBridge/bin/requirements.txt
RUN pip install --upgrade -r requirements.txt

COPY . /AudioBridge/bin

ENTRYPOINT ["python3", "-Bu", "-m", "audiobridge"]
