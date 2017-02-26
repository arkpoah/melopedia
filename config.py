import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://[user]:[pass]@localhost/[database_name]?charset=utf8'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# warnings.warn('SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.'
SQLALCHEMY_TRACK_MODIFICATIONS = 'true'

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = '5h_k45=79%#8o+(jyjk#d&2i'

SECRET_KEY = '14jkh*$$1*58gxh+ulja)6(vxk9rn_x8dw^71fpsre#%c1vlv!'

# APPLICATION

PER_PAGE = 30

LASTFM_USER = "[lastfm username]"
LASTFM_API_KEY = "[lastfm api key]"
LASTFM_SECRET = "[lastfm secret]"
