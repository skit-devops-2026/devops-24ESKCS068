# Kubernetes Deployment

This directory contains the Kubernetes orchestration manifests for the Student Management System.

## Architecture

- **Deployment (`deployment.yaml`)**:
  - Image: `ghcr.io/aryansharma68/student-management-system-2:latest`
  - Replicas: 2
  - Configured with HTTP liveness and readiness probes pointing to `/health`.
  - Resource requests and limits for memory and CPU.
- **Service (`service.yaml`)**:
  - Exposes the deployment as a `NodePort` on port `30080` (container port 80).

## Deploying to a Local Cluster (Kind or K3d)

### 1. Create a Kind Cluster
```bash
kind create cluster --name student-management
```

### 2. Apply Manifests
```bash
kubectl apply -k k8s/
# or
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 3. Verify Pods and Service
```bash
kubectl get pods -l app=student-management-system
kubectl get svc student-management-system-service
```

### 4. Access Application
Forward port to localhost:
```bash
kubectl port-forward svc/student-management-system-service 8080:80
```
Then visit `http://localhost:8080` or `http://localhost:8080/health`.
