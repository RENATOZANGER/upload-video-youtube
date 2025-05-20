import os
from youtube_client import YouTubeClient
from utils import format_publish_datetime


class VideoUploadService:
    
    def __init__(self, credentials):
        self.client = YouTubeClient(credentials)
    
    def upload_video(self, file, form_data):
        title = form_data.get('title', 'Vídeo via API')
        description = form_data.get('description', 'Enviado com Flask + YouTube API')
        privacy_status = form_data.get('privacyStatus', 'private')
        made_for_kids = form_data.get('madeForKids', 'false') == 'true'
        publish_at_input = form_data.get('publishAt')
        
        publish_at = format_publish_datetime(publish_at_input) if publish_at_input else None
        
        temp_path = f"temp_{file.filename}"
        file.save(temp_path)
        
        try:
            video_id = self.client.upload_video(
                file_path=temp_path,
                title=title,
                description=description,
                privacy_status=privacy_status,
                made_for_kids=made_for_kids,
                publish_at=publish_at
            )
            return video_id
        finally:
            os.remove(temp_path)
