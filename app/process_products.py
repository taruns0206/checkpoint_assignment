import json
import requests
import boto3
import os

S3_BUCKET = "product-data-bucket-checkpoint-assignment"
OUTPUT_FILE = "filtered_products.json"

def main():
    # Download JSON from dummy API
    response = requests.get("https://dummyjson.com/products")
    data = response.json()

    # Filter products with price >= 100
    filtered = [p for p in data.get("products", []) if p.get("price", 0) >= 100]

    # Save filtered JSON locally
    with open(OUTPUT_FILE, "w") as f:
        json.dump(filtered, f, indent=2)

    # Create S3 client using environment variables for credentials
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        region_name=os.environ.get("AWS_DEFAULT_REGION")
    )

    # Upload file to S3
    s3.upload_file(OUTPUT_FILE, S3_BUCKET, OUTPUT_FILE)
    print(f"Uploaded {OUTPUT_FILE} to S3 bucket {S3_BUCKET}")

    # Download via CloudFront
    cloudfront_url = f"https://<CLOUDFRONT_DOMAIN>/{OUTPUT_FILE}"
    cf_response = requests.get(cloudfront_url)

    try:
        cf_response.json()
        print("Downloaded file is valid JSON")
    except ValueError:
        print("Downloaded file is NOT valid JSON")

if __name__ == "__main__":
    main()