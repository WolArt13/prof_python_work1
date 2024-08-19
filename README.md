# Домашнее задание к лекции 1. «Import. Module. Package»

1. Разработана **структура** программы «Бухгалтерия»:
- main.py;  
- application/salary.py;  
- application/db/people.py.

Main.py — основной модуль для запуска программы.  
В модуле ```salary.py``` функция **calculate_salary**.  
В модуле ```people.py``` функция **get_employees**.  

2. Импортированы функции в модуль main.py и вызываются в конструкции:
```
if __name__ == '__main__':
```

3. Ознакомлен с модулем [datetime](https://pythonworld.ru/moduli/modul-datetime.html). 
При вызове функций модуля ```main.py``` выводится текущая дата.

1. Нашел интересные для себя пакеты **BeautifulSoup** и **Colorama** на [pypi](https://pypi.org/) и в файле ```requirements.txt``` указал их с актуальной версией. На основе этих модулей написан скраппер изображений на примере с сайтом **Нетологии** в файле ```images_scrapper.py```.

\*5. Создан рядом с файлом ```main.py``` модуль ```dirty_main.py``` и импортированы все функции с помощью
конструкции:
```
from package.module import *
``` 


