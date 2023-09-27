FROM python:3.10
EXPOSE 6743
COPY . .
RUN pip install -r ./requirements.txt
CMD ["gunicorn", "wsgi:app", "--bind", "localhost:6743"]