resource "aws_vpc" "myvpc" {
  cidr_block = var.CIDR
  tags = {
    Name = "${var.VPC}"
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

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.myvpc.id
  tags = {
    Name = "${var.VPC}-${var.IGW}01"
  }
}

resource "aws_route_table" "RT" {
  vpc_id = aws_vpc.myvpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "${var.VPC}-${var.RTB}01-public"
  }
}

resource "aws_route_table_association" "rta1" {
  subnet_id      = aws_subnet.sub1.id
  route_table_id = aws_route_table.RT.id
}


resource "aws_security_group" "webSg" {
  vpc_id = aws_vpc.myvpc.id

  ingress {
    description = "Allow All"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["122.171.23.142/32"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.VPC}-${var.SG}"
  }
}

resource "aws_instance" "server1" {
  ami                    = "${var.AMI}"
  instance_type          = "t2.medium"
  key_name               = "madireddyKeyPair"
  vpc_security_group_ids = [aws_security_group.webSg.id]
  subnet_id              = aws_subnet.sub1.id
  #user_data             = base64encode(file("KubemasterInst.sh"))
  user_data              = templatefile("./KubeMasasNorm.sh", {})
  tags = {
    Name = "${var.VPC}-${var.INS}01-Kubemaster"
  }
  
}
