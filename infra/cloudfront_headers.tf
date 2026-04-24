# CloudFront Response Headers Policy
# Adds security headers (CSP, HSTS, COOP, X-Frame-Options) to all CloudFront responses.
#
# After terraform apply, associate this policy with the CloudFront distribution's
# default cache behaviour:
#   AWS Console → CloudFront → Distribution → Behaviours → Edit →
#   Response headers policy → select "portfolio-security-headers"
# OR import the distribution into Terraform and reference this policy's id.

resource "aws_cloudfront_response_headers_policy" "security_headers" {
  name    = "portfolio-security-headers"
  comment = "Security headers for estebanmoreno.link"

  security_headers_config {
    # Prevents clickjacking by blocking the page from being framed
    frame_options {
      frame_option = "DENY"
      override     = true
    }

    # Prevents MIME-type sniffing
    content_type_options {
      override = true
    }

    # Forces HTTPS for 1 year; includes subdomains
    strict_transport_security {
      access_control_max_age_sec = 31536000
      include_subdomains         = true
      preload                    = true
      override                   = true
    }

    # Restricts referrer information sent to third parties
    referrer_policy {
      referrer_policy = "strict-origin-when-cross-origin"
      override        = true
    }

    # Cross-Origin-Opener-Policy: isolates the browsing context
    content_security_policy {
      content_security_policy = join("; ", [
        "default-src 'self'",
        "script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com",
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
        "font-src 'self' https://fonts.gstatic.com",
        "img-src 'self' data: https:",
        "connect-src 'self' https://qfky693v2f.execute-api.eu-west-2.amazonaws.com https://gql.hashnode.com https://formspree.io https://www.google-analytics.com",
        "frame-ancestors 'none'",
        "base-uri 'self'",
        "form-action 'self' https://formspree.io"
      ])
      override = true
    }
  }

}

output "security_headers_policy_id" {
  description = "Associate this policy ID with the CloudFront distribution's default cache behaviour."
  value       = aws_cloudfront_response_headers_policy.security_headers.id
}
