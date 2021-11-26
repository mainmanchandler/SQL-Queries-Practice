"""
------------------------------------------------------------------------
testing the get_member_expertises method from functions.py
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-02-01"
------------------------------------------------------------------------
"""
#imports
from Connect import Connect
from Fetching_by_ID_Functions import get_member_expertises

try:
        # Connect to the DCRIS database with an option file
        conn = Connect("dcris.txt")
        # Get the connection cursor object
        cursor = conn.cursor
        
        
        #testing with just the cursor
        print("Testing get_member_expertises with no member_id, no keyword_id:\n")        

        pub_data = get_member_expertises(cursor)
        
        for i in pub_data:
            print(i)
            
        
        #testing with cursor and keyword_id
        print("-"*100 + "\nTesting get_member_expertises with no member_id, keyword_id '10':\n")        

        pub_data = get_member_expertises(cursor,keyword_id=10)

        for i in pub_data:
            print(i)
        
          
        
        #testing with cursor and member_id
        print("-"*100 + "\nTesting get_member_expertises with member_id '9', no keyword_id:\n")        

        pub_data = get_member_expertises(cursor,member_id=9)

        for i in pub_data:
            print(i)
      
              
        
        #testing with cursor, member_id and keyword_id
        print("-"*100 + "\nTesting get_member_expertises with member_id '9', keyword_id '10':\n")        

        pub_data = get_member_expertises(cursor,member_id=9,keyword_id=10)

        for i in pub_data:
            print(i)
        
        
        conn.close()
        
        
except Exception as e:
        print(str(e))


