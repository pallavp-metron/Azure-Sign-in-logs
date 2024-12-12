import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import subprocess

def test_cli_help():
    result = subprocess.run(["python", "azure_logs_cli.py", "--help"], capture_output=True, text=True)
    assert result.returncode == 0  
    assert "Usage" in result.stdout