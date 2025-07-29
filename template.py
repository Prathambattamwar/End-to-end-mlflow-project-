import os 
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "mlProject"


list_of_files = {
    ".github/workflow/.gitkeep",
    f"src/{project_name}/init.py",
f"src/{project_name}/components/_init.py",
f"src/{project_name}/utils/init.py",
f"src/{project_name}/utils/common.py",
f"src/{project_name}/config/init.py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/pipeline/init.py",
f"src/{project_name}/entity/init.py",
f"src/{project_name}/entity/config_entity.py",
f"src/{project_name}/constants/init.py",
"config/config.yaml",
"params.yaml",
"schema.yaml",
"main.py",
"app.py",
"Dockerfile",
"requirements.txt",
"setup.py",
"research/trials.ipynb",
"templates/index.html"
}

for filepath in list_of_files:
    filepath= Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir , )