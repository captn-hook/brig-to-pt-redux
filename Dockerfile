FROM python:3.10
EXPOSE 6743
COPY . .

RUN apt-get update && apt-get install -y \
    build-essential xorg git subversion cmake libx11-dev libxxf86vm-dev libxcursor-dev libxi-dev libxrandr-dev libxinerama-dev libegl-dev libxkbcommon-dev 
    #libwayland-dev wayland-protocols libdbus-1-dev linux-libc-dev

RUN pip install -r ./requirements.txt
RUN chmod +x ./run.sh
CMD ["gunicorn"  , "-b", "0.0.0.0:6743", "wsgi:app"]