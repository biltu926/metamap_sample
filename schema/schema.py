from marshmallow import Schema, fields, ValidationError

class EmployeeArgumentSchema(Schema):
    id = fields.String()
    employee_name = fields.String()
    employee_department = fields.String()

class DepartmentArgumentSchema(Schema):
    department_id = fields.String()
    department_name = fields.String()

class ProjectArgumentSchema(Schema):
    project_id = fields.String()
    project_name = fields.String()
