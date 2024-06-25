from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    HYPHEN ='-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace('\n','') for req in requirements]

        if HYPHEN in requirements:
            requirements.remove(HYPHEN)

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='ritesh_kunugunla',
author_email='kunugunla.ritesh.mec21@itbhu.ac.in',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)