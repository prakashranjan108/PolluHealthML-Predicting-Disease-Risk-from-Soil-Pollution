import os
from pathlib import Path

# Setup basic logging
import logging

# Define custom exception class
class TemplateGenerationException(Exception):
    def __init__(self, message):
        super().__init__(message)

# Logger setup
LOG_FILE = "template_generation.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

project_name = "soil_disease_project"

list_of_files = [

    f"{project_name}/__init__.py",

    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/trainer.py",
    f"{project_name}/components/evaluator.py",
    f"{project_name}/components/model_deployer.py",

    f"{project_name}/configuration/__init__.py",

    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/soil_disease_data.py",

    f"{project_name}/constants/__init__.py",

    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",

    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",

    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "dvc.yaml",
    "config/model.yaml",
    "config/schema.yaml",
]

try:
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Directory created or already exists: {filedir}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
                pass
            logging.info(f"File created: {filepath}")
        else:
            logging.warning(f"File already exists and is not empty: {filepath}")

    print("✅ Project scaffold generated successfully.")
    logging.info("Project scaffold generation completed successfully.")

except Exception as e:
    logging.error(f"Error while generating project structure: {str(e)}")
    raise TemplateGenerationException(f"Error in template.py: {str(e)}")
