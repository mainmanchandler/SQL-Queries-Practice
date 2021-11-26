"""
------------------------------------------------------------------------
testing for get_all_expertises functions
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-02-25"
------------------------------------------------------------------------
"""

#imports
from Connect import Connect
from Join__Query_Methods import get_all_expertises
SEP = "-"*100

try:    
        print('Testing get_all_expertises:\n')
        # Connect to the DCRIS database with an option file
        conn = Connect("dcris.txt")
        # Get the connection cursor object
        cursor = conn.cursor
        
        
        
        print(SEP+'\nTesting get_all_expertises with member_id NOT NONE:')
        #testing with just the cursor
        all_rows = get_all_expertises(cursor, 42)
        for i in all_rows:
            print(i)
            
            
        print(SEP+'\nTesting get_all_expertises with member_id NOT NONE AND DIFFERENT:')
        #testing with just the cursor
        all_rows = get_all_expertises(cursor, 3)
        for i in all_rows:
            print(i)
        
        '''
        #the below is too long for console, 
        print(SEP+'\nTesting get_all_expertises with member_id NONE:')
        
        #testing with just the cursor
        all_rows = get_all_expertises(cursor, None)
        for i in all_rows:
            print(i) 
        '''
        conn.close()
        
except Exception as e:
        print(str(e))