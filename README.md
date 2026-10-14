# Student Management System

## Author

| Roll No. | Name | GitHub username |
|---|---|---|
| 24ESKCS068 | Aryan Sharma | Aryansharma68 |

## About

This Student Management System is a comprehensive web application used to manage and display academic information about students, courses, and teachers. It allows administrators to register student records, manage course offerings, organize faculty profiles, and quickly search through records. The project uses HTML5, CSS3, JavaScript, Docker containerization, Kubernetes orchestration, Prometheus and Grafana observability, GitHub Actions CI/CD, and Jenkins declarative pipelines.

## Tech stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Web Server / Container**: Nginx 1.27 Alpine, Docker, Docker Compose
- **Orchestration**: Kubernetes (Kind / K3d / Minikube)
- **Monitoring & Observability**: Prometheus, Grafana
- **CI/CD**: GitHub Actions, GitHub Packages Container Registry (GHCR), Jenkins

## Live URL

https://aryansharma68.github.io/student-management-system-2/

The application is deployed live on GitHub Pages:
- Web Application: [https://aryansharma68.github.io/student-management-system-2/](https://aryansharma68.github.io/student-management-system-2/)
- Health Endpoint: [https://aryansharma68.github.io/student-management-system-2/health](https://aryansharma68.github.io/student-management-system-2/health)

## Health endpoint

`GET /health` returns JSON health check information:

```json
{
  "status": "UP",
  "service": "student-management-system",
  "version": "1.0.0"
}
```

## Running locally

### Using Make and Local Python Server
```bash
make install
make test
make run
```
Then open `http://localhost:8000` in your web browser.

### Using Docker Compose (App + Prometheus + Grafana)
```bash
docker compose up -d --build
```
Access points:
- Web Application: `http://localhost:8000`
- Prometheus Server: `http://localhost:9090`
- Grafana Dashboard: `http://localhost:3000` (User: `admin` / Password: `admin`)

## Containerization (Module 5)

The container image is built using the multi-stage Alpine Nginx `Dockerfile` and published to GitHub Container Registry (GHCR):

- Image: `ghcr.io/aryansharma68/student-management-system-2:latest`

Pull and run directly:
```bash
docker pull ghcr.io/aryansharma68/student-management-system-2:latest
docker run -d -p 8000:80 --name student-app ghcr.io/aryansharma68/student-management-system-2:latest
```

## Deployment & Monitoring (Module 6)

- **Prometheus Configuration**: Defined in `monitoring/prometheus.yml` and `prometheus.yml`.
- **Grafana Dashboard**: Committed in `monitoring/dashboard.json` with auto-provisioning under `monitoring/grafana-provisioning/`.
- **Deployment Screenshot**: Committed under `docs/deployment.png`.

## Kubernetes (Module 7)

Kubernetes manifests are located in `k8s/`:
- `k8s/deployment.yaml`: Deploys 2 replicas referencing `ghcr.io/aryansharma68/student-management-system-2:latest` with HTTP liveness and readiness probes.
- `k8s/service.yaml`: Exposes the pods via a `NodePort` service on port 30080.
- `docs/kubectl_get_pods.png`: Verification screenshot showing pods running in Ready state.

Deploy to a cluster:
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods -l app=student-management-system
```

## Testing

Run the automated test suite and static file validation:

```bash
make test
```