import os
import sys


def file_comparison(file1, file2):
    if file1['name'] == file2['name'] and \
                    file1['size'] == file2['size'] and \
                    file1['path'] != file2['path']:
        return True


def search_name_size_pth(pth):
    list_file_info = []
    for name_pth, dir_name, list_file_name in os.walk(pth):
        for name_file in list_file_name:
            full_path_file = os.path.join(name_pth, name_file)
            size_file = os.path.getsize(full_path_file)
            file_info = dict(path=full_path_file, name=name_file, size=size_file)
            list_file_info.append(file_info)
    return list_file_info


def duplicates_search(list_file_info):
    list_duplicates = []
    buffer_dict = {}
    for file1 in list_file_info:
        for file2 in list_file_info:
            if file_comparison(file1, file2):
                buffer_dict = list_file_info.pop(list_file_info.index(file2))
                buffer_dict.update({'path_2': file1['path']})
                list_duplicates.append(buffer_dict)
    return list_duplicates


def duplicates_print(duplicates_list, pth):
    if duplicates_list:
        print('\nБыли найдены следующие дубликаты:\n\n')
        for file in duplicates_list:
            print('----- Файл {} ----- \n{}\n{}\n\n'
                  .format(file['name'], file['path'],file['path_2']))
    else:
        print('В папке {} дубликатов не было найдено!'.format(pth))


if __name__ == '__main__':
    try:
        work_pth = sys.argv[1]
        list_file_search = search_name_size_pth(work_pth)
        result_duplicate = duplicates_search(list_file_search)
        duplicates_print(result_duplicate, work_pth)
    except (IndexError, FileNotFoundError):
        print('Вы не добавили папку для поиска!')
