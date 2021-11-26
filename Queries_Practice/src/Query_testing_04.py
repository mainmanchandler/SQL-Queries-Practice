"""
------------------------------------------------------------------------
testing the get_expertises method from functions.py
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-02-01"
------------------------------------------------------------------------
"""
#imports
from Connect import Connect
from Fetching_by_ID_Functions import get_expertises

try:
        # Connect to the DCRIS database with an option file
        conn = Connect("dcris.txt")
        # Get the connection cursor object
        cursor = conn.cursor
        
        
        #testing with just the cursor
        print("Testing get_expertises with no keyword, no supp_key:\n")        
                
        pub_data = get_expertises(cursor)
        
        for i in pub_data:
            print(i)
            

        
        
        #testing with cursor and keyword
        print("-"*100 + "\nTesting get_expertises with keyword 'arms', no supp_key:\n")        
        
        pub_data = get_expertises(cursor,keyword="arms")

        for i in pub_data:
            print(i)
        
        
        
        #testing with cursor and supp_key
        print("-"*100 + "\nTesting get_expertises with no keyword, supp_key 'confidence':\n")        

        pub_data = get_expertises(cursor,supp_key="confidence")

        for i in pub_data:
            print(i)
        
        
        
        #testing with cursor, keyword and supp_key 
        print("-"*100 + "\nTesting get_expertises with keyword 'arms', supp_key 'confidence':\n")        

        pub_data = get_expertises(cursor,keyword="arms",supp_key="confidence")

        for i in pub_data:
            print(i)
        
        
        conn.close()
        
        
except Exception as e:
        print(str(e))



