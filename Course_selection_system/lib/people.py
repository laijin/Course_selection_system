import pickle
class People:
    def __init__(self,name):
        self.name=name
    def info_courses(self):
        f=open('course_info','rb')
        count=0
        while 1:
            try:
                count+=1
                course_obj=pickle.load(f)
                print(count,course_obj.name,course_obj.money,course_obj.teacher)
            except EOFError:
                print('--------')
                break


