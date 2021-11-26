"""
------------------------------------------------------------------------
testing for get_publication_counts functions
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-02-25"
------------------------------------------------------------------------
"""
#imports

from Connect import Connect
from Join__Query_Methods import get_publication_counts
SEP = "-"*100

try:    
        print('Testing get_publication_counts:\n')
        # Connect to the DCRIS database with an option file
        conn = Connect("dcris.txt")
        # Get the connection cursor object
        cursor = conn.cursor
        
        
        
        print(SEP+'\nTesting get_publication_counts with member_id and pub_type_id NOT NONE:')
        #testing with just the cursor
        all_rows = get_publication_counts(cursor, 97 , "b")
        for i in all_rows:
            print(i)
            
            
        print(SEP+'\nTesting get_publication_counts with member_id NOT NONE and pub_type_id NONE:')
        #testing with just the cursor
        all_rows = get_publication_counts(cursor, 97, None)
        for i in all_rows:
            print(i)
            
            
        print(SEP+'\nTesting get_publication_counts with member_id NONE and pub_type_id NOT NONE:')
        #testing with just the cursor
        all_rows = get_publication_counts(cursor, None, "b")
        for i in all_rows:
            print(i)
            
            
        print(SEP+'\nTesting get_publication_counts with member_id and pub_type_id NONE:')
        #testing with just the cursor
        all_rows = get_publication_counts(cursor, None, None)
        for i in all_rows:
            print(i)
    
        conn.close()
        
except Exception as e:
        print(str(e))
