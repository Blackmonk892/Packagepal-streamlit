import json
import subprocess
from typing import List, Dict

def get_installed_packages() -> List[Dict[str, str]]:
    try:
        result = subprocess.run(
            ["pip", "list", "--format=json"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        packages = json.loads(result.stdout)
        return packages
    except subprocess.CalledProcessError as e:
        print(f"Error fetching pip packages:", e.stderr)
        return []