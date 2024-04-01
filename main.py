import os
import time
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import observerInstance

def main():
    #Variáveis
    input_folder = 'C:\\Users\\fujim\\Downloads'

    output_folder = 'C:\\Users\\fujim\\Downloads'

    # Instancia a classe de monitoramento
    event_handler = observerInstance.MyHandler(input_folder, output_folder)
    observer = Observer()
    observer.schedule(event_handler, path=input_folder, recursive=False)
    observer.start()
    print(f"Monitorando o diretório: {input_folder}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

main()

