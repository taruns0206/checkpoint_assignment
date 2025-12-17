import json
import os
import requests
import boto3

S3_BUCKET = os.environ.get("S3_BUCKET", "product-data-bucket-checkpoint-assignment")
OUTPUT_FILE = "filtered_products.json"
CLOUDFRONT_DOMAIN = os.environ.get("CLOUDFRONT_DOMAIN")

def main():
    # 1️⃣ Fetch products from API
    response = requests.get("https://dummyjson.com/products")
    data = response.json()

    # 2️⃣ Filter products with price >= 100
    filtered = [p for p in data.get("products", []) if p.get("price", 0) >= 100]

    # 3️⃣ Save filtered products to JSON
    with open(OUTPUT_FILE, "w") as f:
        json.dump(filtered, f, indent=2)

    # 4️⃣ Upload to S3 using environment credentials
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        region_name=os.environ.get("AWS_DEFAULT_REGION")
    )
    s3.upload_file(OUTPUT_FILE, S3_BUCKET, OUTPUT_FILE)
    print(f"Uploaded {OUTPUT_FILE} to S3 bucket {S3_BUCKET}")

    # 5️⃣ Download via CloudFront to verify
    if not CLOUDFRONT_DOMAIN:
        print("CLOUDFRONT_DOMAIN environment variable not set. Skipping CloudFront check.")
        return

    cloudfront_url = f"https://{CLOUDFRONT_DOMAIN}/{OUTPUT_FILE}"
    try:
        cf_response = requests.get(cloudfront_url)
        cf_response.raise_for_status()
        cf_response.json()  # Validate JSON
        print("Downloaded file via CloudFront is valid JSON")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch file from CloudFront: {e}")
    except ValueError:
        print("Downloaded file is NOT valid JSON")

if __name__ == "__main__":
    main()
