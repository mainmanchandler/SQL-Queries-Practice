"""
------------------------------------------------------------------------
get_supp_key_member_counts function testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-03-03"
------------------------------------------------------------------------
"""
#imports
from Connect import Connect
from Sub-Query_Methods import get_supp_key_member_counts
SEP = "-"*100

try:    
        print('Testing get_supp_key_member_counts:\n')
        # Connect to the DCRIS database with an option file
        conn = Connect("dcris.txt")
        # Get the connection cursor object
        cursor = conn.cursor
        
        
        
        print(SEP+'\nTesting get_supp_key_member_counts with supp_key_id NOT NONE:')

        all_rows = get_supp_key_member_counts(cursor, 70)
        for i in all_rows:
            print(i)
            
            
        print(SEP+'\nTesting get_supp_key_member_counts with supp_key_id NONE:')

        all_rows = get_supp_key_member_counts(cursor)
        for i in all_rows:
            print(i)

    
        conn.close()
        
except Exception as e:
        print(str(e))