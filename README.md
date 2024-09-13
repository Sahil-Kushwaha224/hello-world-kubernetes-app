# Hello World Application

## Overview
This is a simple "Hello, World!" web application built with Node.js, Dockerized, and deployed on Kubernetes. 

## Prerequisites
- Docker
- Kubernetes (kubectl and Minikube to be installed and configured)
- kubectl

## Setup Instructions

### Steps

1. **Build and Run Docker Image Locally**
   - Build the Docker image:
     ```bash
     docker build -t hello-world-code .
     ```
   - Run the Docker container:
     ```bash
     docker run -p 5000:5000 hello-world-code
     ```

2. **Deploy to Kubernetes**
   - Start Minikube:
     ```bash
     minikube start
     ```
   - Apply the Deployment configuration:
     ```bash
     kubectl apply -f deployment.yaml
     ```
   - Apply the Service configuration:
     ```bash
     kubectl apply -f service.yaml
     ```

3. **Access the Application**
   - Get the Minikube IP:
     ```bash
     minikube ip
     ```
   - Access the application in your browser at:
     ```
     http://<minikube-ip>:30000
     ```
     or

     Using curl: You can also use curl to check:
     bash
     curl http://<minikube-ip>:30000

4. **Scale the Application**
   - Scale the number of replicas:
     ```bash
     kubectl scale deployment hello-world-app-deployment --replicas=<number-of-replicas>
     ```

5. **Troubleshooting**
   - Check service and pod statuses:
     ```bash
     kubectl get svc
     kubectl get pods
     ```
   - Use Minikube tunnel if necessary:
     ```bash
     minikube tunnel
     ```

