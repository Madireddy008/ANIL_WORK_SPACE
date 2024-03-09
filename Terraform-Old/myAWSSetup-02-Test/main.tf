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

resource "aws_subnet" "sub2" {
  vpc_id                  = aws_vpc.myvpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = true
  tags = {
    Name = "${var.VPC}-${var.SN}02"
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

resource "aws_route_table_association" "rta2" {
  subnet_id      = aws_subnet.sub2.id
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

resource "aws_instance" "webserver1" {
  ami                    = "${var.AMI}"
  instance_type          = "t2.micro"
  key_name               = "madireddyKeyPair"
  vpc_security_group_ids = [aws_security_group.webSg.id]
  subnet_id              = aws_subnet.sub1.id
  tags = {
    Name = "${var.VPC}-${var.INS}01-Jenkins&Docker"
  }
  
}

resource "aws_instance" "webserver2" {
  ami                    = "${var.AMI}"
  instance_type          = "t2.micro"
  key_name               = "madireddyKeyPair"
  vpc_security_group_ids = [aws_security_group.webSg.id]
  subnet_id              = aws_subnet.sub2.id
  tags = {
    Name = "${var.VPC}-${var.INS}02-Tom&Maven"
  }
}

resource "aws_instance" "webserver3" {
  ami                    = "${var.AMI}"
  instance_type          = "t2.medium"
  key_name               = "madireddyKeyPair"
  vpc_security_group_ids = [aws_security_group.webSg.id]
  subnet_id              = aws_subnet.sub1.id
  tags = {
    Name = "${var.VPC}-${var.INS}03-Kubernetes"
  }
}

resource "aws_instance" "webserver4" {
  ami                    = "${var.AMI}"
  instance_type          = "t2.medium"
  key_name               = "madireddyKeyPair"
  vpc_security_group_ids = [aws_security_group.webSg.id]
  subnet_id              = aws_subnet.sub2.id
  tags = {
    Name = "${var.VPC}-${var.INS}03-KubeNode1"
  }
}

resource "aws_instance" "webserver5" {
  ami                    = "${var.AMI}"
  instance_type          = "t2.medium"
  key_name               = "madireddyKeyPair"
  vpc_security_group_ids = [aws_security_group.webSg.id]
  subnet_id              = aws_subnet.sub2.id
  tags = {
    Name = "${var.VPC}-${var.INS}03-KubeNode2"
  }
}


