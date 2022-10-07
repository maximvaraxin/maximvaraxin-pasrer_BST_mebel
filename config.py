from db import Furniture_db
import pandas as pd

class configClass():
   DATABASE = Furniture_db('bst_furniture.db')
   pd.options.display.max_colwidth = 300

   # флаг чтения исходных данных из xls
   READ_XLS = False
   cols =[0]
   FILE_XLS = pd.read_excel('./catalog.xlsx', sheet_name='sheet1')

   URL = "https://btsmebel.ru/search/"
   HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}