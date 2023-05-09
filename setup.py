"""
Whenever setup.py will run , find_packages() in it, will consider 'src' as a package itself since it contains '__init__.py'.
And after that it builds, once it builds, I can import it whereever I want, but we need it to put in pypi itself so it can be used as pandas,matplolib 
"""

from setuptools import find_packages,setup
from typing import List

HYPHEN = '-e.'

def get_req(file_path:str)->List[str]:

    req=[]
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [r1.replace("\n","") for r1 in req]

        if HYPHEN in req:
            req.remove(HYPHEN)

    return req 

setup(  
name = 'genericml',
version = '0.0.1',
author='Prakhara',
author_email='kumarprakhara01@gmail.com',
packages=find_packages(),
install_requires = get_req('requirements.txt')

)