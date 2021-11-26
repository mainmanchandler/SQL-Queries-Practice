"""
------------------------------------------------------------------------
testing for get_keyword_counts functions
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-02-25"
------------------------------------------------------------------------
"""
#imports
from Connect import Connect
from Join__Query_Methods import get_keyword_counts
SEP = "-"*100

try:    
        print('Testing get_keyword_counts:\n')
        # Connect to the DCRIS database with an option file
        conn = Connect("dcris.txt")
        # Get the connection cursor object
        cursor = conn.cursor
        
        
        
        print(SEP+'\nTesting get_publication_counts with member_id NOT NONE:')
        #testing with just the cursor
        all_rows = get_keyword_counts(cursor, 42) #42 example
        for i in all_rows:
            print(i)
            
            
        print(SEP+'\nTesting get_publication_counts with member_id NONE:')
        #testing with just the cursor
        all_rows = get_keyword_counts(cursor, None)
        for i in all_rows:
            print(i)
        
    
        conn.close()
        
except Exception as e:
        print(str(e))

