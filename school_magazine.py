import pandas as pd
import random
import argparse

from random import randint

                                                                        
def analysis_academic_performance(table, number_best_students):
    #for best_students in table['mean'][:number_best_students]:
    best_students = table[['parall', 'bukva', 'name', 'mathematics', 'russian', 'computer science', 'mean']]
    best_students = table.sort_values(by = 'mean', ascending=False).head(number_best_students)
    print(best_students)

def main():
    parser = argparse.ArgumentParser(description='Этот код находит (n) кол-во лучших учащихся среди 10 и 9 классов. Запустите файл: shcool_magazine.py --number(чило лучших учеников)')
    parser.add_argument('--number',
                        type=int,
                        default=3,
                        help='Введите колличечтво лучших учеников (до 20)')

    args = parser.parse_args()
    number_best_students = args.number

    klas = {'A':['Смирнов', 'Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Попов', 'Васильев', 'Михайлов', 'Федоров', 'Павлов'], 
'B':['Ковалев', 'Егоров', 'Леонов', 'Лебедев', 'Новиков', 'Суханов', 'Алексеев', 'Григорьев', 'Тимофеев', 'Зайцев']
}

    table = pd.DataFrame(klas)        
    table = table.melt()
    table = table.rename(columns={"variable": "bukva", "value": "name"})

    mat = [randint(3,5) for i in range(len(table))]
    rus = [randint(3,5) for i in range(len(table))]
    inf = [randint(3,5) for i in range(len(table))]

    table['mathematics'] = mat
    table['russian'] = rus
    table['computer science'] = inf

    table['mean'] = (table['mathematics'] + table['russian'] + table['computer science'])/3
    table = table.sort_values(by = 'mean', ascending=False).head(20)
    table = table.reset_index(drop = True)

    spis = [9 if i%2==1 else 10 for i in range(len(table))]
    table['parall'] = spis

    #table = table[['parall', 'bukva', 'name', 'mathematics', 'russian', 'computer science', 'mean']]
    tabl = table.pivot_table(index = ['parall', 'bukva'], columns = 'mathematics', values = 'mean', aggfunc = 'count')

    #print(table)
    # print(tabl)
    analysis_academic_performance(table, number_best_students)
    

if __name__ == '__main__':
        main()