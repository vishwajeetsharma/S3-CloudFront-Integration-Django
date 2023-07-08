from storages.backends.s3boto3 import S3Boto3Storage, S3StaticStorage


class MediaStorage(S3Boto3Storage):
    bucket_name = 'wearebuddiesdjangotest'
    custom_domain = 'cdn.wearebuddies.club'

class StaticStorage(S3StaticStorage):
    bucket_name = 'testassestforwearebuddies'
    custom_domain = 'assets.wearebuddies.club'