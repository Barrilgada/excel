import os
import time
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def excel_to_csv(input_file, output_folder):
    """
    Funcão para exportar arquivos .xlss para .csv

    :param input_file: dirétorio onde está com arquivo
    :param output_folder: diretório para onde vai o arquivo exportado
    """
    #Lê o arquivo
    file = pd.read_excel(input_file)

    #Ajusta o nome
    csv_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + '.csv')

    #Separador ';' para não bugar as colunas
    file.to_csv(csv_file, index=False, sep=';', encoding='utf-8-sig')
    print(f"Arquivo {input_file} convertido para CSV com sucesso!")

