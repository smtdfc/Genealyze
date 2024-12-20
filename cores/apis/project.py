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
