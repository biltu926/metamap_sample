from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'emloyee'
    id = Column(Integer, primary_key=True)
    ename = Column(String)
    edept = Column(String, ForeignKey('department.deptid'))

class Department(Base):
    __tablename__ = 'department'
    deptid = Column(Integer, primary_key=True)
    deptname = Column(String)

class Project(Base):
    __tablename__ = 'project'
    pid = Column(String)