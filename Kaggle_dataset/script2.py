import kaggle
import os
from google.cloud import storage

# Step 1: Authenticate with Kaggle
kaggle.api.authenticate()

# Step 2: Download dataset to local temp directory
kaggle.api.dataset_download_files(
    'mmohaiminulislam/ecommerce-data-analysis',
    path='tmp_download',
    unzip=True
)

# Step 3: Upload files to GCS bucket
BUCKET_NAME = 'your-gcs-bucket-name'
destination_folder = 'kaggle-ecommerce-data/'

client = storage.Client()
bucket = client.get_bucket(BUCKET_NAME)

for file_name in os.listdir('tmp_download'):
    local_path = os.path.join('tmp_download', file_name)
    blob = bucket.blob(destination_folder + file_name)
    blob.upload_from_filename(local_path)
    print(f"Uploaded {file_name} to gs://{BUCKET_NAME}/{destination_folder}")
