from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT=' -e .'


def get_requirements(file_path:str)->list[str]:
    ''' Read the requirements file and return the list of requirements'''
    requirements=[]
    with open(file_path) as f:
        requirements = f.read().readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='text-generation',
    version='0.1',
    author='Nikhil',
    author_email='nikhilmahesh89@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)