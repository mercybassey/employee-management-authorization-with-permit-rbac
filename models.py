from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Department(db.Model):
    __tablename__ = 'departments'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)  
    employees = db.relationship('Employee', backref='department', lazy=True)  

class Employee(db.Model): 
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    start_year = db.Column(db.Integer, nullable=False)
    hobbies = db.Column(db.String(200))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)


    