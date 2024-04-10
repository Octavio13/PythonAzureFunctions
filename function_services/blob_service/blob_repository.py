import os, uuid
import asyncio
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import json

# https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-python-get-started?tabs=azure-ad

class BlobConnection:

    #this should be private and readonly
    _current_dir = os.path.dirname(__file__)
    _file_path = os.path.join(_current_dir, "sample_policy.json ")
    _connection_string = ""
    _account_url = "https://fott1995firstblobstorage.blob.core.windows.net" # TODO: Replace <storage-account-name> with your actual storage account name
    _credential = DefaultAzureCredential()


    def __init__(self, connection_string):
        self._connection_string = connection_string



    def get_blob_service_client_token_credential(self):
        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient(self._account_url, credential= self._credential)
        return blob_service_client



    # we will need to use a managed identity
    # more specifically a system-assigned managed identities
    async def initialize_bloc_client(self):
        async with BlobServiceClient(self._account_url, credential= self._credential) as blob_service_client:
            container_client = blob_service_client.get_container_client(container="sample-container")
            return container_client



    def get_containers():
        return ""

    def get_blobs():
        return ""
    
    def get_blob_using_tab():
        return ""



    # Test gets local object
    def get_data(self):
        with open(file = self._file_path, mode = "r") as json_file: # Load JSON data from the file
            data = json.load(json_file)      
        return data
    
    
    

