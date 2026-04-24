# Archive Python code into a zip file
data "archive_file" "zip_the_python_code" {
  type        = "zip"
  source_dir  = "${path.module}/lambda/"
  output_path = "${path.module}/lambda/lambda_function.zip"
}

# CloudWatch Log Group for Lambda (controls retention; prevents unbounded log growth)
resource "aws_cloudwatch_log_group" "lambda" {
  name              = "/aws/lambda/terraform_lambda_func"
  retention_in_days = 30

  tags = {
    Name = "Cloud Resume Challenge"
  }
}

# Lambda Function
resource "aws_lambda_function" "terraform_lambda_func" {
  filename      = "${path.module}/lambda/lambda_function.zip"
  function_name = "terraform_lambda_func"
  role          = aws_iam_role.lambda_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.12"
  depends_on    = [aws_iam_role_policy_attachment.attach_iam_policy_to_iam_role, aws_cloudwatch_log_group.lambda]
  environment {
    variables = {
      databaseName = "visitor_count_ddb"
    }
  }

  tags = {
    Name = "Cloud Resume Challenge"
  }
}