import site
import sys
from typing import List


def get_site_packages_paths() -> List[str]:
    paths = []

    if hasattr(site, 'getsitepackages'):
        paths.extend(site.getsitepackages())

    paths.append(site.getusersitepackages())

    return list(set(paths))
