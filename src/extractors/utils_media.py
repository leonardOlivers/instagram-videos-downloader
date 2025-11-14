thonpython
def generate_media_object(media_id: str, video_url: str, quality: str, extension: str):
    return {
        "id": media_id,
        "url": video_url,
        "quality": quality,
        "type": "video",
        "extension": extension,
    }