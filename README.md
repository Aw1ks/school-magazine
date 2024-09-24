# school-magazine
This project finds (n) the number of the best students among grades 10 and 9. The table is made using the library [Pandas](https://habr.com/ru/companies/ruvds/articles/494720/)
## How to install
This project uses libraries such as: [random](https://python-scripts.com/random?ysclid=m0zhzk6iqx773448571), [argparse](https://docs.python.org/3/library/argparse.html) and [Pandas](https://habr.com/ru/companies/ruvds/articles/494720/)

Python3 should already be installed. Use `pip` (or `pip3`, there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
## Launch example
Just run the code Initially, the number of the best students will be 3.

To run the code and change the number of top students, you need to call an argument when running the script and specify the number of students:
```
 python school_magazine.py --number (the number of the best students (up to 20))
```
To change the letter of the class, you need to call an argument when running the script and specify the letter of the class:
```
python school_magazine.py --letter (the letter of the class)
```
To change the class digit, you need to call an argument when running the script and specify the class digit:
```
python school_magazine.py --klass (the number of the class)
```
