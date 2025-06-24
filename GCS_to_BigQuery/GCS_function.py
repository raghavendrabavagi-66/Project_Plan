from google.cloud import bigquery
import os

def gcs_to_bq(event, context):
    bucket_name = event['bucket']
    file_name = event['name']

    if not file_name.endswith(".csv"):
        print(f"Skipped non-csv file: {file_name}")
        return

    uri = f"gs://{bucket_name}/{file_name}"

    dataset_id = os.environ.get("BQ_DATASET")
    if not dataset_id:
        raise Exception("BQ_DATASET env var not set.")

    table_name = file_name.replace(".csv", "").replace("/", "_")
    client = bigquery.Client()
    table_id = f"{client.project}.{dataset_id}.{table_name}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
    )

    load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
    load_job.result()

    print(f"Loaded {file_name} into BigQuery table {table_id}")
