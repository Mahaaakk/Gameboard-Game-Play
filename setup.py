from setuptools import find_packages , setup
from typing import List

def get_requirements()->List[str]:
    
    reuiremets_list : List[str] = []
    return reuiremets_list

setup(
    name = 'ImageProc',
    version = "0.0.1",
    author = "Mahak",
    author_eamil = "Mahakp1611@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements() ,#["pymongo"]
    
    
)
