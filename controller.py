from flask import Blueprint, render_template, session, redirect, request, url_for
from oauth import OAuthHandler
from utils import parse_credentials
from service import VideoUploadService

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/authorize')
def authorize():
    return redirect(OAuthHandler.get_authorization_url())


@bp.route('/oauth2callback')
def oauth2callback():
    credentials = OAuthHandler.fetch_credentials()
    session['credentials'] = parse_credentials(credentials)
    return redirect(url_for('main.upload_form'))


@bp.route('/upload-form')
def upload_form():
    return render_template('upload_form.html')


@bp.route('/upload', methods=['POST'])
def upload():
    try:
        if 'credentials' not in session:
            return redirect(url_for('main.index'))
        
        service = VideoUploadService(session['credentials'])
        video_id = service.upload_video(request.files['file'], request.form)
        youtube_url = f"https://www.youtube.com/watch?v={video_id}"
        
        return render_template('success.html', title=request.form.get('title'), youtube_url=youtube_url)
    except Exception as e:
        return render_template('error.html', error_message=str(e))
