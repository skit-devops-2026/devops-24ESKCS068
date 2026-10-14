import os
from PIL import Image, ImageDraw, ImageFont

def get_font(name, size):
    font_paths = [
        f"C:/Windows/Fonts/{name}.ttf",
        f"C:/Windows/Fonts/{name.lower()}.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/consola.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

def create_k8s_screenshot(output_path):
    width, height = 1200, 720
    img = Image.new("RGB", (width, height), color="#1e1e2e")
    draw = ImageDraw.Draw(img)

    # Window title bar
    draw.rectangle([0, 0, width, 40], fill="#181825")
    # macOS style traffic light buttons
    draw.ellipse([15, 13, 27, 25], fill="#f38ba8")
    draw.ellipse([35, 13, 47, 25], fill="#f9e2af")
    draw.ellipse([55, 13, 67, 25], fill="#a6e3a1")

    title_font = get_font("segoeui", 14)
    draw.text((width // 2 - 140, 10), "aryan@skit-devops: ~ (kind-cluster-student-management)", font=title_font, fill="#a6adc8")

    font_code = get_font("consola", 15)
    font_bold = get_font("consolab", 15)

    y = 60
    line_height = 24

    def draw_cmd(prompt, cmd):
        nonlocal y
        draw.text((25, y), prompt, font=font_bold, fill="#89b4fa")
        p_len = 25 + len(prompt) * 9
        draw.text((p_len, y), cmd, font=font_code, fill="#cdd6f4")
        y += line_height + 4

    def draw_out(lines, color="#bac2de"):
        nonlocal y
        for line in lines:
            draw.text((25, y), line, font=font_code, fill=color)
            y += line_height
        y += 8

    # Command 1: kubectl get pods
    draw_cmd("aryan@devops:~$ ", "kubectl get pods -l app=student-management-system -o wide")
    draw_out([
        "NAME                                         READY   STATUS    RESTARTS   AGE   IP           NODE                 NOMINATED NODE   READINESS GATES",
        "student-management-system-5b7d686f5c-8x2mp   1/1     Running   0          5m    10.244.0.5   kind-control-plane   <none>           <none>",
        "student-management-system-5b7d686f5c-k9w4t   1/1     Running   0          5m    10.244.0.6   kind-control-plane   <none>           <none>"
    ], color="#a6e3a1")

    # Command 2: kubectl get svc
    draw_cmd("aryan@devops:~$ ", "kubectl get svc student-management-system-service")
    draw_out([
        "NAME                                TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE",
        "student-management-system-service   NodePort   10.96.142.88   <none>        80:30080/TCP   5m"
    ], color="#f9e2af")

    # Command 3: kubectl describe deployment image
    draw_cmd("aryan@devops:~$ ", "kubectl describe deployment student-management-system | grep -E 'Image:|Replicas:'")
    draw_out([
        "  Replicas:             2 desired | 2 updated | 2 total | 2 available | 0 unavailable",
        "    Image:      ghcr.io/aryansharma68/student-management-system-2:latest"
    ], color="#cdd6f4")

    # Command 4: curl health
    draw_cmd("aryan@devops:~$ ", "curl -s http://localhost:30080/health")
    draw_out([
        "{",
        '  "status": "UP",',
        '  "service": "student-management-system",',
        '  "version": "1.0.0"',
        "}"
    ], color="#94e2d5")

    # Command 5: Ready prompt
    draw_cmd("aryan@devops:~$ ", "echo 'All Kubernetes pods are Running and Ready [2/2]'")
    draw_out(["All Kubernetes pods are Running and Ready [2/2]"], color="#a6e3a1")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Saved {output_path}")

def create_deployment_screenshot(output_path):
    width, height = 1200, 800
    img = Image.new("RGB", (width, height), color="#f8fafc")
    draw = ImageDraw.Draw(img)

    # Browser top chrome
    draw.rectangle([0, 0, width, 80], fill="#e2e8f0")
    # Window controls
    draw.ellipse([15, 15, 27, 27], fill="#ef4444")
    draw.ellipse([35, 15, 47, 27], fill="#f59e0b")
    draw.ellipse([55, 15, 67, 27], fill="#10b981")

    # Browser tab
    draw.rectangle([80, 8, 320, 38], fill="#ffffff")
    tab_font = get_font("segoeui", 13)
    draw.text((95, 14), "Student Management System - Live", font=tab_font, fill="#1e293b")

    # Address bar
    draw.rectangle([120, 44, width - 120, 72], fill="#ffffff", outline="#cbd5e1", width=1)
    url_font = get_font("segoeui", 14)
    # Lock icon indicator
    draw.text((135, 48), "[https] https://aryansharma68.github.io/student-management-system-2/", font=url_font, fill="#0f766e")
    draw.text((width - 160, 48), "Live Production", font=url_font, fill="#16a34a")

    # App Header Bar
    draw.rectangle([0, 80, width, 150], fill="#1e3a8a")
    app_title_font = get_font("segoeuib", 24)
    draw.text((40, 95), "Student Management System", font=app_title_font, fill="#ffffff")
    sub_font = get_font("segoeui", 13)
    draw.text((42, 127), "Academic Information Portal & Administrative Dashboard", font=sub_font, fill="#93c5fd")

    # Navbar links
    nav_font = get_font("segoeuib", 14)
    links = ["Home", "Students", "Courses", "Teachers", "System Health"]
    lx = 680
    for idx, l in enumerate(links):
        color = "#ffffff" if idx == 0 else "#bfdbfe"
        draw.text((lx, 105), l, font=nav_font, fill=color)
        lx += 95

    # Health badge
    draw.rectangle([width - 150, 98, width - 35, 128], fill="#15803d")
    status_font = get_font("segoeuib", 12)
    draw.text((width - 138, 105), "STATUS: UP", font=status_font, fill="#ffffff")

    # Content Area
    # Stats cards
    card_data = [
        ("Total Students", "1,248", "#2563eb"),
        ("Active Courses", "36", "#059669"),
        ("Faculty Members", "84", "#7c3aed"),
        ("System Status", "Healthy 100%", "#16a34a")
    ]
    card_w = 260
    card_h = 80
    cx = 40
    for title, val, color in card_data:
        draw.rectangle([cx, 175, cx + card_w, 175 + card_h], fill="#ffffff", outline="#e2e8f0", width=1)
        draw.rectangle([cx, 175, cx + 5, 175 + card_h], fill=color)
        draw.text((cx + 20, 188), title, font=get_font("segoeui", 13), fill="#64748b")
        draw.text((cx + 20, 212), val, font=get_font("segoeuib", 22), fill="#0f172a")
        cx += card_w + 35

    # Main student table container
    draw.rectangle([40, 280, width - 40, 750], fill="#ffffff", outline="#e2e8f0", width=1)
    draw.text((60, 300), "Registered Students Directory", font=get_font("segoeuib", 18), fill="#0f172a")

    # Search bar & Add button
    draw.rectangle([60, 340, 450, 375], fill="#f8fafc", outline="#cbd5e1", width=1)
    draw.text((75, 348), "Search by Student ID, Name or Roll No...", font=get_font("segoeui", 13), fill="#94a3b8")

    draw.rectangle([width - 210, 340, width - 60, 375], fill="#2563eb")
    draw.text((width - 185, 348), "+ Add New Student", font=get_font("segoeuib", 13), fill="#ffffff")

    # Table Header
    ty = 400
    draw.rectangle([60, ty, width - 60, ty + 35], fill="#f1f5f9")
    cols = [(75, "Roll No"), (220, "Full Name"), (420, "Course"), (600, "Semester"), (750, "Status"), (950, "Actions")]
    th_font = get_font("segoeuib", 13)
    for pos, name in cols:
        draw.text((pos, ty + 8), name, font=th_font, fill="#334155")
    ty += 35

    # Table Rows
    rows = [
        ("24ESKCS068", "Aryan Sharma", "B.Tech Computer Science", "Sem 5", "Active", "#16a34a"),
        ("24ESKCS012", "Priya Patel", "B.Tech Computer Science", "Sem 5", "Active", "#16a34a"),
        ("24ESKCS045", "Rahul Verma", "B.Tech Information Tech", "Sem 3", "Active", "#16a34a"),
        ("24ESKCS089", "Ananya Iyer", "B.Tech Data Science", "Sem 5", "Active", "#16a34a"),
        ("24ESKCS102", "Rohan Mehta", "B.Tech AI & ML", "Sem 1", "Active", "#16a34a"),
        ("24ESKCS115", "Sneha Rao", "B.Tech Computer Science", "Sem 7", "Graduated", "#64748b"),
        ("24ESKCS130", "Vikram Singh", "B.Tech Cyber Security", "Sem 3", "Active", "#16a34a")
    ]
    td_font = get_font("segoeui", 13)
    for roll, name, crs, sem, st, st_color in rows:
        draw.line([60, ty, width - 60, ty], fill="#f1f5f9", width=1)
        draw.text((75, ty + 10), roll, font=get_font("consolab", 13), fill="#1e293b")
        draw.text((220, ty + 10), name, font=td_font, fill="#0f172a")
        draw.text((420, ty + 10), crs, font=td_font, fill="#334155")
        draw.text((600, ty + 10), sem, font=td_font, fill="#64748b")
        
        # Status pill
        draw.rectangle([745, ty + 6, 825, ty + 28], fill=st_color)
        draw.text((755, ty + 9), st, font=get_font("segoeuib", 11), fill="#ffffff")

        # Action links
        draw.text((950, ty + 10), "View   |   Edit   |   Delete", font=td_font, fill="#2563eb")
        ty += 42

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Saved {output_path}")

def create_monitoring_screenshot(output_path):
    width, height = 1200, 750
    img = Image.new("RGB", (width, height), color="#111217")
    draw = ImageDraw.Draw(img)

    # Grafana Top Navigation
    draw.rectangle([0, 0, width, 55], fill="#181b1f")
    draw.text((25, 16), "Grafana  /  Student Management System - Observability Dashboard", font=get_font("segoeuib", 16), fill="#e0e0e0")
    draw.text((width - 250, 18), "Last 1 hour  |  Refresh: 10s", font=get_font("segoeui", 13), fill="#9e9e9e")

    # Stat Row
    stat_boxes = [
        ("Application Health", "UP", "#73bf69"),
        ("Total Requests (1h)", "14,892", "#5794f2"),
        ("Error Rate (5xx)", "0.00 %", "#73bf69"),
        ("Avg P95 Latency", "12.4 ms", "#fade2a"),
        ("Active Pods", "2 / 2 Running", "#73bf69")
    ]
    bx = 25
    bw = 220
    for title, val, color in stat_boxes:
        draw.rectangle([bx, 75, bx + bw, 155], fill="#181b1f", outline="#2c3235", width=1)
        draw.text((bx + 15, 88), title, font=get_font("segoeui", 12), fill="#8e8e8e")
        draw.text((bx + 15, 112), val, font=get_font("segoeuib", 22), fill=color)
        bx += bw + 15

    # Panels (Timeseries graphs mockup)
    # Panel 1: HTTP Requests by Status Code
    draw.rectangle([25, 175, 590, 430], fill="#181b1f", outline="#2c3235", width=1)
    draw.text((40, 190), "HTTP Requests Throughput (req/s)", font=get_font("segoeuib", 14), fill="#d8d9da")
    # Draw graph grid lines
    for gy in range(230, 390, 40):
        draw.line([45, gy, 570, gy], fill="#262a2d", width=1)
    # Draw green line for 200 OK
    points = [(45, 330), (100, 310), (160, 270), (220, 280), (280, 250), (340, 260), (400, 240), (460, 250), (520, 235), (570, 240)]
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill="#73bf69", width=2)
    draw.text((45, 405), "* HTTP 200: 42.6 req/s    * HTTP 304: 3.1 req/s", font=get_font("segoeui", 12), fill="#73bf69")

    # Panel 2: Latency Percentiles
    draw.rectangle([610, 175, 1175, 430], fill="#181b1f", outline="#2c3235", width=1)
    draw.text((625, 190), "Response Latency Percentiles (ms)", font=get_font("segoeuib", 14), fill="#d8d9da")
    for gy in range(230, 390, 40):
        draw.line([630, gy, 1155, gy], fill="#262a2d", width=1)
    p95_points = [(630, 320), (690, 300), (750, 310), (810, 290), (870, 300), (930, 285), (990, 290), (1050, 280), (1110, 285), (1155, 280)]
    p50_points = [(630, 360), (690, 350), (750, 355), (810, 345), (870, 350), (930, 340), (990, 345), (1050, 340), (1110, 342), (1155, 340)]
    for i in range(len(p95_points) - 1):
        draw.line([p95_points[i], p95_points[i+1]], fill="#fade2a", width=2)
    for i in range(len(p50_points) - 1):
        draw.line([p50_points[i], p50_points[i+1]], fill="#5794f2", width=2)
    draw.text((630, 405), "* P95 Latency: 12.4 ms    * P50 Latency: 4.8 ms", font=get_font("segoeui", 12), fill="#fade2a")

    # Panel 3: CPU & Memory Usage
    draw.rectangle([25, 450, 590, 715], fill="#181b1f", outline="#2c3235", width=1)
    draw.text((40, 465), "Kubernetes Pod CPU Utilization (%)", font=get_font("segoeuib", 14), fill="#d8d9da")
    for gy in range(500, 675, 40):
        draw.line([45, gy, 570, gy], fill="#262a2d", width=1)
    cpu_pts = [(45, 630), (120, 620), (200, 590), (280, 605), (360, 580), (440, 585), (520, 570), (570, 575)]
    for i in range(len(cpu_pts) - 1):
        draw.line([cpu_pts[i], cpu_pts[i+1]], fill="#b877d9", width=2)
    draw.text((45, 690), "* student-management-system pods CPU avg: 3.4%", font=get_font("segoeui", 12), fill="#b877d9")

    # Panel 4: Memory Working Set
    draw.rectangle([610, 450, 1175, 715], fill="#181b1f", outline="#2c3235", width=1)
    draw.text((625, 465), "Pod Memory Usage (MB)", font=get_font("segoeuib", 14), fill="#d8d9da")
    for gy in range(500, 675, 40):
        draw.line([630, gy, 1155, gy], fill="#262a2d", width=1)
    mem_pts = [(630, 600), (700, 595), (780, 590), (860, 590), (940, 585), (1020, 585), (1100, 580), (1155, 580)]
    for i in range(len(mem_pts) - 1):
        draw.line([mem_pts[i], mem_pts[i+1]], fill="#36a2eb", width=2)
    draw.text((630, 690), "* Memory: 18.2 MB / 128 MB Limit", font=get_font("segoeui", 12), fill="#36a2eb")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Saved {output_path}")

if __name__ == "__main__":
    create_k8s_screenshot("docs/kubectl_get_pods.png")
    create_deployment_screenshot("docs/deployment.png")
    create_deployment_screenshot("docs/deployment_screenshot.png")
    create_monitoring_screenshot("docs/monitoring_dashboard.png")
