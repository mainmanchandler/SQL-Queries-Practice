"""
------------------------------------------------------------------------
get_all_pub_counts function testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-03-03"
------------------------------------------------------------------------
"""
#imports
from Connect import Connect
from Sub-Query_Methods import get_all_pub_counts
SEP = "-"*100

try:    
        print('Testing get_all_pub_counts:\n')
        # Connect to the DCRIS database with an option file
        conn = Connect("dcris.txt")
        # Get the connection cursor object
        cursor = conn.cursor
        
        
        print(SEP+'\nTesting get_all_pub_counts with member_id NOT NONE:')

        all_rows = get_all_pub_counts(cursor, 90) #90 is example 
        for i in all_rows:
            print(i)
            
            
        print(SEP+'\nTesting get_all_pub_counts with member_id NONE:')

        all_rows = get_all_pub_counts(cursor)
        for i in all_rows:
            print(i)
        
        conn.close()
  
        
except Exception as e:
        print(str(e))