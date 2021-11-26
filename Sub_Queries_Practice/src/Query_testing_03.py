"""
------------------------------------------------------------------------
get_keyword_counts function testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-03-03"
------------------------------------------------------------------------
"""
#imports
from Connect import Connect
from Sub-Query_Methods import get_keyword_counts
SEP = "-"*100

try:    
        print('Testing get_keyword_counts:\n')
        # Connect to the DCRIS database with an option file
        conn = Connect("dcris.txt")
        # Get the connection cursor object
        cursor = conn.cursor
        
        
        
        print(SEP+'\nTesting get_keyword_counts with keyword_id NOT NONE:')

        all_rows = get_keyword_counts(cursor, 7)
        for i in all_rows:
            print(i)
            
            
        print(SEP+'\nTesting get_keyword_counts with keyword_id NONE:')

        all_rows = get_keyword_counts(cursor)
        for i in all_rows:
            print(i)
            
    
        conn.close()
        
except Exception as e:
        print(str(e))
