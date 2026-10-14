import os
import unittest


class TestStudentManagementSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        cls.pages = ["index.html", "students.html", "courses.html", "teachers.html"]

    def test_html_files_exist(self):
        """Verify that all core HTML pages exist in the repository root."""
        for page in self.pages:
            path = os.path.join(self.root_dir, page)
            self.assertTrue(os.path.isfile(path), f"Missing page: {page}")

    def test_html_structure(self):
        """Verify that all HTML pages contain standard HTML5 tags and valid doctype."""
        for page in self.pages:
            path = os.path.join(self.root_dir, page)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            self.assertIn("<!DOCTYPE html>", content, f"{page} missing <!DOCTYPE html>")
            self.assertIn("<title>", content, f"{page} missing <title>")
            self.assertIn("<header>", content, f"{page} missing <header>")
            self.assertIn("<nav>", content, f"{page} missing <nav>")
            self.assertIn("</html>", content, f"{page} missing closing </html> tag")

    def test_navigation_bar_links(self):
        """Verify that every HTML page contains links to all other pages."""
        expected_links = ['href="index.html"', 'href="students.html"', 'href="courses.html"', 'href="teachers.html"']
        for page in self.pages:
            path = os.path.join(self.root_dir, page)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            for link in expected_links:
                self.assertIn(link, content, f"{page} missing navigation link {link}")

    def test_asset_links(self):
        """Verify that all HTML pages properly link to css/style.css and js/script.js."""
        for page in self.pages:
            path = os.path.join(self.root_dir, page)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            self.assertIn('href="css/style.css"', content, f"{page} should link to css/style.css")
            self.assertIn('src="js/script.js"', content, f"{page} should link to js/script.js")

    def test_css_stylesheet(self):
        """Verify that css/style.css exists and defines core styles."""
        css_path = os.path.join(self.root_dir, "css", "style.css")
        self.assertTrue(os.path.isfile(css_path), "css/style.css missing")
        with open(css_path, "r", encoding="utf-8") as f:
            content = f.read()

        for selector in ["body", "header", "nav", "button", "table"]:
            self.assertIn(selector, content, f"css/style.css missing styling for {selector}")

    def test_javascript_functions(self):
        """Verify that js/script.js exists and implements all required handlers."""
        js_path = os.path.join(self.root_dir, "js", "script.js")
        self.assertTrue(os.path.isfile(js_path), "js/script.js missing")
        with open(js_path, "r", encoding="utf-8") as f:
            content = f.read()

        expected_functions = [
            "welcomeMessage",
            "showMessage",
            "addStudent",
            "searchStudent",
            "addCourse",
            "addTeacher",
        ]
        for fn in expected_functions:
            self.assertIn(f"function {fn}", content, f"js/script.js missing function: {fn}")

    def test_milestone_files(self):
        """Verify that all M5, M6, and M7 files and directories are present."""
        expected_paths = [
            "Dockerfile",
            "docker-compose.yml",
            "nginx.conf",
            "health",
            "prometheus.yml",
            os.path.join("monitoring", "prometheus.yml"),
            os.path.join("monitoring", "dashboard.json"),
            os.path.join("k8s", "deployment.yaml"),
            os.path.join("k8s", "service.yaml"),
            os.path.join("docs", "deployment.png"),
            os.path.join("docs", "kubectl_get_pods.png"),
        ]
        for p in expected_paths:
            full_path = os.path.join(self.root_dir, p)
            self.assertTrue(os.path.exists(full_path), f"Required milestone path missing: {p}")


if __name__ == "__main__":
    unittest.main()

