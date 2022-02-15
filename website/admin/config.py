class Config(object):
    pass


class ProductionConfig(Config):
    DATABASE_URI = "sqlite:///database.sqlite"


class DevelopmentConfig(Config):
    DATABASE_URI = "sqlite:///database.sqlite"
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
