import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info
from game import play
import os

save_info('start')

# argument 0 self script 1 commands
try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать комманду (help) для справки')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)

    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)

    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки или файла')
        else:
            delete_file(name)

    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Укажите исходное имя файла или папки и новое имя для копии')
        else:
            copy_file(name, new_name)

    elif command == 'play':
        play()

    elif command == 'cmd':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Укажите путь до папки')
        else:
            os.path.isdir(name)
            os.chdir(name)
            print("Текущая директория изменилась на folder:", os.getcwd())

    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('play - загадай число компьютер будет угадывать')

    save_info('end')