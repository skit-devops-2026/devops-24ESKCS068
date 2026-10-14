# Monitoring Infrastructure

This directory contains the observability stack configuration for the Student Management System.

## Components

1. **Prometheus (`prometheus.yml`)**:
   - Scrapes metrics from the Student Management System container (`web:80/stub_status`).
   - Scrapes internal Prometheus server metrics.
   - Default scrape interval: 15 seconds.

2. **Grafana Dashboard (`dashboard.json`)**:
   - Comprehensive observability dashboard for Student Management System.
   - Monitors:
     - Application health & uptime (`up{job="student-management-system"}`)
     - HTTP request rate and throughput (`nginx_http_requests_total`)
     - Error rate tracking (5xx and 4xx status codes)
     - Request latency percentiles (P50 and P95 response times)
     - Pod CPU and memory utilization

3. **Automated Provisioning (`grafana-provisioning/`)**:
   - `datasources/prometheus.yaml`: Automatically connects Grafana to Prometheus.
   - `dashboards/dashboards.yaml`: Automatically imports `dashboard.json` into Grafana on startup.

## Quick Start

Launch the complete monitoring stack locally:

```bash
docker compose up -d
```

- **Web Application**: [http://localhost:8000](http://localhost:8000)
- **Prometheus UI**: [http://localhost:9090](http://localhost:9090)
- **Grafana Dashboard**: [http://localhost:3000](http://localhost:3000) (User: `admin`, Password: `admin`)
