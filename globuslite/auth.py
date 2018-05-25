import re
from globus_sdk import AuthClient, RefreshTokenAuthorizer
from globuslite.config import set_auth_access_token, get_auth_tokens
from globuslite.version import app_name

# what qualifies as a valid Identity Name?
_IDENTITY_NAME_REGEX = '^[a-zA-Z0-9]+.*@[a-zA-z0-9-]+\..*[a-zA-Z]+$'


def is_valid_identity_name(identity_name):
    """
    Check if a string is a valid identity name.
    Does not do any preprocessing of the identity name, so you must do so
    before invocation.
    """
    if re.match(_IDENTITY_NAME_REGEX, identity_name) is None:
        return False
    else:
        return True

def verify_identity_name( id_name ):
    '''
    Throw an exception if id_name is not valid. Else, return id_name
    unchanged.
    '''

    if is_valid_identity_name( id_name ):
        return id_name
    else:
        raise RuntimeError('Invalid Globus identifier.')

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



