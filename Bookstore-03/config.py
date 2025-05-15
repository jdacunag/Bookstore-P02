import os

# Usando variables de entorno para configuración
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secretkey')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'mysql+pymysql://bookstore_user:bookstore_pass@db/bookstore')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', 'False') == 'True'