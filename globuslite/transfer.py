from globuslite import auth
from globus_sdk import TransferClient, TransferData
from globuslite.config import get_transfer_tokens

__all__ = ['Transfer']

class Transfer:
    '''
    This class describes a Globus transfer task.
    '''

    def __init__(self, source_id, dest_id, label=None, sync_level=None ):

        self.source_id = auth.verify_uuid( source_id )
        self.dest_id = auth.verify_uuid( dest_id )

        # Perform authorization work
        authorizer = auth.get_refresh_authorizer( get_transfer_tokens() )
        self.transfer_client = TransferClient(authorizer=authorizer)

        self.transfer_data = TransferData( self.transfer_client,
            source_id, dest_id, label=label, sync_level=sync_level)

    def add_item( self, src_path, dst_path, recursive=False ):
        self.transfer_data.add_item( src_path, dst_path,
            recursive=recursive )

    def submit( self ):
        self.transfer_client.submit_transfer( self.transfer_data )

