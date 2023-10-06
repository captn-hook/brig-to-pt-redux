FROM python:3.10
EXPOSE 6743
COPY . .

RUN apt-get update && apt-get install -y xorg
RUN pip install -r ./requirements.txt
RUN chmod +x ./run.sh
CMD ["gunicorn"  , "-b", "0.0.0.0:6743", "wsgi:app"]