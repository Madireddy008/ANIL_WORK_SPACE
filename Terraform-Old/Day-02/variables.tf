variable "CIDR" {
  description = "cidr value"
  default = "10.0.0.0/16"
}

variable "VPC" {
  description = "vpc name"
  default = "techopsVPC"
}

variable "SN" {
  description = "Subnet value"
  default = "sn"
}

variable "IGW" {
  description = "Internet Gate way Value"
  default = "igw"
}

variable "RTB" {
  description = "Routetable Name"
  default = "rtb"
}

variable "SG" {
  description = "Security group Name"
  default = "sg"
}

variable "INS" {
  description = "Instance Name"
  default = "ins"
}

variable "ALB" {
  description = "Application Load Balancer"
  default = "alb"
}

variable "NLB" {
  description = "Network Load Balancer"
  default = "nlb"
}

variable "TG" {
  description = "Target Group"
  default = "tg"
}

variable "AMI" {
  description = "Amazon Machine Image Name"
  default = "ami-0fc5d935ebf8bc3bc"
}