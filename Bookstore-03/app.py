from flask import Flask, render_template
from extensions import db, login_manager
from models.user import User

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Luego importar blueprints
from controllers.auth_controller import auth
from controllers.book_controller import book
from controllers.purchase_controller import purchase
from controllers.payment_controller import payment
from controllers.delivery_controller import delivery
from controllers.admin_controller import admin

# Registrar blueprints
app.register_blueprint(auth)
app.register_blueprint(book, url_prefix='/book')
app.register_blueprint(purchase)
app.register_blueprint(payment)
app.register_blueprint(delivery)
app.register_blueprint(admin)

from models.delivery import DeliveryProvider

def initialize_delivery_providers():
    with app.app_context():
        if DeliveryProvider.query.count() == 0:
            providers = [
                DeliveryProvider(name="DHL", coverage_area="Internacional", cost=50.0),
                DeliveryProvider(name="FedEx", coverage_area="Internacional", cost=45.0),
                DeliveryProvider(name="Envia", coverage_area="Nacional", cost=20.0),
                DeliveryProvider(name="Servientrega", coverage_area="Nacional", cost=15.0),
            ]
            db.session.bulk_save_objects(providers)
            db.session.commit()

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    # Esperar a que la base de datos esté lista
    import time
    import pymysql
    
    print("Esperando a que la base de datos MySQL esté disponible...")
    max_attempts = 30
    for attempt in range(max_attempts):
        try:
            conn = pymysql.connect(
                host='db',
                user='bookstore_user',
                password='bookstore_pass',
                database='bookstore',
                connect_timeout=5
            )
            conn.close()
            print("Base de datos conectada exitosamente!")
            break
        except pymysql.err.OperationalError as e:
            print(f"Intento {attempt+1}/{max_attempts}: Base de datos no disponible, esperando 2 segundos...")
            time.sleep(2)
    else:
        print("No se pudo conectar a la base de datos después de varios intentos.")
        print("Intentando crear tablas de todos modos...")
    
    # Crear tablas e inicializar datos
    with app.app_context():
        db.create_all()
        initialize_delivery_providers()
    
    # Iniciar la aplicación Flask
    app.run(host="0.0.0.0", debug=True)