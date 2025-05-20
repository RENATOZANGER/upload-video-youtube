from google_auth_oauthlib.flow import Flow
from flask import session, request, url_for
from config import Config


class OAuthHandler:
    
    @staticmethod
    def get_flow(state=None):
        return Flow.from_client_secrets_file(
            Config.CLIENT_SECRET_FILE,
            scopes=Config.SCOPES,
            state=state,
            redirect_uri=Config.REDIRECT_URI
        )
    
    @staticmethod
    def get_authorization_url():
        flow = OAuthHandler.get_flow()
        auth_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )
        session['state'] = state
        return auth_url
    
    @staticmethod
    def fetch_credentials():
        flow = OAuthHandler.get_flow(session['state'])
        flow.fetch_token(authorization_response=request.url)
        return flow.credentials
