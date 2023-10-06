from google.cloud import storage
from google.oauth2 import service_account
#import secrets/iam.json
import sys
import os
import glob

credentials = service_account.Credentials.from_service_account_file('/secrets/key.json')

# scoped_credentials = credentials.with_scopes(
#     ['https://www.googleapis.com/auth/cloud-platform'])

storage_client = storage.Client(project='brig-b2ca3', credentials=credentials)

#upload blob

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to upload is aborted if the object's
    # generation number does not match your precondition. For a destination
    # object that does not yet exist, set the if_generation_match precondition to 0.
    # If the destination object already exists in your bucket, set instead a
    # generation-match precondition using its generation number.
    generation_match_precondition = 0

    blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

def upload_local_directory_to_gcs(local_path, bucket, gcs_path):
    print("uploading", local_path, bucket, gcs_path)
    assert os.path.isdir(local_path)
    for local_file in glob.glob(local_path + '/**'):
        if not os.path.isfile(local_file):
           upload_local_directory_to_gcs(local_file, bucket, gcs_path + "/" + os.path.basename(local_file))
        else:
           remote_path = os.path.join(gcs_path, local_file[1 + len(local_path):])
           blob = bucket.blob(remote_path)
           blob.upload_from_filename(local_file)


#upload_blob('brig-b2ca3.appspot.com', sys.argv[1], 'Images/' + sys.argv[1])
upload_local_directory_to_gcs(sys.argv[1], storage_client.bucket('brig-b2ca3.appspot.com'), 'Images/' + sys.argv[1])