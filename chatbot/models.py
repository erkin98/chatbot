from chatbot import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f'{self.sender}'
