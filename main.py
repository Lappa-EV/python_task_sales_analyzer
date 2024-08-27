import matplotlib.pyplot as plt
from collections import defaultdict
import csv

class SalesAnalyzer:
    def __init__(self):
        self.sales_data = []

    def read_sales_data(self, file_path):
        '''Метод, который считывает данные о продажах из файла и добавляет их в список sales_data'''
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                product_name, quantity, price, date = row
                sale = {
                    'product_name': product_name,
                    'quantity': int(quantity),
                    'price': int(price),
                    'date': date
                }
                self.sales_data.append(sale)

    def total_sales_per_product(self):
        '''Метод, который возвращает общую сумму продаж для каждого продукта'''
        total_sales = defaultdict(int)
        for sale in self.sales_data:
            total_sales[sale['product_name']] += sale['quantity'] * sale['price']
        return dict(total_sales)

    def sales_over_time(self):
        '''Метод, который возвращает общую сумму продаж в разрезе дат'''
        total_sales = defaultdict(int)
        for sale in self.sales_data:
            total_sales[sale['date']] += sale['quantity'] * sale['price']
        return dict(total_sales)

    def max_revenue_product(self):
        '''Метод для определения какой продукт принес наибольшую выручку'''
        total_sales = self.total_sales_per_product()
        max_revenue_product = max(total_sales, key=total_sales.get)
        return max_revenue_product

    def max_sales_date(self):
        '''Метод для вычисления в какой день была наибольшая сумма продаж'''
        total_sales = self.sales_over_time()
        max_sales_date = max(total_sales, key=total_sales.get)
        return max_sales_date

    def plot_total_sales_per_product(self):
        '''Метод для постстроения столбчатой диаграммы общей суммы продаж по каждому продукту'''
        total_sales = self.total_sales_per_product()
        products = list(total_sales.keys())
        sales = list(total_sales.values())
        plt.bar(products, sales, width=0.3)
        plt.xlabel('Продукт')
        plt.ylabel('Объем продаж')
        plt.title('График общей суммы продаж по каждому продукту')
        plt.xticks(rotation=10)
        plt.subplots_adjust(bottom=0.16)
        plt.show()

    def plot_sales_over_time(self):
        '''Метод для построения графика общей суммы продаж по дням'''
        total_sales = self.sales_over_time()
        dates = list(total_sales.keys())
        sales = list(total_sales.values())
        plt.plot(dates, sales, marker='o', color='purple')
        plt.xlabel('Дата')
        plt.ylabel('Объем продаж')
        plt.title('График общей суммы продаж по дням')
        plt.xticks(rotation=10)
        plt.subplots_adjust(bottom=0.16)
        plt.grid(True)
        plt.show()


analyzer = SalesAnalyzer()
analyzer.read_sales_data('E:/python/Git_projects/python_task_sales_analyzer/sales_data.csv')
print("1. Продукт, который принес наибольшую выручку: ", analyzer.max_revenue_product())
print("2. Дата, в которую была наибольшая сумма продаж: ", analyzer.max_sales_date())
analyzer.plot_total_sales_per_product()
analyzer.plot_sales_over_time()


