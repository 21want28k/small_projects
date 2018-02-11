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
