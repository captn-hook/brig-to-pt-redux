FROM python:3.10
EXPOSE 6743
COPY . .
RUN pip install -r ./requirements.txt
#CMD ["gunicorn", "wsgi:server", "--bind", "localhost:6743"]
RUN chmod +x ./run.sh
CMD ["gunicorn"  , "-b", "0.0.0.0:6743", "wsgi:app"]