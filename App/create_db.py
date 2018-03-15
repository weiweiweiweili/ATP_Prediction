from msiapp import db
from msiapp import models


# Creates a table in the database provided as the 'SQLALCHEMY_DATABASE_URI'
# configuration parameter in __init__.py with the schema defined by models.Track()
def create_db():
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    create_db()
