import os
import logging
from collections import namedtuple
import sys

# Настройка логирования
logging.basicConfig(filename='directory_contents.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Определение namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def collect_directory_info(directory_path):
    # Проверяем, является ли указанный путь директорией
    if not os.path.isdir(directory_path):
        print(f'Ошибка: {directory_path} не является директорией.')
        return

    # Список для хранения информации о файлах и каталогах
    contents = []

    # Проходим по всем элементам в директории
    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        parent_directory = os.path.basename(directory_path)

        if os.path.isdir(full_path):
            # Если это каталог
            info = FileInfo(name=entry, extension='', is_directory=True, parent_directory=parent_directory)
            contents.append(info)
            logging.info(f'Найден каталог: {info}')
        else:
            # Если это файл
            name, extension = os.path.splitext(entry)
            info = FileInfo(name=name, extension=extension.lstrip('.'), is_directory=False, parent_directory=parent_directory)
            contents.append(info)
            logging.info(f'Найден файл: {info}')

    return contents

def main():
    if len(sys.argv) != 2:
        print('Использование: python script.py <путь_до_директории>')
        sys.exit(1)

    directory_path = sys.argv[1]
    collect_directory_info(directory_path)

if __name__ == '__main__':
    main()

