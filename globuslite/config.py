import yaml
import os.path
from globuslite import version


CONFIG_FILE = '~/.globus-lite.yaml'
CONFIG_PATH = os.path.expanduser( CONFIG_FILE )
AUTH_RT_OPTNAME = 'auth_refresh_token'
AUTH_AT_OPTNAME = 'auth_access_token'
AUTH_AT_EXPIRES_OPTNAME = 'auth_access_token_expires'
TRANSFER_RT_OPTNAME = 'transfer_refresh_token'
TRANSFER_AT_OPTNAME = 'transfer_access_token'
TRANSFER_AT_EXPIRES_OPTNAME = 'transfer_access_token_expires'

app_name = 'globuslite'
CLIENT_ID = '257aa35a-4619-4806-80eb-e8751380a206'

def get_conf():

    try:
        with open( CONFIG_PATH, 'r' ) as f:
            config = yaml.safe_load(f)
        return config
    
    except FileNotFoundError:
        with open( CONFIG_PATH, 'w' ) as f:
            yaml.dump( {}, f )

        return {}

def lookup_option( option ):
    try:
        return get_conf()[option]
    except KeyError:
        return None

def write_option( opt, val ):

    config = get_conf()
    config[opt] = val

    with open( CONFIG_PATH, 'w' ) as f:
        yaml.dump( config, f, default_flow_style=False )

def get_auth_tokens():
    path = os.path.expanduser( CONFIG_FILE )

    config = get_conf()

    return {
        'refresh_token': lookup_option(AUTH_RT_OPTNAME) , 
        'access_token': lookup_option(AUTH_AT_OPTNAME),
        'access_token_expires': lookup_option(AUTH_AT_EXPIRES_OPTNAME)
    }

def set_auth_access_token( token, expires_at ):
    write_option( AUTH_AT_OPTNAME, token)
    write_option( AUTH_AT_EXPIRES_OPTNAME, expires_at )

def internal_auth_client():
    return globus_sdk.NativeAppAuthClient( CLIENT_ID, app_name = version.app_name )
