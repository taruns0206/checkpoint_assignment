terraform {
  source = "../../modules/s3"
}

inputs = {
  bucket_name = "product-data-bucket-checkpoint-assignment"
  tags = {
    Name      = "ProductCloudFront"
    Owner     = "Tarun Soni"
    Terraform = "True"
  }
}