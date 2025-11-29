from department import Department
from employee import Employee
import pytest


class TestEmployeeProperties:
    '''Class Employee in employee.py'''

    @pytest.fixture(autouse=True)
    def reset_db(self):
        '''drop and recreate tables prior to each test.'''
        Employee.drop_table()
        
        Employee.create_table()
        
        # clear the object cache
        Department.all = {}
        Employee.all = {}

    
        '''validates name, job title, department id are valid'''
        # should not raise exception
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Lee", "Manager", department.id)

    
        '''validates name property is assigned a string'''
        
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Lee", "Manager", department.id)
        employee.name = 7

    def test_name_string_length(self):
        '''validates name property length > 0'''
       
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Lee", "Manager", department.id)
            

    def test_location_is_string(self):
        '''validates job_title property is assigned a string'''
        
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Lee", "Manager", department.id)
        employee.job_title = 7

    def test_location_string_length(self):
        '''validates job_title property length > 0'''
        
        department = Department.create("Payroll", "Building A, 5th Floor")
        employee = Employee.create("Lee", "Manager", department.id)
        employee.job_title = ''

    def test_department_property(self):
        department = Department.create("Payroll", "Building C, 3rd Floor")
        employee = Employee.create(
            "Raha", "Accountant", department.id)  # no exception

    def test_department_property_fk(self):
        
            Employee.create("Raha", "Accountant", 7)

    def test_department_property_type(self):
        
            employee = Employee.create("Raha", "Accountant", "abc")
