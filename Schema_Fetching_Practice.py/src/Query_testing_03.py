"""
------------------------------------------------------------------------
get_constraint_info testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-03-17"
------------------------------------------------------------------------
"""

#imports
from Connect import Connect
from Schema_Fetching_Methods import get_constraint_info
SEP = "-"*100

try:    
        print('Testing get_constraint_info:\n')
        # Connect to the DCRIS database with an option file
        conn = Connect("dcris.txt")
        # Get the connection cursor object
        cursor = conn.cursor
        
        
        print(SEP+'\nTesting get_constraint_info with constraint_type NOT NONE:')

        all_rows = get_constraint_info(cursor, "dcris", "FOREIGN KEY") #example is foreign key   
        for i in all_rows:
            print(i)
            
            
        print(SEP+'\nTesting get_constraint_info with constraint_type NONE:')

        all_rows = get_constraint_info(cursor, "dcris")
        for i in all_rows:
            print(i)
        
        conn.close()
  
        
except Exception as e:
        print(str(e))

