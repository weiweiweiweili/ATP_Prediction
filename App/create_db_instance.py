from msiapp import db
from msiapp import models

import os
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
db.create_engine(SQLALCHEMY_DATABASE_URI)
