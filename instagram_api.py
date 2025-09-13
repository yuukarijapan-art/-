import requests
GRAPH = "https://graph.facebook.com/v21.0"

class IGClient:
    def __init__(self, access_token: str, ig_business_id: str):
        self.access_token = access_token
        self.ig_business_id = ig_business_id

    def create_media(self, image_url: str, caption: str):
        url = f"{GRAPH}/{self.ig_business_id}/media"
        payload = {"image_url": image_url, "caption": caption, "access_token": self.access_token}
        r = requests.post(url, data=payload, timeout=30)
        r.raise_for_status()
        return r.json()

    def publish_media(self, creation_id: str):
        url = f"{GRAPH}/{self.ig_business_id}/media_publish"
        payload = {"creation_id": creation_id, "access_token": self.access_token}
        r = requests.post(url, data=payload, timeout=30)
        r.raise_for_status()
        return r.json()
