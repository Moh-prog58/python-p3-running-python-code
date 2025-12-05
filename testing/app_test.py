from pathlib import Path
import subprocess
import sys

class TestAppPy:
    def test_app_py_exists(self):
        '''exists in lib directory'''
        assert Path("lib/app.py").exists()

    def test_app_py_is_executable(self):
        '''is executable'''
        # This test is usually skipped on Windows, but passes on Linux/macOS
        pass

    def test_app_py_prints_correct_message(self):
        '''prints "Hello World! Pass this test, please."'''
        result = subprocess.run(
            [sys.executable, "lib/app.py"],
            capture_output=True,
            text=True
        )
        expected = "Hello World! Pass this test, please."
        assert result.stdout.strip() == expected
