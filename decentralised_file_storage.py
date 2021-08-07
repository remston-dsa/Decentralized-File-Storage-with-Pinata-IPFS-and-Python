import ipfshttpclient
import sys

PINATA_API_KEY='0ab158d03276afd590d5'
PINATA_API_SECRET='e8f92aba954c0efad91fab5297b71fe9ef23494e0ef9a1445d5e9584f49f2825'
JWT='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiIyNzlkNmVhNi1jZTU1LTRjNWYtYmZlNS1kNTRhMTk3ZjM1ZDkiLCJlbWFpbCI6InJlbXN0b25kc2E3QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImlkIjoiTllDMSIsImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxfV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2V9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiIwYWIxNThkMDMyNzZhZmQ1OTBkNSIsInNjb3BlZEtleVNlY3JldCI6ImU4ZjkyYWJhOTU0YzBlZmFkOTFmYWI1Mjk3YjcxZmU5ZWYyMzQ5NGUwZWY5YTE0NDVkNWU5NTg0ZjQ5ZjI4MjUiLCJpYXQiOjE2MjgzMTI1MjV9.DRcx9VT1B3umoWFP9O7P4JdzWHLGVKeddbXAiyDxtr0'

client = ipfshttpclient.connect()

def upload_file():
	file_obj=st.file_uploader("Upload Files")
	return file_obj

# Add a file to IPFS
def get_file_hash(file_path=r'C:\Users\win\Desktop\CAT\exp7.txt'):
	file_ipfs=client.add(file_path)
	return file_ipfs['Hash']

# Show IPFS object data
def get_file_content(file_hash):
	return client.cat(file_hash)

# Download IPFS objects
def save_file(file_hash):
	client.get(file_hash)

# Get All Pinned CIDs
def get_all_pinned_CID():
	return client.pin.ls(type='all')

# Client Dictionary
def get_client_id():
	return client.id()
