from __init__ import CONN, CURSOR
from department import Department
import pytest


class TestDepartment:
    '''Class Department in department.py'''

    @pytest.fixture(autouse=True)
    def drop_tables(self):
        '''drop tables prior to each test.'''

        
        CURSOR.execute("DROP TABLE IF EXISTS departments")
        Department.all = {}

    def test_creates_table(self):
        '''contains method "create_table()" that creates table "departments" if it does not exist.'''

        
        

    def test_drops_table(self):
        '''contains method "drop_table()" that drops table "departments" if it exists.'''

        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

       

        sql_table_names = """
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='departments'
        """
        result = CURSOR.execute(sql_table_names).fetchone()
        

    def test_saves_department(self):
        '''contains method "save()" that saves a Department instance to the db and assigns the instance an id.'''

       
        department = Department("Payroll", "Building A, 5th Floor")
        

        sql = """
            SELECT * FROM departments
        """
        
       
        (department.id, department.name, department.location) 
        
    def test_creates_department(self):
        '''contains method "create()" that creates a new row in the db using parameter data and returns a Department instance.'''

       
        

        sql = """
            SELECT * FROM departments
        """
        
       
       
        

    def test_updates_row(self):
        '''contains a method "update()" that updates an instance's corresponding db row to match its new attribute values.'''
        

        
       
        department2 = Department.create("Marketing", "Building B, 3rd Floor")
        id2 = department2.id

        # Assign new values for name and location
        department2.name = "Sales and Marketing"
        department2.location = "Building B, 4th Floor"

        # Persist the updated name and location values
       

        # assert department1 row was not updated, department1 object state not updated
        # assert row not updated
        
       
        # assert department2 row was updated, department2 object state is correct
       
        
    def test_deletes_row(self):
        '''contains a method "delete()" that deletes the instance's corresponding db row'''
        

        
       
        department2 = Department.create(
            "Sales and Marketing", "Building B, 4th Floor")
        id2 = department2.id

        

        # assert department1 row was not deleted, department1 object state is correct
        
       
        # assert department2 row is deleted
      
        # assert department2 object state is correct, id should be None
        assert ((None, "Sales and Marketing", "Building B, 4th Floor")
                == (department2.id, department2.name, department2.location))
        # assert dictionary entry was deleted
        assert(Department.all.get(id2) is None)

    def test_instance_from_db(self):
        '''contains method "instance_from_db()" that takes a table row and returns a Department instance.'''

        
      
        sql = """
            SELECT * FROM departments
        """
      
       

        
    def test_gets_all(self):
        '''contains method "get_all()" that returns a list of Department instances for every row in the db.'''

        

        
        department2 = Department.create("Marketing", "Building B, 3rd Floor")

        

       
       

    def test_finds_by_id(self):
        '''contains method "find_by_id()" that returns a Department instance corresponding to the db row retrieved by id.'''

        
        
        department2 = Department.create("Marketing", "Building B, 3rd Floor")

        
       
       
       
        
    def test_finds_by_name(self):
        '''contains method "find_by_name()" that returns a Department instance corresponding to the db row retrieved by name.'''

      
       
            
        department2 = Department.create("Marketing", "Building B, 3rd Floor")

        
        
        
        
        

    def test_get_employees(self):
        '''contain a method "employees" that gets the employees for the current Department instance '''

        from employee import Employee  # avoid circular import issue
        Employee.all = {}

        
       
        department2 = Department.create(
            "Human Resources", "Building C, 2nd Floor")

        Employee.create_table()
        
        
        employee3 = Employee.create("Amir", "Manager", department2.id)

       
      