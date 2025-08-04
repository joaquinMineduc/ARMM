from Frontend.Variables import directory_social_programs, dir_output_PDFs
import shutil
import os
from pathlib import Path


def rename_and_copy():
    files = [f for f in directory_social_programs.iterdir() if f.is_file()]
    for file in files:
        shutil.copy(Path(directory_social_programs)/file.name, Path(dir_output_PDFs/'13.pdf'))
    
   

