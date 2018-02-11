## 前景  
学习python中看到廖老师的xml操作，便想着来玩一把～大概有sax等几种方法，由于感觉这种比较麻烦，便找到了xml.etree.Element这个模块，轻量级的操作xml，挺好用的，关于内存占用的问题，因为还没遇到，似乎文档里面有解决方df案。学了xml操作之后，便学着用到小项目里面，顺便简单的学习了一下MVC这种架构.
## 思路  
- view层,只负责数据的显示，和向model层去请求数据。
- controller 层，负责接受用户的指令，调用视图，让视图去向model请求数据，拿到数据之后，通过view层显示数据。更改数据时，接受用户指令，直接作用于model之上
- model层，独立于控制器，和视图，可以独自进行数据的查，改
## 模块说明  
- view.py 负责向model请求数据，然后显示数据
- control.py 负责接受用户的指令，所有用户指令全部由它来接受，然后由它去调用view显示数据，调用model修改数据。只负责控制整个过程。
- model.py model层能独立于其它两层，它所有的实质功能都由它来操作，view只能调用它的功能
- Operator.py 负责操作数据xml的文件，也属于model层，为了清楚点，单独用了一个模块，model,py调用它来执行数据修改.然后修改之后，美化xml。  
![](https://github.com/21want28k/small_projects/blob/master/%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image/2018-02-11%2011-36-15%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png) 
## 代码示例  
- view.py
```python
from model.student模型 import Student as S

# 验证ID的存在性
def vertify(ID):
    if S.vertify(ID) == '存在':
        return '存在'
    else:
        return '不存在'


def get_all(ID):
    a = S(ID)
    return a.get_all()


def get_item(ID,attribute):
    a = S(ID)
    if attribute == 'time':
        return a.time
    if attribute == 'name':
        return a.name
    if attribute == 'sex':
        return a.sex
    if attribute == 'grade':
        return a.grade


if __name__ == '__main__':
    print(vertify('001'))
    print(get_all('002'))
    print(get_item('002', 'time'))
```
- control
```python
# 控制器，不同层面之间的组织作用，用于控制应用程序的流程，接收用户的行为，操作模型和视图
from model.student模型 import Student as S
from view import view
if __name__ == '__main__':
    print('**欢迎光临学生教务管理系统**')
    choice = input('功能选项:\n1：查看学生的信息\n2：删除学生的信息\n3:添加学生信息\n4:修改学生的信息:\n')
    # 这部分来验证学生的存在性
    if choice == '1' or choice == '2' or choice == '4':
        while True:
            ID = input('输入你要操作的学生学号\n')
            # 通知视图view去model里面查询有没有这个学生的信息
            result = view.vertify(ID)
            if result != '不存在':
                break
            else:
                print('你要找的学生不存在，请重新输入')
    if choice == '1':
        print(view.get_all(ID))
    if choice == '2':
        S.deltete(ID)
        print('删除成功')
    if choice == '3':
        print('按提示输入学生的信息')
        while True:
            ID = input('输入学生的学号')
            if view.vertify(ID) == '不存在':
                time = input('输入学生的入学时间')
                name = input('输入学生的名字')
                sex = input('输入学生的性别')
                grade = input('输入学生的成绩')
                S.add(ID, time, name, sex, grade)
                print('添加成功')
                break
            else:
                print('该学号已经存在，请重新输入')
    if choice == '4': 
        temp = input('1：修改学生的入学时间\n2：修改学生的名字\n3:修改学生的性别\n4：修改学生的成绩\n')
        dicta = {'1': 'time', '2': 'name', '3': 'sex', '4': 'grade'}
        info = view.get_item(ID, dicta[temp])
        content = input('学生当前的信息为：{0},输入修改之后的值\n'.format(info))
        a = S(ID)
        if temp == '1':
            a.time = content
        if temp == '2':
            a.name = content
        if temp == '3':
            a.sex = content
        if temp == '4':
            a.grade = content
        print('修改成功')

```
- student模型.py
```python
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
```
- OPerator.py
```python
# 用来处理数据的层
import xml.etree.ElementTree as ET
def indent(elem, level=0):
    i = "\n" + level * "\t"
    # 如果有子节点
    if len(elem):
        # 如果element里面text为空,或者只有空格
        if elem.text is None or elem.text.isspace():
            elem.text = i + "\t"
        # 如果element尾部没有内容
        if elem.tail is None or elem.tail.isspace():
            elem.tail = i
        # 如果是最外层的，尾部就不必有格式了
        if level == 0:
            elem.tail = ""
        # 对里面的每一个节点都执行这样的缩进
        for elem in elem:
            indent(elem, level + 1)
        # 执行完了之后，此时的elem是当前父节点的最后一个子节点,由于每个子节点之后都会是/n+/t的缩进，所以最后一个节点的tail = /n+/t
        # 注意，调用完了indent(elem,level + 1)之后，会回到这一行，此时level为0，element为最后一个子节点,i为/n
        # print(elem,repr(i))  # <Element 'test2' at 0x7fda7b2c0a48> '\n'
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        # 如果没有子节点
    else:
        if level and (elem.tail is None or elem.tail.isspace()):
            elem.tail = i
            elem.text = elem.text.strip()

class Operator:
    @staticmethod
    def verify(ID):
        tree = ET.parse('../data.xml')
        root = tree.getroot()
        for student in root.iter('student'):
            if student.get('id') == ID:
                return True
            else:
                pass

    @staticmethod
    def get(ID):
        temp = []
        tree = ET.parse('../data.xml')
        root = tree.getroot()
        for student in root.iter('student'):
            if student.get('id') == ID:
                for item in student:
                    temp.append(item.text)
        return temp

    @staticmethod
    def delete(ID):
        tree = ET.parse('../data.xml')
        root = tree.getroot()
        for student in root.findall('student'):
            if student.get('id') == ID:
                root.remove(student)
        indent(root)
        tree.write('../data.xml', encoding='utf-8')

    @staticmethod
    def increase(ID, time, name, sex, grade):
        tree = ET.parse('../data.xml')
        root = tree.getroot()
        student_id = ET.Element('student')
        student_id.set('id', ID)
        stu_time = ET.Element('time')
        stu_time.text = time
        stu_name = ET.Element('name')
        stu_name.text = name
        stu_sex = ET.Element('sex')
        stu_sex.text = sex
        stu_grade = ET.Element('grade')
        stu_grade.text = grade
        root.append(student_id)
        student_id.extend((stu_time, stu_name, stu_sex, stu_grade))
        indent(root)
        tree.write('../data.xml', encoding='UTF-8')

    @staticmethod
    def modify(ID, item, comment):
        tree = ET.parse('../data.xml')
        root = tree.getroot()
        for student in root.findall('student'):
            if student.get('id') == ID:
                temp = student.find(item)
                temp.text = comment
        indent(root)
        tree.write('../data.xml', encoding='UTF-8')

if __name__ == '__main__':
    a = Operator()
    results = a.get('001')
    print(results)
    a.modify('002', 'time', '2016')
    a.modify('002', 'grade', '99')
    print(a.verify('002'))
    print(a.get('002'))
    a.increase('003', '2016', '张三', '女', '98')
    a.delete('003')
```
- data.xml
```xml
<exam>
	<student id="001">
		<time>2015</time>
		<name>张三</name>
		<sex>男</sex>
		<grade>90</grade>
	</student>
	<student id="002">
		<time>2016</time>
		<name>李四</name>
		<sex>男</sex>
		<grade>99</grade>
	</student>
</exam>
```
## 效果展示
- 查看信息    
![](https://github.com/21want28k/small_projects/blob/master/%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image/%E6%9F%A5%E7%9C%8B%E5%8A%9F%E8%83%BD.png)  
- 添加信息    
![](https://github.com/21want28k/small_projects/blob/master/%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image/%E6%B7%BB%E5%8A%A0%E5%8A%9F%E8%83%BD.png)  
![](https://github.com/21want28k/small_projects/blob/master/%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image/xml%E6%B7%BB%E5%8A%A0.png)   
- 删除信息    
![](https://github.com/21want28k/small_projects/blob/master/%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image/%E5%88%A0%E9%99%A4%E5%8A%9F%E8%83%BD.png)  
![](https://github.com/21want28k/small_projects/blob/master/%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image/%E5%88%A0%E9%99%A4xml.png)     
- 修改信息    
![](https://github.com/21want28k/small_projects/blob/master/%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image/%E4%BF%AE%E6%94%B9.png)  
![](https://github.com/21want28k/small_projects/blob/master/%E5%AD%A6%E7%94%9F%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/image/%E4%BF%AE%E6%94%B9xml.png)   
## 总结
- 优点
	- 用到了MVC分层的思想
	- 运用了xml.etree.element模块
	 - 美化了修改的XML
	 - 简单的封装了所用的代码
- 不足之处
	 - 由于是第一次实际用到类，对类的书写还比较混乱，并不知道怎样正确地写一个类，需要改进，但是自己不知道怎么去改
	 - 要是用个GUI来实现功能会比较好，用户体验更好

虽说，代码写的蛮烂哈哈哈～不过总归是自己的一个练手小项目，玩的太少。还是第一次用分层的思想去实现自己的小项目，自己动手写了这么些代码，小有成就感～有待up～加油啦～，希望看到的各位大神，能指出我的不足，让我能够修改。完善，3Q
## 参考链接
[xml美化1](http://blog.csdn.net/shinobiii/article/details/8253976)  
[xml美化2](http://blog.linhere.com/archives/355.html)  
[MVC](https://draveness.me/mvx)  
[深入解读xml解析几种方式](http://codingpy.com/article/parsing-xml-using-python/)  
[python中文文档](http://python.usyiyi.cn/translate/python_352/library/xml.etree.elementtree.html#module-xml.etree.ElementTree)
