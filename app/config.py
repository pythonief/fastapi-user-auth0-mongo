import json

with open('secret.json') as f:
    secret = json.loads(f.read())


MONGODB_USERNAME = secret.get('MONGODB_USERNAME')
MONGODB_PASSWORD = secret.get('MONGODB_PASSWORD')
MONGODB_DB_NAME = secret.get('MONGODB_DB_NAME')

GOOGLE_API_URL = 'https://www.googleapis.com/'
GOOGLE_METADATA_URL = 'https://accounts.google.com/.well-known/openid-configuration'
GOOGLE_CLIENT_SCOPE = {
    'scope': 'openid email profile'
}

DB_CONFIG = {
    "DB_URI": f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@sandbox.iw33d.mongodb.net/{MONGODB_DB_NAME}?retryWrites=true&w=majority"
}
