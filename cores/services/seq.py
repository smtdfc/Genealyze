from datetime import datetime
from dataclasses import dataclass
from pathlib import Path
import os
import shutil
import json

@dataclass
class SequencetAnnotation:
    name: str
    location: str
