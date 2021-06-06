from storages.backends.azure_storage import AzureStorage
import os

class AzureStaticStorage(AzureStorage):
    account_name = os.getenv('AZ_STORAGE_ACCOUNT_NAME')
    account_key = os.getenv('AZ_STORAGE_KEY')
    azure_container = os.getenv('AZ_STORAGE_CONTAINER')
    expiration_secs = None