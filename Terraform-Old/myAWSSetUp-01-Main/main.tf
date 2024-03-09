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

resource "aws_subnet" "sub3" {
  vpc_id                  = aws_vpc.myvpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1c"
  map_public_ip_on_launch = true
  tags = {
    Name = "${var.VPC}-${var.SN}03"
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

resource "aws_route_table_association" "rta3" {
  subnet_id      = aws_subnet.sub3.id
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
  user_data              = base64encode(file("JenkinsInstall.sh"))
  tags = {
    Name = "${var.VPC}-${var.INS}01-JenkinsMaster"
  } 
}

resource "aws_instance" "server2" {
  ami                    = "${var.AMI}"
  instance_type          = "t2.medium"
  key_name               = "madireddyKeyPair"
  vpc_security_group_ids = [aws_security_group.webSg.id]
  subnet_id              = aws_subnet.sub2.id
  user_data              = base64encode(file("JenDokNode1.sh"))
  tags = {
    Name = "${var.VPC}-${var.INS}02-JenDokNode1"
  }
}

resource "aws_instance" "server3" {
  ami                    = "${var.AMI}"
  instance_type          = "t2.medium"
  key_name               = "madireddyKeyPair"
  vpc_security_group_ids = [aws_security_group.webSg.id]
  subnet_id              = aws_subnet.sub3.id
  user_data              = base64encode(file("JenDokNode2.sh"))
  tags = {
    Name = "${var.VPC}-${var.INS}03-JenDokNode2"
  }
}

resource "aws_instance" "server4" {
  ami                    = "${var.AMI}"
  instance_type          = "t2.medium"
  key_name               = "madireddyKeyPair"
  vpc_security_group_ids = [aws_security_group.webSg.id]
  subnet_id              = aws_subnet.sub1.id
  #user_data             = base64encode(file("KubemasterInst.sh"))
  user_data              = templatefile("./KubeMasasNorm.sh", {})
  tags = {
    Name = "${var.VPC}-${var.INS}04-KubeMaster"
  }
}

resource "aws_instance" "server5" {
  ami                    = "${var.AMI}"
  instance_type          = "t2.medium"
  key_name               = "madireddyKeyPair"
  vpc_security_group_ids = [aws_security_group.webSg.id]
  subnet_id              = aws_subnet.sub2.id
  user_data              = base64encode(file("KubeNodeInst.sh"))
  tags = {
    Name = "${var.VPC}-${var.INS}05-KubeNode01"
  }
}

resource "aws_instance" "server6" {
  ami                    = "${var.AMI}"
  instance_type          = "t2.medium"
  key_name               = "madireddyKeyPair"
  vpc_security_group_ids = [aws_security_group.webSg.id]
  subnet_id              = aws_subnet.sub3.id
  user_data              = base64encode(file("KubeNode1Inst.sh"))
  tags = {
    Name = "${var.VPC}-${var.INS}06-KubeNode02"
  }
}

resource "aws_instance" "server7" {
  ami                    = "${var.AMI}"
  instance_type          = "t2.medium"
  key_name               = "madireddyKeyPair"
  vpc_security_group_ids = [aws_security_group.webSg.id]
  subnet_id              = aws_subnet.sub1.id
  user_data              = base64encode(file("TomcatMavenInst.sh"))
  tags = {
    Name = "${var.VPC}-${var.INS}07-Tomcat01"
  }
}


