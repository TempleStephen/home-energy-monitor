# 🏡 Home Energy Monitor

A serverless AWS-based Home Energy Monitoring solution that collects energy usage data from IoT devices, processes the data using AWS Lambda, stores it in DynamoDB, and notifies users through Amazon SNS when energy usage exceeds predefined thresholds.

---

## 📌 Project Overview

This project demonstrates how to build a scalable, event-driven IoT application using AWS cloud services.

The architecture simulates smart home energy monitoring where connected devices send electricity usage data to AWS IoT Core. The data is processed by a Lambda function, stored in DynamoDB, and monitored for abnormal energy consumption. When a threshold is exceeded, Amazon SNS sends an alert notification to the user.

---

## 🏗️ Architecture

The solution uses the following AWS services:

- AWS IoT Core
- AWS Lambda
- Amazon DynamoDB
- Amazon SNS
- Amazon CloudWatch
- IAM
- Amazon S3 (for documentation/assets)

### Architecture Flow

IoT Device
⬇
AWS IoT Core
⬇
AWS Lambda
⬇
Amazon DynamoDB
⬇
CloudWatch Monitoring
⬇
Amazon SNS Notifications

---

## 🚀 Features

- Collects IoT energy usage data
- Serverless architecture
- Stores readings in DynamoDB
- Sends real-time alerts using SNS
- Event-driven processing with Lambda
- Scalable and cost-effective design

---

## 📂 Repository Structure

```
home-energy-monitor/
│
├── README.md
├── architecture/
│   └── architecture-diagram.png
│
├── lambda/
│   └── lambda_function.py
│
├── screenshots/
│   ├── Home page.png
│   ├── Buckets.png
│   ├── Lambda.png
│   ├── Rules.png
│   ├── SNS.png
│   └── ...
│
└── website/
    ├── index.html
    ├── style.css
    └── script.js
```

---

## ⚙️ AWS Services Used

| Service | Purpose |
|----------|----------|
| AWS IoT Core | Receives IoT device messages |
| AWS Lambda | Processes incoming data |
| Amazon DynamoDB | Stores energy readings |
| Amazon SNS | Sends alert notifications |
| Amazon CloudWatch | Monitoring and logging |
| IAM | Permissions and security |
| Amazon S3 | Stores architecture documentation |

---

## 📸 Screenshots

### AWS Architecture

`architecture/architecture-diagram.png`

### AWS Console

Screenshots demonstrating:

- IoT Rules
- Lambda Function
- DynamoDB Table
- SNS Topic
- S3 Bucket
- IAM Policies
- CloudWatch Logs

---

## 🛠️ Technologies

- AWS Lambda
- AWS IoT Core
- Amazon DynamoDB
- Amazon SNS
- Amazon CloudWatch
- HTML
- CSS
- JavaScript
- Python

---

## 🔮 Future Improvements

- Real IoT device integration
- Live dashboard
- User authentication
- Historical analytics
- Energy consumption forecasting
- Cost estimation dashboard

---

## 👨‍💻 Author

**Temple Stephen**

Cloud & DevOps Engineer

GitHub:
https://github.com/TempleStephen

LinkedIn:
(Add your LinkedIn URL here)

---

## 📄 License

This project is for educational and portfolio purposes.