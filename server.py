#server on flask that takes a http json post and returns a OK response when done
#                                               ^                                
#                                               |                                
#                                               |                                
#                        request: {"csv": "csv file",                            
#                                  "model": "model link",
#                                  "bucket": "bucket name",
#                                  "folder": "folder name"}

from flask import Flask, request, jsonify

import json
import os
import codecs

from google.cloud import storage
from google.oauth2 import service_account
#import secrets/iam.json

credentials = service_account.Credentials.from_service_account_file('/secrets/key.json')

# scoped_credentials = credentials.with_scopes(
#     ['https://www.googleapis.com/auth/cloud-platform'])

storage_client = storage.Client(project='brig-b2ca3', credentials=credentials)

print("init1", __name__)
app = Flask(__name__)

print("init2")
#import projectID from secret

@app.route('/', methods=['GET'])
def index():
    #if there is a ./model folder get *.png from it and return tiled view
    def imageTile(url):
        return "<img src=\"" + url + "\" width=\"100\" height=\"100\">"
    
    #check if there is a model folder
    if os.path.isdir("model"):
        #get all the pngs
        pngs = os.listdir("model")
        #return the tiled view
        return "<html><body>" + "".join(list(map(imageTile, pngs))) + "</body></html>"
    else:
        return "<html><body>no model</body></html>"

@app.route('/', methods=['POST'])
def get():
    #check if request is json
    if request.is_json:
        print("request is json")
        #get json

        print(request.get_json())
        
        print(request)
        #req = request.get_json()
        req = request.data.decode()
        print(req)

        req =json.loads(req)
        
        print(req)

        csv = req['csv']
        model = req['model']
        bucket = req['bucket']

        print("csv: " + csv)
        print("model: " + model)
        print("bucket: " + bucket)
        
        #check if model folder exists
        if os.path.isdir("model"):
            os.system("rm -rf model")

        #create folder and download model
        os.system("mkdir model")

        download_blob(bucket, model, "model/model.glb")

        #write csv file in same folder
        with open("model/model.csv", "w") as file:
            file.write(csv)

        #run the shell script
        os.system("sh run.sh model")

        print("done?")

        #upload the model/output to bucket/model/output
        #   bucket = storage_client.get_bucket(bucket_name)
        #  blob = bucket.blob(folder_name + "/output")
        #upload folder
        # blob.upload_from_filename("model/output")

        #force rm the directory
        
        #return the response
        return jsonify({"response": "OK"}), 200

    else:
        print("request is not json")
        return jsonify({"error": "request is not json"}), 400

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # source_blob_name = "storage-object-name"

    # The path to which the file should be downloaded
    # destination_file_name = "local/path/to/file"

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )