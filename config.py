class Config(object):
    """
    nanti di setting
    """


class DevelopmentConfig(Config):
    
    DEBUG = True
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):

    DEBUG = False


app_config = {

    'development':DevelopmentConfig,
    'production':ProductionConfig
}