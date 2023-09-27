# brig-to-pt-redux

docker build --tag=brigo .

docker run -p 6743:6743 brigo

gunicorn --bind 0.0.0.0:6743 wsgi:app