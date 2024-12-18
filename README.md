# Deploying-Cloud-Infra
Welcome to the Cloud Microservices Deployment project! This project showcases a Python Flask-based microservice deployed across leading cloud platform: AWS ECS Fargate. By leveraging containerization with Docker and automated CI/CD pipelines, this project demonstrates a secure, highly available, and scalable cloud architecture.

The goal of this project is to highlight the use of cloud-native tools and Well-Architected Framework principles (Operational Excellence, Security, Reliability, Performance Efficiency, and Cost Optimization) in deploying microservices.

This project uses Docker containerization and CI/CD pipelines to streamline deployment on **AWS**.
# Cloud Microservices Deployment - Flask Application 🚀

This repository contains a **Python Flask microservice** deployed across **AWS ECS Fargate**. The infrastructure for AWS is provisioned using **Terraform**, ensuring repeatable, reliable, and automated deployments.

---

## **Introduction**

This project demonstrates the deployment of a simple Flask-based microservice that returns:
"Hello from Dhruv ECS Container."


By combining **Docker**, **CI/CD pipelines**, and **Terraform**, this project highlights multi-cloud deployment following **Well-Architected Framework** principles:
- **Operational Excellence**
- **Security**
- **Reliability**
- **Performance Efficiency**
- **Cost Optimization**

---

## **Key Features**
1. **Multi-Cloud Deployment**: AWS, GCP, and Azure.
2. **Infrastructure as Code (IaC)**: AWS infrastructure deployed using **Terraform**.
3. **Containerization**: Dockerized Flask application.
4. **CI/CD Pipelines**: AWS CodePipeline.
5. **High Availability**: Load Balancers, Auto-Scaling, and private subnets.
6. **Security**: VPC, security groups, container security scanning.

---

## **Technologies Used**
- **Programming**: Python (Flask)
- **Containerization**: Docker
- **IaC**: Terraform
- **CI/CD**: AWS CodePipeline
- **Orchestration**: AWS ECS Fargate
- **Networking**: ALB, VPC, Subnets, Security Groups
- **Container Registry**: Amazon ECR

---

## **Prerequisites**
1. **Install Required Tools**:
   - **Terraform**: [Install Guide](https://learn.hashicorp.com/tutorials/terraform/install-cli)
   - AWS CLI
   - Docker
   - Python 3.x

2. **AWS Configuration**:
   - Set up IAM credentials and configure AWS CLI:
     ```bash
     aws configure
     ```
---

## **Setup Instructions**

### **1. Dockerize the Flask Application**
```bash
# Clone the Repository
git clone https://github.com/yourusername/Cloud-Microservices-Deployment.git
cd Cloud-Microservices-Deployment

# Build the Docker Image
docker build -t flask-app .

# Run Locally
docker run -p 5000:5000 flask-app

# Verify
curl http://localhost:5000
```

### **2. AWS Deployment Using Terraform**
#### Step 2.1: Initialize Terraform
```bash
terraform init
```

#### Step 2.2: Review Deployment Plan
#### Preview Terraform Plan
```bash
terraform plan
```

#### Step 2.3: Apply Terraform Configuration
#### Apply Terraform Changes
```bash
terraform apply -auto-approve
```

#### Step 2.4: Push Docker Image to Amazon ECR
#### Authenticate Docker to ECR
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com
```

### Build, Tag, and Push Docker Image
```bash
docker build -t flask-app .
docker tag flask-app:latest <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/flask-app:latest
docker push <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/flask-app:latest
```

#### Step 2.5: Deploy ECS Fargate Service
Update ECS Task Definition to pull the image from ECR.
Ensure the ECS Service is running in your private subnet.

#### Step 2.6: Verify the Application
##### Retrieve the ALB DNS Name
```bash
aws elbv2 describe-load-balancers --query 'LoadBalancers[*].DNSName' --output text
# Verify the Application via ALB DNS
curl http://<alb-dns-name>
```

### **3. Clean Up AWS Resources**
```bash
terraform destroy
```


