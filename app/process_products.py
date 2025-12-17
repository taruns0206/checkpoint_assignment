import json
import requests
import boto3

S3_BUCKET = "product-data-bucket"
OUTPUT_FILE = "filtered_products.json"

def main():
    response = requests.get("https://dummyjson.com/products")
    data = response.json()

    filtered = [
        p for p in data["products"]
        if p.get("price", 0) >= 100
    ]

    with open(OUTPUT_FILE, "w") as f:
        json.dump(filtered, f, indent=2)

    s3 = boto3.client("s3")
    s3.upload_file(OUTPUT_FILE, S3_BUCKET, OUTPUT_FILE)

    print("Uploaded filtered JSON to S3")

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
