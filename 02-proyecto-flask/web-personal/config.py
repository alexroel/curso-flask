class Config:
    #Configuracion base
    DEBUG = True
    TESTING  = True

    #Configuración de Base de Datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/my_webpersonal"

class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING  = True
