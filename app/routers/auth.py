from os import access
from authlib.integrations import starlette_client
from dotenv import dotenv_values, find_dotenv
from fastapi import APIRouter, status
from starlette.requests import Request
import requests

config = dotenv_values(find_dotenv())

AUTH0_CLIENT_ID = 'AUTH0_CLIENT_ID'
AUTH0_CLIENT_SECRET = 'AUTH0_CLIENT_SECRET'
AUTH0_CALLBACK_URL = 'AUTH0_CALLBACK_URL'
AUTH0_DOMAIN = 'AUTH0_DOMAIN'
AUTH0_AUDIENCE = 'AUTH0_AUDIENCE'
PROFILE_KEY = 'profile'
AUTH0_GRANT_TYPE = 'authorization_code'
SECRET_KEY = 'ThisIsTheSecretKey'
JWT_PAYLOAD = 'jwt_payload'
API_BASE_URL = 'https://fritzlerilan.us.auth0.com'
ACCESS_TOKEN_URL = 'https://fritzlerilan.us.auth0.com/oauth/token'
AUTHORIZE_URL = 'https://fritzlerilan.us.auth0.com/authorize'
CLIENT_KWARGS = {'scope': 'openid profile email'}

router = APIRouter()


@router.get('/callback')
async def callback_handling(request: Request):
    code = request.query_params.get('code')
    state = request.query_params.get('state')

    response = requests.post(
        url = ACCESS_TOKEN_URL,
        
        data=dict(
            grant_type=AUTH0_GRANT_TYPE,
            client_id=config.get(AUTH0_CLIENT_ID),
            client_secret=config.get(AUTH0_CLIENT_SECRET),
            code=code,
            redirect_uri = 'http://localhost:8000',
            state = state,
        )
    )
    if not response.status_code == status.HTTP_200_OK:
        return 'authentication error', 400

    token = response.json().get('access_token')
    token_type = response.json().get('token_type')
    id_token = response.json().get('id_token')
    exp = response.json().get('expires_in')
    scope = response.json().get('scope')

    response = response.json()
    return response
        
    

    """response = requests.post(ACCESS_TOKEN_URL, client_id=config.get(
        AUTH0_CLIENT_ID), client_secret=config.get(AUTH0_CLIENT_SECRET), otp = requests.code, )
"""
