import os
import time
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import export


class MyHandler(FileSystemEventHandler):
    """
    Classe para monitorar diretório
    """
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def on_created(self, event):
        if event.is_directory:
            return
        elif event.src_path.endswith('.xlsx'):
            print(f"Novo arquivo encontrado: {event.src_path}")
            export.excel_to_csv(event.src_path, self.output_folder)

