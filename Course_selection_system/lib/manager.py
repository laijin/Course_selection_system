from people import *
from course import *
from teacher import *
from student import *
import pickle
class Manager(People):
    action=['info_courses','create_course','create_people','info_student','info_student_course','exit']
    def __init__(self,name):
        self.name=name
    def create_course(self):
        print('创建课程')
        course_name=input('课程名称')
        money=input('价钱')
        cyc=input('周期')
        teacher=input('老师')
        place=input('地点')
        course_obj=Course(course_name,money,cyc,teacher,place)
        f=open('course_info','ab')
        pickle.dump(course_obj,f)
        print('%s课程创建成功'%course_obj.name)
    def create_people(self):
        people=input('输入Student或Teacher')
        p=people+'_info'
        people_name=input('名称')
        people_pwd=input('密码')
        people_str='%s|%s|%s\n'%(people_name,people_pwd,people)
        if people == 'Student':
            people_obj = Student(people_name)
        elif people == 'Teacher':
            people_obj = Teacher(people_name)
        f1=open('userinfo','a',encoding='utf-8')
        f1.write(people_str)
        f2=open(p,'ab')
        pickle.dump(people_obj,f2)
        print('%s创建成功'%people_obj.name)
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
    def info_student_course(self):
        print('查看学生课程')
        f=open('student_info','rb')
        while 1:
            try:
                student_obj = pickle.load(f)
                course_name = [course.name for course in student_obj.course]
                print(student_obj.name,'所选课程%s'%'|'.join(course_name))
            except EOFError:
                break
    def exit(self):
        exit()
    @classmethod
    def init(cls,name):
        return cls(name)