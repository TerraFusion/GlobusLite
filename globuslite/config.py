import yaml
import os.path.expanduser
from globuslite import version


CONFIG_FILE = '~/.globus-lite.yaml'
AUTH_RT_OPTNAME = 'auth_refresh_token'
AUTH_AT_OPTNAME = 'auth_access_token'
AUTH_AT_EXPIRES_OPTNAME = 'auth_access_token_expires'
app_name = 'globuslite'
CLIENT_ID = '257aa35a-4619-4806-80eb-e8751380a206'

def write_option( opt, val ):
    path = os.path.expanduser( CONFIG_FILE )

    with open( path, 'r' ) as f:
        config = yaml.safe_load(f)

    config[opt] = val

    with open( path, 'w' ) as f:
        yaml.dump( config, f )

def get_auth_tokens():
    path = os.path.expanduser( CONFIG_FILE )

    with open( path, 'r' ) as f:
        config = yaml.safe_load( f )

    return {
        'refresh_token': config[ AUTH_RT_OPTNAME ], 
        'access_token': config[ AUTH_AT_OPTNAME],
        'access_token_expires': config[ AUTH_AT_EXPIRES_OPTNAME ]
    }

def set_auth_access_token( token, expires_at ):
    write_option( AUTH_AT_OPTNAME, token)
    write_option( AUTH_AT_EXPIRES_OPTNAME, expires_at )

def internal_auth_client():
    return globus_sdk.NativeAppAuthClient( CLIENT_ID, app_name = version.app_name )
