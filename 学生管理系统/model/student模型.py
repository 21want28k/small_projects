# model层主要封装业务的数据及数据处理的方法
from model.Operator import Operator as op


class Student:

    def __init__(self, value):
        self.__id = value
        lista = op.get(value)
        self.__time, self.__name, self.__sex, self.__grade = lista

    @staticmethod
    def vertify(ID):
        if op.verify(ID):
            return '存在'

    def get_all(self):
        return '学号{0}的信息为：{5}入学时间:{1}{5}姓名:{2}{5}性别:{3}{5}成绩:{4}{5}'.format(self.__id, self.__time, self.__name, self.__sex, self.__grade, '\n')

    @staticmethod
    def deltete(ID):
        op.delete(ID)
    
    @staticmethod
    def add(ID,time,name,sex,grade):
        op.increase(ID, time, name, sex, grade)

    @property
    def id(self):
        return self.__id

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        op.modify(self.__id, 'time', value)
        self.__time = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        op.modify(self.__id, 'name', value)
        self.__name = value

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        op.modify(self.__id, 'sex', value)
        self.__sex = value

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        op.modify(self.__id, 'sex', value)
        self.__grade = value


if __name__ == '__main__':
    a = Student('002')
    print(a.get_all())
