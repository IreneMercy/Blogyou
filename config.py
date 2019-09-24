class Config:
    Debug = True
    SECRET_KEY= '4444'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joozao:12345@localhost/blogyu'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME='ijanemercy@gmail.com'
    MAIL_PASSWORD='@janeMercy700'


class DevConfig(Config):
    Debug = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joozao:12345@localhost/blogyu'

configurations = {"development":DevConfig, "production":ProdConfig}
