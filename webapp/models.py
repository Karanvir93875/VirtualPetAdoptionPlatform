from . import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    
    # Additional fields and methods as needed
    
    def __repr__(self):
        return f'<Pet {self.name}>'
