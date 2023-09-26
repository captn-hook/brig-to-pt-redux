# brig-to-pt-redux

docker build --tag=brigo .

docker run brigo

gunicorn --bind 0.0.0.0:8000 wsgi:app