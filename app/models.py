from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class Student(Model):
    __table_args__ = {
        'schema': 'fab'
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    addr = Column(String(50))

    def __repr__(self):
        return '<student %r>' % self.name


class Role(Model):
    __table_args__ = {
        'schema': 'fab'
    }
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    # users = relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.xx


class User(Model):
    __tablename__ = 'users'
    __table_args__ = {
        'schema': 'fab'
    }

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    passwd_hash = Column(String(128))
    # role_id = Column(Integer, ForeignKey('roles.id'))
    email = Column(String(64), unique=True)

    def __repr__(self):
        return '<User %r>' % self.name

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute!')

    @password.setter
    def password(self, password):
        self.passwd_hash = generate_password_hash(password)

