"""
------------------------------------------------------------------------
testing the get_publications method from functions.py
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-02-01"
------------------------------------------------------------------------
"""
#imports
from Connect import Connect
from Fetching_by_ID_Functions import get_publications

try:
        # Connect to the DCRIS database with an option file
        conn = Connect("dcris.txt")
        # Get the connection cursor object
        cursor = conn.cursor
        
        #testing with just the cursor
        print("Testing get_publications with no pub_type, no member_id:\n")

        pub_data = get_publications(cursor)
        
        for i in pub_data:
            print(i)
      
      
        
        #testing with cursor and pub_type
        print("-"*100 + "\nTesting get_publications with pub_type 'b', no member_id:\n")        

        pub_data = get_publications(cursor,pub_type_id='b')

        for i in pub_data:
            print(i)
        
        
        
        #testing with cursor and member_id
        print("-"*100 + "\nTesting get_publications with no pub_type, member_id 31:\n")        

        pub_data = get_publications(cursor,member_id=31)

        for i in pub_data:
            print(i)
        
        
        
        #testing with cursor, member_id and pub_type
        print("-"*100 + "\nTesting get_publications with pub_type 'a', member_id 31:\n")        

        pub_data = get_publications(cursor,member_id=31,pub_type_id='a')

        for i in pub_data:
            print(i)
        
        conn.close()
        
except Exception as e:
        print(str(e))