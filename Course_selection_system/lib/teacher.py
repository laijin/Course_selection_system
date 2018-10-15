from people import *
import pickle
class Teacher(People):
    action=['info_courses','info_class','info_student','exit']
    def __init__(self,name):
        self.name=name
        self.course=[]
    def info_class(self):
        print('查看班级')
        f=open('course_info','rb')
        for line in f:
            print(line)
    def info_student(self):
        print('查看学生')
        f=open('student_info', 'rb')
        count = 0
        while 1:
            try:
                count += 1
                student_obj = pickle.load(f)
                print(count, student_obj.name)
            except EOFError:
                break
    def exit(self):
        exit()
    @staticmethod
    def init(name):
        f=open('teacher_info','rb')
        while 1:
            teacher_obj = pickle.load(f)
            if teacher_obj.name == name:
                return teacher_obj