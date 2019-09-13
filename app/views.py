from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, expose, has_access

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


# 类似于蓝图的概念
class MyView(BaseView):
    default_view = "method1"

    @expose('/method1/')
    @has_access
    def method1(self):
        return 'hello'

    @expose('/method2/<string:param1>')
    @has_access
    def method2(self, param1):

        return 'goodbye %s' % param1


appbuilder.add_view(
    MyView, "method1", category="my view",

)

appbuilder.add_link("method2", href='myview/method2/john', category='my view')

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
