"""
------------------------------------------------------------------------
Testing for get_keywords function
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-02-01"
------------------------------------------------------------------------
"""
#imports
from Connect import Connect
from Fetching_by_ID_Functions import get_keywords
SEP = "-"*40

try:    
        print('Testing get_keywords with no keyword ID:\n')
        # Connect to the DCRIS database with an option file
        conn = Connect("dcris.txt")
        # Get the connection cursor object
        cursor = conn.cursor
        
        #testing with just the cursor
        all_rows = get_keywords(cursor)
        for i in all_rows:
            print(i)
        
        print(SEP+'\nTesting get_keywords with keyword ID:')
        #testing with just the cursor
        all_rows = get_keywords(cursor, 13)
        for i in all_rows:
            print(i)
    
        conn.close()
        
except Exception as e:
        print(str(e))