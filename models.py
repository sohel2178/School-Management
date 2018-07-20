from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,DateTime,Integer
from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    addresses = relationship("Address",back_populates='user')

    def __repr__(self):
         return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer,ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


class DataBase():
    def __init__(self,dbname):
        print('Hello')
        self.engine = create_engine(dbname)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def add_user(self,user):
        self.session.add(user)
        self.session.commit()

    def get_all_user(self):
        return self.session.query(User).all()

    def get_user_by_id(self,id):
        return self.session.query(User).filter_by(id=id).first()

    def get_users_by_name(self,name):
        return self.session.query(User).filter_by(name=name).all()

    def get_users_by_names(self,nameList):
        return self.session.query(User).filter(User.name.in_(nameList)).all()

    def get_users_by_limit(self,number,descending=False):

        if descending:
            return self.session.query(User).order_by(User.id.desc())[:number]

        return self.session.query(User).order_by(User.id)[:number]

    # Not Equal Query
    def get_all_users_not_equal_name(self,name):
        return self.session.query(User).filter(User.name != name)

    def get_all_like_users(self,like):
        return self.session.query(User).filter(User.name.like(like))


    def drop_all(self):
        Base.metadata.drop_all(self.engine)


    def add_address(self,user_id,email):
        address = Address(user_id=user_id,email_address=email)
        self.session.add(address)
        self.session.commit()


