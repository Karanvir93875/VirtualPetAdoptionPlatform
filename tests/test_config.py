class Config(object):
    # General configuration that applies to all environments
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    # Other configurations...

class TestConfig(Config):
    TESTING = True
    # Database URI for testing. Using in-memory SQLite for simplicity
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    # Disable CSRF tokens in the testing configuration
    WTF_CSRF_ENABLED = False
    # Other test-specific configurations...
