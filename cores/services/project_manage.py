from datetime import datetime
from dataclasses import dataclass
from pathlib import Path
from cores.apis.seq import SequencetAnnotation
from cores.apis.project import ProjectAnnotation
import os
import shutil
import json



class ProjectManageService:
    @staticmethod
    def get_project(location):
        with open(f'{location}/project.json', 'r') as file:
            data = json.load(file)
        
        return ProjectAnnotation(
            name=data["project"],
            root_path=location,
            sequences_path=data["sequence_dir"]
        )
    
    @staticmethod
    def create_project(name, location):
        source_folder = "data/template"
        project_path = f'{location}/{name}'
        os.makedirs(project_path, exist_ok=True)
        
        if os.path.exists(source_folder):
            shutil.copytree(source_folder, project_path, dirs_exist_ok=True)
        else:
            raise Exception(f"Source folder '{source_folder}' does not exist!")
        
        with open(f'{project_path}/project.json', 'r') as file:
            data = json.load(file)
        
        data["project"] = name
        data["created_at"] = str(datetime.utcnow())
        
        with open(f'{project_path}/project.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        return ProjectAnnotation(
            name=name,
            root_path=location,
            sequences_path=data["sequence_dir"]
        )