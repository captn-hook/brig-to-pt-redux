# brig-to-pt-redux

docker build --tag=brigo .

docker run -p 6743:6743 brigo

gunicorn --bind 0.0.0.0:6743 wsgi:app

curl -X POST http://127.0.0.1:5000/ \
   -H 'Content-Type: application/json' \
   --json @sample.json

curl -X POST http://127.0.0.1:5000/ \
   -H 'Content-Type: application/json' \
   -d '{"csv": "csvtest", "model": "modeltest", "bucket": "buckettest", "folder": "foldertest"}'

    
curl -X POST -H "Content-Type: application/json" -d '{"csv": $(cat ./daikin.csv), "model": "https://firebasestorage.googleapis.com/v0/b/brig-b2ca3.appspot.com/o/Sites%2FArroyo%2FArroyo.glb", "bucket": "brig-b2ca3.appspot.com", "folder": "Sites/Arroyo"}' http://127.0.0.1:5000/