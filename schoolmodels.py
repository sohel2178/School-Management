from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,DateTime,Integer,UniqueConstraint
from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base()


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),unique=True)
    subjects = relationship("Subject",back_populates='course')


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    part = Column(String(4),nullable=False)
    course_id = Column(Integer,ForeignKey('courses.id'))
    course = relationship("Course", back_populates="subjects")
    teacher_id = Column(Integer,ForeignKey('teachers.id'))
    teacher = relationship("Teacher",back_populates='subjects')
    classroom_id = Column(Integer,ForeignKey('classrooms.id'))
    classroom = relationship("ClassRoom",back_populates='subjects')


    __table_args__ = (UniqueConstraint('name','part','course_id',name='subject_course_part'),)

    def __repr__(self):
        return f"{self.name} {self.part} {self.course.name}"







class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    passport_number = Column(String(50))
    race = Column(String(50))
    gender = Column(Integer)
    email = Column(String(50))
    work_phone = Column(Integer)
    cell_phone = Column(Integer)
    subjects = relationship("Subject",back_populates='teacher')

    def __repr__(self):
        return f"< {self.first_name} {self.last_name} {self.email} >"


    



class ClassRoom(Base):
    __tablename__ = 'classrooms'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subjects = relationship("Subject",back_populates="classroom")



    def __repr__(self):
        return f"< id={self.id} {self.name} >"


class DataBase():
    def __init__(self,dbname):
        self.engine = create_engine(dbname)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def drop_all(self):
        Base.metadata.drop_all(self.engine)

    def add_course(self,course):
        self.session.add(course)
        self.session.commit()

    def delete_course(self,course_id):
        course = self.session.query(Course).filter_by(id=course_id).first()
        self.session.delete(course)
        self.session.commit()


    def get_all_course(self):
        return self.session.query(Course).order_by(Course.id).all()


    # SubJECT SECTION

    def add_subject(self,subject):
        self.session.add(subject)
        self.session.commit()

    def get_all_subject(self):
        return self.session.query(Subject).order_by(Subject.id).all()

    def update_subject_teacher_id(self,subject_id,teacher_id):
        try:
            subject = self.session.query(Subject).filter_by(id=subject_id).first()
            subject.teacher_id = teacher_id
            self.session.commit()

        except Exception as e:
            print(str(e))


    def update_subject_classroom_id(self,subject_id,classroom_id):
        try:
            subject = self.session.query(Subject).filter_by(id=subject_id).first()
            subject.classroom_id = classroom_id
            self.session.commit()

        except Exception as e:
            print(str(e))




    # Teacher Section
    def add_teacher(self,teacher):
        self.session.add(teacher)
        self.session.commit()

    def get_all_teacher(self):
        return self.session.query(Teacher).order_by(Teacher.id).all()

    def get_teacher_by_id(self,id):
        return self.session.query(Teacher).filter_by(id=id).first()


    # CLASS ROOM

    def add_classroom(self,classroom):
        self.session.add(classroom)
        self.session.commit()

    def get_all_classroom(self):
        return self.session.query(ClassRoom).order_by(ClassRoom.id).all()

    
