# Анализ данных о продажах продуктов в магазине

## Задание

Необходимо написать программу, которая будет анализировать данные о продажах продуктов в магазине и строить графики наглядного представления информации. В ходе создания программы необходимо реализовать следующие функции:

- `read_sales_data(file_path)` - функция, которая принимает путь к файлу и возвращает список продаж. Продажи представляют собой словари с ключами `product_name`, `quantity`, `price`, `date` (название, количество, цена, дата).
- `total_sales_per_product(sales_data)` - функция, которая принимает список продаж и возвращает словарь, в котором ключ - название продукта, а значение - общая сумма продаж этого продукта.
- `sales_over_time(sales_data)` - функция, которая принимает список продаж и возвращает словарь, в котором ключ - дата, а значение - общая сумма продаж за эту дату.

## Входные данные

Данные о продажах хранятся в файле [sales_data.csv](https://github.com/Lappa-EV/python_task_sales_analyzer/blob/master/sales_data.csv) в формате: название продукта, количество, цена, дата.

Пример входных данных:

```text
яблоки, 10, 15, 2024-06-21 
груши, 16, 11, 2024-06-22
```

## Решение

Для решения поставленной задачи был создан файл [main.py](https://github.com/Lappa-EV/python_task_sales_analyzer/blob/master/main.py),  который содержит класс `SalesAnalyzer`. В классе реализованы методы:

- `read_sales_data(self, file_path)` - считывает данные о продажах из файла и добавляет их в список `self.sales_data`.
- `total_sales_per_product(self)` - вычисляет общую выручку по каждому продукту.
- `sales_over_time(self)` - вычисляет общую выручку по датам продаж.
- `plot_total_sales_per_product(self)` - строит столбчатую диаграмму общей выручки по каждому продукту.
- `plot_sales_over_time(self)` - строит график общей выручки по датам продаж.
- `max_revenue_product(self)` - находит продукт с наибольшей выручкой.
- `max_sales_date(self)` - находит дату с наибольшей общей выручкой.


## Результаты

В результате работы программы выводится следующая информация:
1. Продукт с наибольшей выручкой
2. Дата с наибольшей выручкой 

Также строятся два графика: 
1.  Общая сумма продаж по каждому продукту
2.  Общая сумма продаж по датам


Для запуска программы выполните команду:

```
python main.py
```

**Библиотеки, используемые в проекте:**

- matplotlib
- csv

**Автор:** Катерина Лаппа
