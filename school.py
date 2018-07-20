from schoolmodels import DataBase,Course,Subject,Teacher


if __name__ == '__main__':
    database = DataBase('sqlite:///school.db')

    # database.drop_all()

    for x in database.get_all_teacher():
        print(x)

    # Add Some Teacher
    # teacher1= Teacher(first_name='Rakib',last_name='Hasan',email='rakib@gmail.com')
    # teacher2= Teacher(first_name='Rohim',last_name='Hasan',email='rhasan@gmail.com')
    # teacher3= Teacher(first_name='Kaju',last_name='Molla')

    # database.add_teacher(teacher1)
    # database.add_teacher(teacher2)
    # database.add_teacher(teacher3)

    # database.delete_course(1)

    # subject1 = Subject(name='Bangla',course_id=1)
    # subject2 = Subject(name='Bangla',course_id=2)
    # subject3 = Subject(name='Bangla',course_id=3)
    # subject4 = Subject(name='English',course_id=1)

    # database.add_subject(subject1)
    # database.add_subject(subject2)
    # database.add_subject(subject3)
    # database.add_subject(subject4)

    # course1 = Course(name='Class One')
    # course2 = Course(name='Class Two')
    # course3 = Course(name='Class Three')
    # course4 = Course(name='Class Four')
    # course5 = Course(name='Class Five')
    # course6 = Course(name='Class Six')
    # course7 = Course(name='Class Seven')
    # course8 = Course(name='Class Eight')
    # course9 = Course(name='Class Nine')
    # course10 = Course(name='Class Ten')

    # database.add_course(course1)
    # database.add_course(course2)
    # database.add_course(course3)
    # database.add_course(course4)
    # database.add_course(course5)
    # database.add_course(course6)
    # database.add_course(course7)
    # database.add_course(course8)
    # database.add_course(course9)
    # database.add_course(course10)