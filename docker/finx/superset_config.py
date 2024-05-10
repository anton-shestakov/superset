import datetime as dt
import json
import os


def get_period_end(to_dttm):
    return dt.datetime.strptime(to_dttm, "%Y-%m-%dT%H:%M:%S") - dt.timedelta(days=1)


JINJA_CONTEXT_ADDONS = {
    "period_end": get_period_end,
}

ROW_LIMIT = os.getenv("ROW_LIMIT", 5000)

# Your App secret key
SECRET_KEY = os.getenv("SECRET_KEY")

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

DATA_CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 60 * 60 * 24,  # 1 day default (in secs)
    "CACHE_KEY_PREFIX": "superset_results",
    "CACHE_REDIS_URL": os.getenv("CACHE_REDIS_URL", "redis://redis:6379/1"),
}

ENABLE_PROXY_FIX = True
HTTP_HEADERS = {}
ENABLE_ROW_LEVEL_SECURITY = True

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

TALISMAN_ENABLED = True
TALISMAN_CONFIG = {
    "content_security_policy": {
        "style-src": ["'self'", "'unsafe-inline'"],
        "script-src": ["'self'", "'unsafe-eval'", "'unsafe-inline'"],
        "img-src": ["'self'", "data:"],
        "default-src": "'self'",
        "object-src": "'none'",
        "connect-src": ["'self'"],
        "frame-ancestors": json.loads(os.getenv("FINX_CLIENT_DOMAINS", "\"'none'\"")),
    },
}
