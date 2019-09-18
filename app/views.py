from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, expose, has_access
from .models import Student, User, Role
from . import appbuilder, db

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""


class New(ModelView):
    datamodel = SQLAInterface(Student)


class UserManage(ModelView):
    datamodel = SQLAInterface(User)


class RoleManage(ModelView):
    datamodel = SQLAInterface(Role)


appbuilder.add_view(New, "学生", icon="gear", category='学生管理',)
appbuilder.add_view(UserManage, "用户管理", icon="gear", category='用户管理',)
appbuilder.add_view(RoleManage, "角色管理", icon="gear", category='角色管理',)
# add_link会重复添加链接，add_view也一样

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
