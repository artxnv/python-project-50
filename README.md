### Hexlet tests and linter status:
[![Actions Status](https://github.com/artxnv/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/artxnv/python-project-50/actions)

[![Test Coverage](https://codeclimate.com/github/artxnv/python-project-50/badges/coverage.svg)](https://codeclimate.com/github/artxnv/python-project-50/coverage)

[![Maintainability](https://api.codeclimate.com/v1/badges/5bdc7500247f242dfa70/maintainability)](https://codeclimate.com/github/artxnv/python-project-50/maintainability)

[![Python CI](https://github.com/artxnv/python-project-50/actions/workflows/python-ci.yml/badge.svg)](https://github.com/artxnv/python-project-50/actions/workflows/python-ci.yml)



# Описание:
Вычислитель отличий. проект Hexlet.

Программа принимает на вход два файла конфигурации типов JSON или YAML. Возвращает отличия второго от первого, какие тэги были добавлены, какие удалены, какие изменены.

Результат может быть представлен в различных видах.


## Установка, тестирование, проверка линтером

Установка производится вызовом: make setup

[![asciicast](https://asciinema.org/a/pQgKilfMQ3cL2OkxWk9KgOfxI.svg)](https://asciinema.org/a/pQgKilfMQ3cL2OkxWk9KgOfxI)


### Сравнение двух файлов:

[![asciicast](https://asciinema.org/a/kdTqg4QyaqlSvHHpZzIx9TqSP.svg)](https://asciinema.org/a/kdTqg4QyaqlSvHHpZzIx9TqSP)


### Сравнение вложенных стуктур:

[![asciicast](https://asciinema.org/a/u60VWgrO2D1eIScrvQxk88tv1.svg)](https://asciinema.org/a/u60VWgrO2D1eIScrvQxk88tv1)


### Программа может вернуть результат в разных форматах:

#### default - 'Stylish'

#### 'plain'

#### 'Json'

### Использование с форматом 'plain':

[![asciicast](https://asciinema.org/a/mzGLkFDEZeqvrEk4EwnxtUgLi.svg)](https://asciinema.org/a/mzGLkFDEZeqvrEk4EwnxtUgLi)


### Использование с форматом 'json':

[![asciicast](https://asciinema.org/a/87CBrRHXlBefxbXibKif7dBHV.svg)](https://asciinema.org/a/87CBrRHXlBefxbXibKif7dBHV)