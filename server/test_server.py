import json
import os
import subprocess
import sys
import time
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

class ServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        env = os.environ.copy()
        env.update(SDEVICE_HOST="127.0.0.1", SDEVICE_PORT="18765", SDEVICE_TOKEN="test-token-that-is-at-least-24-characters")
        cls.process = subprocess.Popen([sys.executable, os.path.join(os.path.dirname(__file__), "sdevice_server.py")], env=env, stdout=subprocess.DEVNULL)
        for _ in range(40):
            try:
                urlopen("http://127.0.0.1:18765/health", timeout=.3)
                break
            except OSError:
                time.sleep(.1)
        else:
            cls.process.terminate()
            raise RuntimeError("Server failed to start")
    @classmethod
    def tearDownClass(cls):
        cls.process.terminate()
        cls.process.wait(timeout=5)
    def test_health(self):
        with urlopen("http://127.0.0.1:18765/health") as r:
            self.assertEqual(json.load(r)["status"], "ok")
    def test_dashboard(self):
        with urlopen("http://127.0.0.1:18765/dashboard") as r:
            page = r.read().decode("utf-8")
            self.assertIn("S DEVICE", page)
            self.assertIn("PROJECTOR MODE", page)
            self.assertEqual(r.headers.get("X-Content-Type-Options"), "nosniff")
    def test_cross_platform_app(self):
        with urlopen("http://127.0.0.1:18765/app/") as r:
            page = r.read().decode("utf-8")
            self.assertIn("S DEVICE", page)
            self.assertIn("iOS", page)
            self.assertEqual(r.headers.get("X-Frame-Options"), "DENY")
    def test_pwa_files(self):
        for path, mime in [
            ("/app/manifest.webmanifest", "application/manifest+json"),
            ("/app/sw.js", "application/javascript"),
            ("/app/icon.svg", "image/svg+xml"),
        ]:
            with self.subTest(path=path):
                with urlopen("http://127.0.0.1:18765" + path) as r:
                    self.assertEqual(r.status, 200)
                    self.assertIn(mime, r.headers.get("Content-Type"))
    def test_post_denied(self):
        req = Request("http://127.0.0.1:18765/api/v1/device", data=b"{}", method="POST")
        with self.assertRaises(HTTPError) as e:
            urlopen(req)
        self.assertEqual(e.exception.code, 401)
    def test_protected(self):
        with self.assertRaises(HTTPError) as e:
            urlopen("http://127.0.0.1:18765/api/v1/device")
        self.assertEqual(e.exception.code, 401)
    def test_authenticated(self):
        req = Request("http://127.0.0.1:18765/api/v1/device", headers={"Authorization": "Bearer test-token-that-is-at-least-24-characters"})
        with urlopen(req) as r:
            self.assertEqual(json.load(r)["product"], "S Device One")
if __name__ == "__main__":
    unittest.main()
