from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,DateTime,Integer
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
    name = Column(String(50))
    course_id = Column(Integer,ForeignKey('courses.id'))
    course = relationship("Course", back_populates="subjects")
    teacher_id = Column(Integer,ForeignKey('teachers.id'))
    teacher = relationship("Teacher",back_populates='subjects')

    def __repr__(self):
        return f"{self.name} {self.course.name}"







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
    teachers = Column(String)
    subjects = Column(String)


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

    def add_subject(self,subject):
        self.session.add(subject)
        self.session.commit()

    def get_all_subject(self):
        return self.session.query(Subject).order_by(Subject.id).all()


    # Teacher Section
    def add_teacher(self,teacher):
        self.session.add(teacher)
        self.session.commit()

    def get_all_teacher(self):
        return self.session.query(Teacher).order_by(Teacher.id).all()

    
