from globus_sdk import AuthClient, RefreshTokenAuthorizer
from globuslite.config import set_auth_access_token

app_name = 'globus_lite'

def _update_access_tokens( token_response ):
    tokens = token_response.by_resource_server['auth.globus.org']
    set_auth_access_token( tokens['access_token'], 
                           tokens['expires_at_seconds'])

def get_auth_client():
    tokens = get_auth_tokens()
    authorizer = None

    if tokens['refresh_token'] is not None:
        authorizer = RefreshTokenAuthorizer(
            tokens['refresh_token'], internal_auth_client(),
            tokens['access_token'], tokens['access_token_expires'],
            on_refresh=_update_access_tokens)

    client = AuthClient( authorizer = authorizer, app_name=app_name )
    return client



