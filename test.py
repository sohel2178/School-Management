from models import User,DataBase
import random

# print('Hello')

name_list= ['Sohel','Shakil','Arham','Rashin','Putul','Sumi','Sajib','Redwan']
lastname_list= ['Ahmed','Mahmud','Khan','Sikdar','Rahman','Biswas','Moin']



def create_user(n):
    user_list =[]
    for i in range(n):
        user ={}
        name = name_list[random.randrange(0,len(name_list))]
        lastname = lastname_list[random.randrange(0,len(lastname_list))]

        user['name']=name
        user['fullname']=name+" "+lastname
        user['password']='123456'

        user_list.append(user)

    return user_list









if __name__ == "__main__":
    # print('Hello')
    database = DataBase('sqlite:///mydb.db')
    # database.drop_all()

    # userList = create_user(30)
    
    # user = User(name='Sohel',fullname='Sohel Ahmed',password='s0201078')
    # database.add_user(user)

    # for x in userList:
    #     user = User(name=x['name'],fullname=x['fullname'],password=x['password'])
    #     database.add_user(user)

    # for x in database.get_all_user():
    #     print(x,x.addresses)



    # get All User Whose Name is Sohel

    # for x in database.get_users_by_name('Shail'):
    #     print(x)

    

    # get All User Whose Name is Sohel and Shakil

    # for x in database.get_users_by_names(['Sohel','Shakil']):
    #     print(x)


    # get First 5 User

    # for x in database.get_users_by_limit(5):
    #     print(x,x.id)

    # get All User Except Sohel

    # for x in database.get_all_users_not_equal_name('Sohel'):
    #     print(x,x.id)



    # get All User Like S

    # for x in database.get_all_like_users('%S%'):
    #     print(x,x.id)

    # for x in database.get_users_by_limit(5):
    #     print(x,x.id)

    # database.drop_all()


    print(database.get_user_by_id(1).addresses)



