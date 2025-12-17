terraform {
  source = "../../modules/cloudfront"
}

dependency "s3" {
  config_path = "../s3"
}

inputs = {
  bucket_domain = dependency.s3.outputs.bucket_domain
  tags = {
    Name      = "ProductCloudFront"
    Owner     = "Tarun Soni"
    Terraform = "True"
  }
}
