import os


class Config:
    SECRET_KEY = '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'
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
    CLIENT_SECRET_FILE = 'client_secret.json'
    REDIRECT_URI = 'http://localhost:5000/oauth2callback'
    LOCAL_TZ = 'America/Sao_Paulo'


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
