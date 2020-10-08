from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.db_settings import engine, session

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    ename = Column(String)
    edept = Column(String, ForeignKey('department.deptid'))

    def __repr__(self):
        return f' Employee: {self.ename}, Id: {self.id}, Department: {self.edept}'

class Department(Base):
    __tablename__ = 'department'
    deptid = Column(String, primary_key=True)
    deptname = Column(String)

    def __repr__(self):
        return f' Department: {self.deptname}, Id: {self.deptid}'

class Project(Base):
    __tablename__ = 'project'
    pid = Column(String, primary_key=True)
    pname = Column(String)

    def __repr__(self):
        return f' Project: {self.pname}, Id: {self.pid}'

def create_all_tables():
    ''' Creates all the tables '''
    Base.metadata.create_all(engine)

def drop_all_tables():
    ''' Drop all tables '''
    Base.metadata.drop_all(engine)

'''if __name__ == '__main__':
    #drop_all_tables()
    #create_all_tables()
    e = Department(
        deptid = 'SD',
        deptname = 'Software Development'
    )
    session.add(e)
    session.commit()
    session.close()'''