import os
import sys
import site
from pathlib import Path
from typing import Optional
from .utils import get_site_packages_paths


def get_package_path(package_name: str) -> Optional[Path]:

    

    for dir_path in get_site_packages_paths():
        candidate = Path(dir_path) / package_name
        if candidate.exists():
            return candidate
        
        candidate_alt = Path(dir_path) / package_name.replace("-", "_")
        if candidate_alt.exists():
            return candidate_alt
    return None


def calculate_directory_size(path: Path) -> int:

    total = 0
    for file in path.rglob('*'):
        if file.is_file():
            total += file.stat().st_size
    return total

def get_package_size(package_name: str) -> Optional[int]:
    path = get_package_path(package_name)
    if path and path.exists():
        return calculate_directory_size(path)
    return None
