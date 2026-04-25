resource "aws_cloudfront_distribution" "portfolio" {
  enabled             = true
  is_ipv6_enabled     = true
  default_root_object = "index.html"
  price_class         = "PriceClass_All"
  http_version        = "http2"
  aliases             = ["estebanmoreno.link"]
  comment             = ""

  origin {
    origin_id                = "esteban-cloud-resume-challenge.s3.us-east-1.amazonaws.com"
    domain_name              = "esteban-cloud-resume-challenge.s3.us-east-1.amazonaws.com"
    origin_access_control_id = "E537L141OOG0Q"

  }

  default_cache_behavior {
    target_origin_id           = "esteban-cloud-resume-challenge.s3.us-east-1.amazonaws.com"
    viewer_protocol_policy     = "redirect-to-https"
    allowed_methods            = ["GET", "HEAD"]
    cached_methods             = ["GET", "HEAD"]
    compress                   = true
    cache_policy_id            = "658327ea-f89d-4fab-a63d-7e88639e58f6" # AWS managed: CachingOptimized
    response_headers_policy_id = aws_cloudfront_response_headers_policy.security_headers.id
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    acm_certificate_arn      = "arn:aws:acm:us-east-1:974262444728:certificate/d4d06328-4ebd-40e3-a493-ed50a8083b74"
    ssl_support_method       = "sni-only"
    minimum_protocol_version = "TLSv1.2_2021"
  }
}
