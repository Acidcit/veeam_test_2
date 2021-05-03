import hashlib
import sys

args = sys.argv
path_to_file = args[1]
path_to_dir = args[2]

with open(path_to_file, 'r', encoding='utf-8') as text_file:  # открываем файл с именами файлов
    for line in text_file:
        try:  # исключение, если в строчке не три параметра
            file_name, algorithm, hash_ = line.split()
            print(file_name, end=' ')
            try:  # исключение, если не удается открыть указанный файл
                with open(path_to_dir + file_name, 'rb') as file:  # открываем файл, чтобы вычислить его хэш
                    if algorithm == 'md5':
                        h = hashlib.md5()
                    elif algorithm == 'sha1':
                        h = hashlib.sha1()
                    elif algorithm == 'sha256':
                        h = hashlib.sha256()
                    else:
                        print('UNKNOWN ALGORITHM', algorithm)
                        continue
                    b = file.read()
                    h.update(b)
                    print('OK' if h.hexdigest() == hash_ else 'FAIL')

            except FileNotFoundError:
                print('NOT FOUND')

        except ValueError:
            print('INVALID INPUT')



