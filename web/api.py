from flask import Flask, request, jsonify
from flask.views import MethodView
from web.api_config import api, app, blueprint
from schema.schema import EmployeeArgumentSchema
from db.models import Employee, Department, Project, Base
from db.db_settings import session, engine


@blueprint.route('/employees/<eid>')
class EmployeeResource(MethodView):
    def get(self):
        ''' Get an employee by eid '''

@blueprint.route('/employees')
class EmployeesResource(MethodView):
    def get(self):
        ''' Get list of Employees '''

    @blueprint.arguments(EmployeeArgumentSchema, location='files')
    #@blueprint.response(201)
    def post(self, args):
        ''' Add an Employee '''
        e = Employee(
            id = request.form.get('id'),
            ename = request.form.get('employee_name'),
            edept = request.form.get('employee_department')
        )
        session.add(e)
        session.commit()
        session.close()
        return jsonify({'Status': 'Created'}), 201

    def delete(self):
        ''''''

api.register_blueprint(blueprint)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=False)
