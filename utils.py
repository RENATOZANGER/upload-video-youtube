from datetime import datetime
import pytz
from config import Config


def parse_credentials(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }


def format_publish_datetime(local_str):
    local_dt = datetime.strptime(local_str, '%Y-%m-%dT%H:%M')
    local_tz = pytz.timezone(Config.LOCAL_TZ)
    utc_dt = local_tz.localize(local_dt).astimezone(pytz.utc)
    return utc_dt.isoformat().replace('+00:00', 'Z')
