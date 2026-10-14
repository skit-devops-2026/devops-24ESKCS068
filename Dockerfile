# Production container for Student Management System
FROM nginx:1.27-alpine

LABEL maintainer="Aryan Sharma <aryan.sharma6122@gmail.com>" \
      description="Student Management System Web Application" \
      version="1.0.0"

# Set working directory to Nginx html folder
WORKDIR /usr/share/nginx/html

# Remove default static files
RUN rm -rf /usr/share/nginx/html/*

# Copy web assets
COPY index.html ./
COPY students.html ./
COPY courses.html ./
COPY teachers.html ./
COPY css/ ./css/
COPY js/ ./js/
COPY health ./health

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose HTTP port
EXPOSE 80

# Container healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:80/health || exit 1

# Launch Nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
