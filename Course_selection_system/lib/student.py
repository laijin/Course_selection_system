from people import *
import pickle
import os
class Student(People):
    action=['info_courses','control_course','check_course','exit']
    def __init__(self,name):
        self.name=name
        self.course=[]
    def control_course(self):
        print('选择课程')
        self.info_courses()
        f=open('course_info','rb')
        n=input('选择课程序号')
        n=int(n)
        count=1
        while 1:
            try:
                course_obj=pickle.load(f)
                if n == count:
                    self.course.append(course_obj)
                    print(self.course)
                    print('已选中课程%s'%(course_obj.name))
                    break
                count+=1
            except EOFError:
                print('没有这个课程')
                break
    def check_course(self):
        print('查看已选课程')
        for course in self.course:
            print(course.name,course.teacher)
    def exit(self):
        f1=open('student_info','rb')
        f2=open('student_info_b','wb')
        while 1:
            try:
                student_obj=pickle.load(f1)
                if student_obj.name == self.name:
                    pickle.dump(self,f2)
                else:
                    pickle.dump(student_obj,f2)
            except EOFError:
                break
        os.remove('student_info')
        os.rename('student_info_b','student_info')
        exit()
    @staticmethod
    def init(name):
        f=open('student_info', 'rb')
        while True:
            try:
                stu_obj = pickle.load(f)
                if stu_obj.name == name:
                    return stu_obj
            except EOFError:
                print('无此学生')
                break