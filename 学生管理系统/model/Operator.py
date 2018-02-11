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