# Project_Plan

# Step-1
# API to GCS Bucket (Folder: Kaggle_dataset)

## 📦 Download Kaggle Dataset and Upload to Google Cloud Storage (GCS)

This script demonstrates how to authenticate with the Kaggle API, download a dataset, and upload it to a GCS bucket for further processing.

### 📚 Dataset Used

[Kaggle Dataset: Ecommerce Data Analysis](https://www.kaggle.com/datasets/mmohaiminulislam/ecommerce-data-analysis)

### 🧰 Prerequisites

1. **Python 3.8+**
2. Kaggle API installed:
   ```bash
   pip install kaggle


# Step-2
# GCS to BigQuery Cloud Function (Floder: GCS_to_BigQuery)

This project deploys a Cloud Function that is triggered when a CSV file is uploaded to a GCS bucket. It loads the data into a BigQuery table.

## 🧱 Prerequisites
- Python 3.10+
- GCP project with billing enabled
- IAM permissions: GCS Admin, BigQuery Admin, Cloud Functions Developer

## ⚙️ Services Used
- Cloud Functions (Gen 2)
- Google Cloud Storage
- BigQuery

## 🚀 Setup Instructions

### 1. Enable APIs
```bash
gcloud services enable cloudfunctions.googleapis.com storage.googleapis.com bigquery.googleapis.com eventarc.googleapis.com run.googleapis.com
```

### 2. Create GCS Bucket
```bash
gsutil mb -l asia-south1 gs://your-bucket-name
```

### 3. Create BigQuery Dataset
```bash
bq mk --location=asia-south1 your_dataset
```

### 4. Deploy Cloud Run Function
```bash
gcloud functions deploy gcs_to_bq \
  --gen2 \
  --runtime=python310 \
  --region=asia-south1 \
  --source=. \
  --entry-point=gcs_to_bq \
  --trigger-event-filters=\"type=google.cloud.storage.object.v1.finalized\" \
  --trigger-event-filters=\"bucket=your-bucket-name\" \
  --set-env-vars=BQ_DATASET=your_dataset \
  --memory=512MB \
  --timeout=60s
```

### 5. Upload a CSV to Trigger
```bash
gsutil cp sample_data.csv gs://your-bucket-name/
```
