import subprocess

def uninstall_package(package_name: str) -> bool:
    try:
        result = subprocess.run(
            ["pip", "uninstall", package_name, "-y"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to uninstall {package_name}: {e.stderr}")
        return False