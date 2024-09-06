from setuptools import find_packages,setup
from typing import List

hypern_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the lis of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hypern_e_dot in requirements:
            requirements.remove(hypern_e_dot)

setup(
name='mlproject',
version='0.0.1',
author='Dhondraj',
author_email='dhondraj1@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)