terraform {
  source = "../../modules/s3"
}

inputs = {
  bucket_name = "product-data-bucket"
  tags = {
    Name      = "ProductCloudFront"
    Owner     = "Tarun Soni"
    Terraform = "True"
  }
}