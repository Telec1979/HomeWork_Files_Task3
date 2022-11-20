import os # Импортируем модуль для работы с операционной системой

def compile_files(files_list): # Определяем функцию записи в новый файл
    data = {} # Определяем словарь, где будем хранить содержимое файлов
    for file in files_list: # Для каждого файла из переданного списка
        with open(file, encoding="utf-8") as f: # открываем файл на чтение
            file_data = f.readlines() # Читаем содержимое в список
            data[len(file_data)] = (file, " ".join(file_data)) # Добавляем в словарь запись, где ключ количество строк, значение -список из названия файла и его содержимого

    data = dict(sorted(data.items())) # сортируем словарь по значениям

    with open("result_data.txt", "w", encoding="utf-8") as new_file: # Открываем итоговый файл на запись
        for key, value in data.items(): # Для каждой записи отсортированного словаря 
            new_file.write(f"{value[0]} \n") # Записываем в файл название файла
            new_file.write(f"{key} \n") # Записываем количество строк
            new_file.write(f"{value[1]} \n") # Записываем текст


files = ["1.txt", "2.txt", "3.txt"] # Определяем список с именами фавйлов
files = [os.path.join(os.getcwd(), file) for file in files] # Для каждого файла из списка добавляем путь к нему
compile_files(files) # Вызываем функцию записи для определенного списка с именами файлов