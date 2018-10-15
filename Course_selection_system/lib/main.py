from login import *
from manager import *
from student import *
from teacher import *
def main():
    r=login()
    action = {
        'Manager': Manager,
        'Student': Student,
        'Teacher': Teacher
    }
    if r['user_status']:
        print('登陆成功')
        obj = action[r['id']](r['name'])
        def continue_operate(cls):
            for nub,item in enumerate(cls.action,1):
                print(nub,item)
            try :
                n=int(input('输入编号'))-1
                fun = cls.action[n]
                if hasattr(obj, fun):
                    getattr(obj, fun)()
            except ValueError:
                print('必须为限定的数字')
        while 1:
            continue_operate(action[r['id']])
    else:
        print('输入错误')
main()


