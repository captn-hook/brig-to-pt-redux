FROM python:3.10
EXPOSE 8000
COPY . .
RUN pip install -r ./requirements.txt
CMD ["gunicorn", "wsgi:app", "--bind", "localhost:8000"]