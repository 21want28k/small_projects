from model.student模型 import Student as S


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