from setuptools import setup,find_packages
from typing import List

def get_requirements_list()->List[str]:
    with open("requirements.txt") as req_file:
        return req_file.readlines().remove("-e .")

setup(
    name    = "Housing Predictor",
    version = "0.0.1",
    author  = "Pravin SK",
    description = "House price prediction project",
    packages = find_packages(),
    install_requires = get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list)