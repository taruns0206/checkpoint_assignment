resource "aws_cloudfront_distribution" "this" {
  enabled = true

  origin {
    domain_name = var.bucket_domain
    origin_id   = "s3-origin"
    origin_access_control_id = aws_cloudfront_origin_access_control.oac.id
  }

  default_cache_behavior {
    allowed_methods        = ["GET", "HEAD"]
    cached_methods         = ["GET", "HEAD"]
    target_origin_id       = "s3-origin"
    viewer_protocol_policy = "redirect-to-https"
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }

  # REQUIRED block to fix the error
  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  tags = var.tags
}