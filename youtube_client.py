from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials


class YouTubeClient:
    def __init__(self, credentials_dict):
        creds = Credentials(**credentials_dict)
        self.client = build('youtube', 'v3', credentials=creds)
    
    def upload_video(self, file_path, title, description, privacy_status, made_for_kids, publish_at=None):
        body = {
            "snippet": {
                "title": title,
                "description": description,
                "categoryId": "22"
            },
            "status": {
                "privacyStatus": privacy_status,
                "selfDeclaredMadeForKids": made_for_kids
            }
        }
        
        if privacy_status == 'private' and publish_at:
            body["status"]["publishAt"] = publish_at
        
        media = MediaFileUpload(file_path, resumable=True)
        request_upload = self.client.videos().insert(
            part="snippet,status",
            body=body,
            media_body=media
        )
        
        response = request_upload.execute()
        
        if hasattr(media, '_fd'):
            media._fd.close()
        
        return response['id']
