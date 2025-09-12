from cloudinary_storage.storage import MediaCloudinaryStorage

class PatchedMediaCloudinaryStorage(MediaCloudinaryStorage):
    """
    Fix for django-cloudinary-storage==0.3.0 etag bug.
    Falls back gracefully if `etag` is missing from Cloudinary response.
    """
    def _save(self, name, content):
        saved_name = super()._save(name, content)
        # Ensure Cloudinary's API response won't break Django's pipeline
        if not hasattr(self, "_entries"):
            self._entries = {}
        self._entries[name] = {"etag": None}
        return saved_name
