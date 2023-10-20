from setuptools import find_packages,setup
from typing import List
def getRequirements(filePath)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(filePath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n' , "") for req in requirements]
    return requirements

    
setup(
    name = "mlprojects",
    version = "0.0.1",
    author = "bivu",
    author_email = "mukherjee4004@gmail.com",
    packages = find_packages(),
    install_requires = getRequirements("requirements.txt")
)