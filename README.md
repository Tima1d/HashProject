# HashProject
 Этот проект — аналитический инструмент для анализа блокчейн-данных, нацеленный на изучение блоков, форков, майнинговых вознаграждений и других аспектов блокчейнов. Основная цель — обеспечить глубокое понимание структуры блокчейна.

## Содержание

1. [Описание Задач](#описание-задач)
2. [Как использовать](#как-использовать)
3. [Структура проекта](#структура-проекта)
4. [Технологии](#технологии)

## Описание Задач

Проект направлен на решение следующих вопросов:

1. Автор и номер блока с хэшем вида 0х000.......000.
2. Длина наименьшего форка в системе.
3. Номер первого блока в форке наименьшей длины.
4. Длина наибольшего форка.
5. Хэш последнего блока в отброшенной ветке форка наибольшей длины.
6. Количество форков, произошедших в системе.
7. Размер вознаграждения за создание блока #71.
8. Период сокращения размера вознаграждения за создание блока.
9. Коэффициент сокращения вознаграждения за выработку блока.
10. Номер блока, в котором размер вознаграждения впервые будет равен 0,09.
11. Блоки с дополнительной информацией в поле secret_info.
12. Сбор информации в порядке её появления в цепочке.
13. Декодирование ключевой строки из полученного значения.

## Как использовать

Опишите, как установить зависимости, запустить скрипты или программы и как интерпретировать результаты.

## Структура проекта

- `/src`: Исходный код проекта.
- `/transactions`: Данные, используемые или генерируемые проектом.

## Технологии

В проекте используются следующие технологии и модули Python:

- `os.listdir`: Для перечисления файлов и директорий в указанной папке.
- `json.load`: Для загрузки и декодирования JSON данных из файла.
- `itertools.takewhile`: Используется для обработки элементов последовательности до тех пор, пока выполняется заданное условие.
- `functools.reduce`: Применяется для выполнения кумулятивных вычислений на элементах последовательности.


