import os
from pathlib import (Path)
import logging

#----Logging string

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')



project_name= 'cnnClassifier'

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    'dvc.yaml',
    'params.yaml',
    'requirement.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html',
    'test.py'
]


for filespath in list_of_files:
    filespath=Path(filespath)
    filedir,filename=os.path.split(filespath)



    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'creating directory; {filedir} for the file: {filename}')
    if (not os.path.exists(filespath) or (os.path.getsize(filespath)==0)):
        with open(filespath,'w') as f:
            pass
            logging.info(f'creating empty file : {filespath}')
    else:
        logging.info(f'{filename} is already exists')





