def login():
    username = input("用户名:")
    password = input("密码:")
    f=open('userinfo',encoding='utf-8')
    try:
        for line in f:
            name,pwd,identify=line.strip().split('|')
            if username == name and password == pwd:
                return {'user_status':True,'name':username,'id':identify}
        else:
            print('..')
            return {'user_status':False, 'name': username}
    except ValueError:
        print('无此人或密码错误')