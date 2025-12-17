remote_state {
  backend = "s3"
  config = {
    bucket         = "tf-state-bucket"
    key            = "checkpoint-assignment/terraform.tfstate"
    region         = "ap-southeast-2"
    encrypt        = true
  }
}
