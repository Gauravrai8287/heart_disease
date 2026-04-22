from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements
setup(
    name="heart_disease_prediction",
    version= "0.0.1",
    author="Gaurav_Rai",
    description="A machine learning project to predict heart disease .",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
    )