from . import db 

class Properties(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    bedrooms = db.Column(db.String(10))
    bathrooms = db.Column(db.String(10))
    location = db.Column(db.String(255))
    price = db.Column(db.String(50))
    property_type = db.Column(db.String(25))
    description = db.Column(db.String(600))
    filename = db.Column(db.String(255))

    def __init__(self, title, bedrooms, bathrooms, location, price, property_type, description, filename):
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.property_type = property_type
        self.description = description
        self.filename = filename
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.title)
