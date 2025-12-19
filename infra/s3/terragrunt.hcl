terraform {
  backend "s3" {}
}

terraform {
  source = "../../modules/s3"
}

inputs = {
  bucket_name = "product-data-bucket-checkpoint-assignment"
  role_arn    = "arn:aws:iam::478822682668:user/TARUN-SONI"
  tags = {
    Name      = "ProductCloudFront"
    Owner     = "Tarun Soni"
    Terraform = "True"
  }
}