# Парсер каталога мебели BST
##### _Собирает данные по позициям из списка файла xlsx, сохраняет полученные параметры в базу данных "bst_furniture"_ 

### Настройки

Для быстрой проверки алгоритма воспользуйтесь наборами тестовых данных

| Флаг | Свойство |
| ------ | ------ |
| READ_XLS | флаг чтения исходных данных из xls/xlsx |
| FILE_XLS | исходный xls/xlsx файл|
| URL | url страницы поиска 

### Алгоритм работы:
- При READ_XLS == True заполняет "product_details.name" значениями 1 колонки FILE_XLS
- При READ_XLS == False выполянет поиск url страниц товаров с помощью webdriver и формы поиска на странице URL, обходит страницы и спомощью request получает параметры товаров и записывает в таблицу product_details




