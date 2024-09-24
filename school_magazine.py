import pandas as pd
import random
import argparse

from random import randint

                                                                        
def analysis_academic_performance(table, number_best_students, klass_students, bukva_students, klas):
    if klass_students == 9:
        table['parall'] = 9

    elif klass_students == 10:
        table['parall'] = 10

    else:
        table = ''   
        print('Ты ввел не существующий класс....')


    if bukva_students.lower() == 'а':
        class_A_names = dict(zip(klas['Б'], klas['А']))

        table['bukva'] = table['bukva'].replace({'Б': 'А'})
        table['name'] = table['name'].replace(class_A_names)

    elif bukva_students.lower() == 'б':
        class_B_names = dict(zip(klas['А'], klas['Б']))

        table['bukva'] = table['bukva'].replace({'А': 'Б'})
        table['name'] = table['name'].replace(class_B_names)

    elif bukva_students.lower() == 'none':
        class_A_and_B_names = klas
        class_A_and_B = dict(zip(klas['А'], klas['Б']))

        table['bukva'] = table['bukva'].replace(class_A_and_B)
        table['name'] = table['name'].replace(class_A_and_B_names)

    else:
        table = ''    
        print('Ты ввел не существующий класс....')   

    best_students = table[['parall', 'bukva', 'name', 'mathematics', 'russian', 'computer science', 'mean']]
    best_students = table.sort_values(by = 'mean', ascending=False).head(number_best_students)

    return best_students


def main():
    parser = argparse.ArgumentParser(description='Этот код находит (n) кол-во лучших учащихся среди 10 и 9 классов. ')
    parser.add_argument('--number',
                        type=int,
                        default=3,
                        help='Введите колличечтво лучших учеников (до 20)')
    parser.add_argument('--klass',
                        type=int,
                        default=10,
                        help='Введите класс 9 или 10')
    parser.add_argument('--letter',
                        type=str,
                        choices=['А', 'а', 'Б', 'б', 'None', 'none'],
                        default='None',
                        help='Введите букву класса А или Б (НА РУССКОМ ЯЗЫКЕ)')

    args = parser.parse_args()
    number_best_students = args.number
    klass_students = args.klass
    bukva_students = args.letter

    klas = {'А':['Смирнов', 'Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Попов', 'Васильев', 'Михайлов', 'Федоров', 'Павлов'], 
'Б':['Ковалев', 'Егоров', 'Леонов', 'Лебедев', 'Новиков', 'Суханов', 'Алексеев', 'Григорьев', 'Тимофеев', 'Зайцев']
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

    print(analysis_academic_performance(table, number_best_students, klass_students, bukva_students, klas))
    

if __name__ == '__main__':
        main()
