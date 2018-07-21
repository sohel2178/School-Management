from schoolmodels import DataBase,Course,Subject,Teacher,ClassRoom


if __name__ == '__main__':
    database = DataBase('sqlite:///school.db')

    # database.drop_all()


    # database.update_subject_teacher_id(1,1)
    # database.update_subject_teacher_id(2,2)
    # database.update_subject_teacher_id(3,2)
    # database.update_subject_teacher_id(4,1)

    # database.update_subject_teacher_id(10,1)

    # database.update_subject_classroom_id(1,1)
    # database.update_subject_classroom_id(2,2)
    # database.update_subject_classroom_id(3,3)
    # database.update_subject_classroom_id(4,2)

    # for x in database.get_all_subject():
    #     print(x.name,x.part,x.classroom,x.teacher,x.course.name)

    teac1 = database.get_teacher_by_id(1)

    print(teac1.subjects)


    # Insert Some Class Room

    # classroom1 = ClassRoom(name="A-101")
    # classroom2 = ClassRoom(name="A-102")
    # classroom3 = ClassRoom(name="A-103")
    # classroom4 = ClassRoom(name="A-104")

    # database.add_classroom(classroom1)
    # database.add_classroom(classroom2)
    # database.add_classroom(classroom3)
    # database.add_classroom(classroom4)

    # Add Some Teacher
    # teacher1= Teacher(first_name='Rakib',last_name='Hasan',email='rakib@gmail.com')
    # teacher2= Teacher(first_name='Rohim',last_name='Hasan',email='rhasan@gmail.com')
    # teacher3= Teacher(first_name='Kaju',last_name='Molla')

    # database.add_teacher(teacher1)
    # database.add_teacher(teacher2)
    # database.add_teacher(teacher3)

    # database.delete_course(1)

    # subject1 = Subject(name='Bangla',course_id=1,part='A')
    # subject2 = Subject(name='Bangla',course_id=2,part='A')
    # subject3 = Subject(name='Bangla',course_id=3,part='A')
    # subject4 = Subject(name='English',course_id=1,part='A')
    # subject5 = Subject(name='English',course_id=1,part='B')

    # database.add_subject(subject1)
    # database.add_subject(subject2)
    # database.add_subject(subject3)
    # database.add_subject(subject4)
    # database.add_subject(subject5)

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