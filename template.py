import os
from pathlib import Path        #handles all the path errors due to '/' and '\'
import logging       #to log all info during run

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = "textSummarizer"

list_of_files = [                       #gitkeep is a eml file hidden deleted later
    ".github/wordflows/.gitkeep",     #automatically deploy in ci/cd when changes made in git commit
    f"src/{project_name}/__init__.py", #Constructor file needed as a localfile to do imports from files of the project
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    "test.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)           #detects the format of the path(win/mac)
    filedir, filename = os.path.split(filepath)   #split return file and folder values from the path

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file:{filepath}")
        
    else:
        logging.info(f"File already exists:{filename}")
