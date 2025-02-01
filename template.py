import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO)#,format='[%(asctime)s]-[%(message)s]')

project_name="SUA Outsmarting Outbreaks Challenge"

list_of_files=[
    # ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    # "app.py",
    # "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for file in list_of_files:
    file_path=Path(file)
    file_dir,file_name=os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Crating Directory {file_dir} for the filename {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path))==0:
        with open(file_path,'w') as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{file_name} is alread exists.")