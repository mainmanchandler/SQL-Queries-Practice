"""
------------------------------------------------------------------------
testing for get_member_publications functions
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-02-25"
------------------------------------------------------------------------
"""
#imports

from Connect import Connect
from Join__Query_Methods import get_member_publications
SEP = "-"*100

try:    
        print('Testing get_member_publications:\n')
        # Connect to the DCRIS database with an option file
        conn = Connect("dcris.txt")
        # Get the connection cursor object
        cursor = conn.cursor
        
        
        
        print(SEP+'\nTesting get_member_publications with title and pub_type_id NOT NONE:')
        #testing with just the cursor
        all_rows = get_member_publications(cursor, "Nuclear" , "b")
        for i in all_rows:
            print(i)
            
            
        print(SEP+'\nTesting get_member_publications with title NOT NONE and pub_type_id NONE:')
        #testing with just the cursor
        all_rows = get_member_publications(cursor, "Nuclear", None)
        for i in all_rows:
            print(i)
            
            
        print(SEP+'\nTesting get_member_publications with title NONE and pub_type_id NOT NONE:')
        #testing with just the cursor
        all_rows = get_member_publications(cursor, None, "b")
        for i in all_rows:
            print(i)
            
            
        print(SEP+'\nTesting get_member_publications with title and pub_type_id NONE:')
        #testing with just the cursor
        all_rows = get_member_publications(cursor, None, None)
        for i in all_rows:
            print(i)
    
        conn.close()
        
except Exception as e:
        print(str(e))
