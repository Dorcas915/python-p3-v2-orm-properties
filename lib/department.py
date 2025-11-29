from __init__ import CURSOR, CONN

class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    # ----------- NAME PROPERTY ----------------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if len(value.strip()) == 0:
            raise ValueError("Name must be at least 1 character.")
        self._name = value

    # ----------- LOCATION PROPERTY ----------------
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise ValueError("Location must be a string.")
        if len(value.strip()) == 0:
            raise ValueError("Location must be at least 1 character.")
        self._location = value

    # ----------- DATABASE METHODS ----------------
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS departments"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
        INSERT INTO departments (name, location)
        VALUES (?, ?)
        """
       
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, location):
        dept = cls(name, location)
       
        return dept

    def update(self):
        sql = """
        UPDATE departments
        SET name = ?, location = ?
        WHERE id = ?
        """
        
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM departments WHERE id = ?"
        
        CONN.commit()
        self.id = None
