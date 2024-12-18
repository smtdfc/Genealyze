from datetime import datetime
from dataclasses import dataclass
from pathlib import Path
from .seq import SequencetAnnotation
import os
import shutil
import json

@dataclass
class ProjectAnnotation:
    name: str
    root_path: str
    sequences_path: str

    def get_list_seq(self):
        list_seq = []
        path = Path(f'{self.root_path}/{self.name}/{self.sequences_path}')
        
        for file_path in path.iterdir():
            if file_path.is_file():
                file_extension = file_path.suffix
                if file_extension == ".seq_genealyze":
                    list_seq.append(SequencetAnnotation(
                      name=file_path.name,
                      location=str(file_path)
                    ))
        return list_seq


class ProjectManage:
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