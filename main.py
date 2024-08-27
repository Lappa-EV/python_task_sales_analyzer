import matplotlib.pyplot as plt
import csv

class SalesAnalyzer:
    def __init__(self):
        self.sales_data = []

    def read_sales_data(self, file_path):
        '''Метод, который считывает данные о продажах из файла и добавляет их в список sales_data'''
        pass

    def total_sales_per_product(self):
        '''Метод, который возвращает общую сумму продаж для каждого продукта'''
        pass

    def sales_over_time(self):
        '''Метод, который возвращает общую сумму продаж в разрезе дат'''
        pass

    def max_revenue_product(self):
        '''Метод для определения какой продукт принес наибольшую выручку'''
        pass

    def max_sales_date(self):
        '''Метод для вычисления в какой день была наибольшая сумма продаж'''
        pass

    def plot_total_sales_per_product(self):
        '''Метод для постстроения столбчатой диаграммы общей суммы продаж по каждому продукту'''
        pass

    def plot_sales_over_time(self):
        '''Метод для построения графика общей суммы продаж по дням'''
        pass


analyzer = SalesAnalyzer()
analyzer.read_sales_data('E:/python/Git_projects/python_task/sales_data.csv')
print("1. Продукт, который принес наибольшую выручку: ", analyzer.max_revenue_product())
print("2. Дата, в которую была наибольшая сумма продаж: ", analyzer.max_sales_date())
analyzer.plot_total_sales_per_product()
analyzer.plot_sales_over_time()


