from cloudinary_storage.storage import MediaCloudinaryStorage, StaticHashedCloudinaryStorage

class PatchedMediaCloudinaryStorage(MediaCloudinaryStorage):
    def _save(self, name, content):
        try:
            return super()._save(name, content)
        except KeyError:
            # fallback when etag is missing
            return name

class PatchedStaticCloudinaryStorage(StaticHashedCloudinaryStorage):
    def _save(self, name, content):
        try:
            return super()._save(name, content)
        except KeyError:
            return name
