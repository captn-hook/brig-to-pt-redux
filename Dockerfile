FROM python:3.10
EXPOSE 6743
COPY . .

RUN apt-get update && apt-get install -y flatpak
RUN flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo 
RUN flatpak install flathub org.blender.Blender -y
RUN pip install -r ./requirements.txt
RUN chmod +x ./run.sh
CMD ["gunicorn"  , "-b", "0.0.0.0:6743", "wsgi:app"]