resource "aws_vpc" "myvpc" {
  cidr_block = var.CIDR
  tags = {
    Name = var.VPC
  }
}

resource "aws_subnet" "sub1" {
  vpc_id                  = aws_vpc.myvpc.id
  cidr_block              = "10.0.0.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true
  tags = {
    Name = "${var.VPC}-${var.SN}01"
  }
}