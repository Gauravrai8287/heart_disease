import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
project_name = 'heart_disease_prediction'
list_of_files = [
    'github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/components/data_ingestion.py',
    f'src/{project_name}/components/feature_engineering.py',
    f'src/{project_name}/components/data_Transformation.py',
    f'src/{project_name}/components/model_trainer.py',
    f'src/{project_name}/components/model_monitoring.py',
    f'src/{project_name}/pipelines/__init__.py',
    f'src/{project_name}/pipelines/training_pipeline.py',
    f'src/{project_name}/pipelines/prediction_pipeline.py',
    f'src/{project_name}/exception.py',
    f'src/{project_name}/logger.py',
    f'src/{project_name}/utils.py',
    "app.py",
    'requirements.txt',
    'setup.py'
    



]
for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    # Create directory if not exists
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    # Create file if not exists or empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists and is not empty")