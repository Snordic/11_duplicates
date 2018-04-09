# Описание проекта

Данный скрип производит поиск дубликатов в папке.

Поиск происходит по всем вложенным папкам. Если были найдены файлы с одинаковым именем и размером, то данные файлы являются дубликатами.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5.

Запуск на Linux:

```bash

$ python duplicates.py You_search_folder # possibly requires call of python3 executive instead of just python


Были найденны следующие дубликаты:

Файл 3421wq.txt и пути к нем: 
five\\second\\3421wq.txt
five\\3421wq.txt

Файл 3421wq.txt и пути к нем: 
five\\second\\three_2\\3421wq.txt
five\\3421wq.txt

Файл 11123qqq.txt и пути к нем: 
five\\second_2\\three\\11123qqq.txt
five\\second\\three\\11123qqq.txt
```

Запуск на Windows происходит аналогично.


# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
