<p align="center">
  <img src="architecture/banner.png" alt="Home Energy Monitor Banner" width="100%">
</p>

<h1 align="center">🏡 Home Energy Monitor</h1>

<p align="center">
  <b>A serverless IoT solution built on AWS that collects, processes, stores, and monitors home energy consumption in real time.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/Architecture-Serverless-success">
  <img src="https://img.shields.io/badge/IoT-AWS%20IoT%20Core-brightgreen?logo=amazonaws">
  <img src="https://img.shields.io/badge/Database-DynamoDB-4053D6?logo=amazondynamodb&logoColor=white">
  <img src="https://img.shields.io/badge/Hosting-Amazon%20S3-569A31?logo=amazons3&logoColor=white">
  <img src="https://img.shields.io/badge/Project-Completed-brightgreen">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey">
</p>

<p align="center">
  <a href="#-project-overview">Overview</a> •
  <a href="#️-aws-architecture">Architecture</a> •
  <a href="#-aws-services-used">Services</a> •
  <a href="#-features">Features</a> •
  <a href="#-project-screenshots">Screenshots</a> •
  <a href="#️-how-to-deploy">Deploy</a> •
  <a href="#-skills-demonstrated">Skills</a>
</p>

---

## 📖 Project Overview

The **Home Energy Monitor** is a serverless AWS project designed to simulate how smart home devices monitor electricity usage in real time.

Energy readings are sent through **AWS IoT Core**, processed by **AWS Lambda**, stored in **Amazon DynamoDB**, monitored using **Amazon CloudWatch**, and users receive real-time alerts through **Amazon SNS** whenever predefined consumption thresholds are exceeded.

This project demonstrates how to design a scalable, secure, event-driven cloud architecture using fully managed AWS services — with no servers to provision or maintain.

---

## 🏗️ AWS Architecture

<p align="center">
  <img src="architecture/architecture-diagram.png" alt="AWS Architecture Diagram" width="900">
</p>

### 🔄 Architecture Flow

```text
Home Energy Device
        │
        ▼
   AWS IoT Core
        │
        ▼
   AWS Lambda
        │
        ▼
  Amazon DynamoDB
        │
        ▼
 Amazon CloudWatch
        │
        ▼
   Amazon SNS
```

**Flow summary:** A simulated smart energy device publishes readings to **AWS IoT Core**, which triggers an **AWS Lambda** function through an IoT Rule. Lambda processes and validates the payload, writes it to **Amazon DynamoDB**, and publishes an alert via **Amazon SNS** if usage crosses a defined threshold. **Amazon CloudWatch** logs every step of the pipeline for monitoring and troubleshooting.

---

## ☁️ AWS Services Used

| Service | Purpose |
|---|---|
| **AWS IoT Core** | Receives and routes messages from simulated IoT devices |
| **AWS Lambda** | Processes incoming events and applies business logic |
| **Amazon DynamoDB** | Stores energy readings as structured, queryable data |
| **Amazon SNS** | Sends real-time notification alerts on threshold breaches |
| **Amazon CloudWatch** | Provides monitoring, logging, and observability |
| **AWS IAM** | Manages secure, least-privilege access across services |
| **Amazon S3** | Hosts the static dashboard website |

---

## ✨ Features

- ⚡ Serverless, event-driven architecture
- 📡 Real-time energy usage monitoring
- 🗄️ Persistent data storage with DynamoDB
- 🔔 Automated SNS threshold alerts
- 📊 CloudWatch logging and observability
- 🖥️ Static web dashboard for viewing data
- 🔐 IAM-managed, least-privilege security
- 📈 Built to scale with managed AWS services

---

## 📂 Repository Structure

```
home-energy-monitor/
│
├── architecture/
│   ├── banner.png
│   └── architecture-diagram.png
│
├── lambda/
│   └── lambda_function.py
│
├── screenshots/
│   ├── Home page.png
│   ├── lambda.png
│   ├── Tables.png
│   ├── sns.png
│   ├── Buckets.png
│   └── Rules.png
│
├── README.md
├── index.html
├── script.js
└── style.css
```

---

## 📸 Project Screenshots

### 🖥️ Home Dashboard
<p align="center">
  <img src="screenshots/Home%20page.png" alt="Home Dashboard" width="800">
</p>

### ⚙️ AWS Lambda
<p align="center">
  <img src="screenshots/lambda.png" alt="AWS Lambda Function" width="800">
</p>

### 🗄️ Amazon DynamoDB
<p align="center">
  <img src="screenshots/Tables.png" alt="DynamoDB Tables" width="800">
</p>

### 🔔 Amazon SNS
<p align="center">
  <img src="screenshots/sns.png" alt="Amazon SNS Topic" width="800">
</p>

### 🪣 Amazon S3 Bucket
<p align="center">
  <img src="screenshots/Buckets.png" alt="S3 Buckets" width="800">
</p>

### 📡 AWS IoT Rule
<p align="center">
  <img src="screenshots/Rules.png" alt="AWS IoT Rule" width="800">
</p>

---

## 🛠️ How to Deploy

### Prerequisites
- An AWS account with console/CLI access
- AWS CLI configured with appropriate IAM permissions
- Python 3.x installed locally (for Lambda development/testing)
- Git installed locally

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/TempleStephen/home-energy-monitor.git
cd home-energy-monitor
```

**2. Create the DynamoDB table**
- Go to the DynamoDB console
- Create a new table (e.g. `EnergyReadings`) with a primary key such as `deviceId` (partition key) and `timestamp` (sort key)

**3. Deploy the Lambda function**
- Go to the Lambda console and create a new function
- Upload the code from `lambda/lambda_function.py`
- Attach an execution role with permissions for DynamoDB and SNS
- Set the DynamoDB table name and SNS topic ARN as environment variables

**4. Configure an IoT Rule**
- In AWS IoT Core, create a new Rule with a SQL query that matches your device's topic (e.g. `SELECT * FROM 'home/energy'`)
- Set the Lambda function as the rule's action/target

**5. Create an SNS Topic**
- Go to the Amazon SNS console and create a new topic
- Subscribe your email or phone number to receive alerts
- Confirm the subscription

**6. Deploy the dashboard**
- Upload `index.html`, `script.js`, and `style.css` to an S3 bucket configured for static website hosting, or deploy via GitHub Pages
- Update the dashboard's API/endpoint configuration to point to your deployed backend

**7. Test the pipeline**
- Publish a test message to your IoT topic (via the AWS IoT Core Test client or an MQTT client)
- Confirm the reading appears in DynamoDB, an SNS alert fires when the threshold is crossed, and CloudWatch logs the execution

---

## 🚀 Skills Demonstrated

- AWS Solutions Architecture
- Serverless Computing
- AWS Lambda (Python)
- AWS IoT Core & MQTT concepts
- Amazon DynamoDB (NoSQL data modeling)
- Amazon SNS (pub/sub notifications)
- Amazon CloudWatch (monitoring & logging)
- IAM security & least-privilege access design
- Static website hosting on Amazon S3
- Event-driven, decoupled architecture design
- Python & JavaScript development
- Git & GitHub version control

---

## 📚 Lessons Learned

Building this project strengthened my understanding of:

- Designing event-driven AWS architectures that scale automatically with demand
- Implementing fully serverless applications with no infrastructure to manage
- Processing and validating IoT events reliably with AWS Lambda
- Managing cloud security and access boundaries using IAM
- Monitoring and troubleshooting distributed systems with CloudWatch
- Building real-time alerting systems using Amazon SNS
- Structuring cloud projects for clarity, maintainability, and portfolio presentation

---

## 📈 Future Improvements

- [ ] Live MQTT data streaming from real hardware sensors
- [ ] User authentication (Amazon Cognito) for the dashboard
- [ ] Historical analytics and trend visualization
- [ ] Energy cost estimation based on local utility rates
- [ ] Integration with real IoT devices (e.g. smart plugs, meters)
- [ ] Mobile-responsive dashboard redesign
- [ ] Infrastructure as Code (Terraform / AWS SAM / CDK) for one-click deployment
- [ ] CI/CD pipeline for automated testing and deployment

---

## 👨‍💻 Author

**Temple Stephen**
*Cloud & AWS Solutions Architect*

[![GitHub](https://img.shields.io/badge/GitHub-TempleStephen-181717?logo=github&logoColor=white)](https://github.com/TempleStephen)
[![LinkedIn](https://www.linkedin.com/in/temple-stephen-74664a1b3/)](#)

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ on GitHub** — it helps others discover it too.
