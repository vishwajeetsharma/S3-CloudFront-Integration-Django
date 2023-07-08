from storages.backends.s3boto3 import S3Boto3Storage, S3StaticStorage
from django.conf import settings


def setting(name, default=None):
    return getattr(settings, name, default)

class MediaStorage(S3Boto3Storage):
    bucket_name = 'wearebuddiesdjangotest'
    custom_domain = 'cdn.wearebuddies.club'

class StaticStorage(S3StaticStorage):
    bucket_name = 'testassestforwearebuddies'
    custom_domain = 'assets.wearebuddies.club'
    object_parameters: setting('AWS_S3_STATIC_OBJECT_PARAMETERS', {})