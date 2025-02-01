from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements.
    """
    file=open(file_path,'r')
    req=file.readlines()
    req=[data.replace('\n','') for data in req]
    if '-e .' in req:
        req.remove('-e .')

    print(req)
    return req

get_requirements('requirements.txt')


# setup(
#     name='zindi-SUA-Outsmarting-Outbreaks-Challenge',
#     version='0.0.1',
#     author='Sourabh',
#     author_email='prajapatisourabh22@gmail.com',
#     packages=find_packages(),
#     install_requires=get_requirements('requirements.txt')
# )