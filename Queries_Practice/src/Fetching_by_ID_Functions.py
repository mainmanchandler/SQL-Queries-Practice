"""
------------------------------------------------------------------------
SQL "get" Methods
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-02-01"
------------------------------------------------------------------------
"""


def get_keywords(cursor, keyword_id=None):
    """
    -------------------------------------------------------
    Queries the keyword table.
    Use: rows = get_keywords(cursor)
    Use: rows = get_keywords(cursor, keyword_id=v)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword_id - a keyword ID (int)
    Returns:
        rows - (list of keyword table data)
            if keyword_id is not None:
                rows matching keyword_id
            else:
            Sorted by keyword description
    -------------------------------------------------------
    """
        
    if keyword_id is None:
        # Define a SQL query
        sql = "SELECT * FROM keyword ORDER BY k_desc"
        # Execute the query from the connection cursor
        cursor.execute(sql)
        # Get the contents of the query results (raw results)
        rows = cursor.fetchall()
    else:
        # Define a SQL query
        sql = "SELECT * FROM keyword WHERE keyword_id = %s ORDER BY k_desc"
        # Execute the query from the connection cursor
        params = [keyword_id]
        cursor.execute(sql, params)
        # Get the contents of the query results (raw results)
        rows = cursor.fetchall()
    
    return rows


def get_publications(cursor, member_id=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = get_publications(cursor)
    Use: rows = get_publications(cursor, member_id=v1)
    Use: rows = get_publications(cursor, pub_type_id=v2)
    Use: rows = get_publications(cursor, member_id=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
        pub_type_id - a publication type (str)
    Returns:
        rows - (list of pub table data)
            if member_id and/or pub_type_id are not None:
                rows matching member_id and/or pub_type_id
            else:
                the entire pub table
            Sorted by publication title
    -------------------------------------------------------
    """
    
    if (member_id is None) and (pub_type_id is None):
        # Define a SQL query
        sql = "SELECT * FROM pub ORDER BY p_title"
        # Execute the query from the connection cursor
        cursor.execute(sql)
        # Get the contents of the query results (raw results)
        rows = cursor.fetchall()
    
    elif (member_id is None) and (pub_type_id is not None):
        # Define a SQL query
        sql = "SELECT * FROM pub WHERE pub_type_id = %s ORDER BY p_title"
        # Execute the query from the connection cursor
        param = [pub_type_id]
        cursor.execute(sql, param)
        # Get the contents of the query results (raw results)
        rows = cursor.fetchall()
    
    elif (member_id is not None) and (pub_type_id is None):
        # Define a SQL query
        sql = "SELECT * FROM pub WHERE member_id = %s ORDER BY p_title"
        # Execute the query from the connection cursor
        param = [member_id]
        cursor.execute(sql, param)
        # Get the contents of the query results (raw results)
        rows = cursor.fetchall()
    
    else:
        # Define a SQL query
        sql = "SELECT * FROM pub WHERE member_id = %s AND pub_type_id = %s ORDER BY p_title"
        # Execute the query from the connection cursor
        params = [member_id, pub_type_id]
        cursor.execute(sql, params) #or like this: cursor.execute(sql, (member_id, pub_type_id))
        # Get the contents of the query results (raw results)
        rows = cursor.fetchall()   
    
    
    return rows


def get_member_expertises(cursor, member_id=None, keyword_id=None):
    """
    -------------------------------------------------------
    Queries the v_member_keyword view.
    Use: rows = get_member_expertises(cursor)
    Use: rows = get_member_expertises(cursor, member_id=v1)
    Use: rows = get_member_expertises(cursor, keyword_id=v2)
    Use: rows = get_member_expertises(cursor, member_id=v1, keyword_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - (list of v_member_keyword view data)
            if member_id and/or keyword_id are not None:
                rows matching member_id and/or keyword_id
            else:
                the entire v_member_keyword view
            Sorted by member last name, first name, and keyword description
    -------------------------------------------------------
    """
    
    if (member_id is None) and (keyword_id is None):
        # Define a SQL query
        sql = "SELECT * FROM v_member_keyword ORDER BY last_name, first_name, k_desc"
        # Execute the query from the connection cursor
        cursor.execute(sql)
        # Get the contents of the query results (raw results)
        rows = cursor.fetchall()
    
    elif (member_id is None) and (keyword_id is not None):
        # Define a SQL query
        sql = "SELECT * FROM v_member_keyword WHERE keyword_id = %s ORDER BY last_name, first_name, k_desc"
        # Execute the query from the connection cursor
        param = [keyword_id]
        cursor.execute(sql, param)
        # Get the contents of the query results (raw results)
        rows = cursor.fetchall()
    
    elif (member_id is not None) and (keyword_id is None):
        # Define a SQL query
        sql = "SELECT * FROM v_member_keyword WHERE member_id = %s ORDER BY last_name, first_name, k_desc"
        # Execute the query from the connection cursor
        param = [member_id]
        cursor.execute(sql, param)
        # Get the contents of the query results (raw results)
        rows = cursor.fetchall()
    
    else:
        # Define a SQL query
        sql = "SELECT * FROM v_member_keyword WHERE member_id = %s AND keyword_id = %s ORDER BY last_name, first_name, k_desc"
        # Execute the query from the connection cursor
        params = [member_id, keyword_id]
        cursor.execute(sql, params)
        # Get the contents of the query results (raw results)
        rows = cursor.fetchall()  
    
    
    
    return rows



def get_expertises(cursor, keyword=None, supp_key=None):
    """
    -------------------------------------------------------
    Queries the v_keyword_supp_key view.
    Use: rows = get_expertises(cursor)
    Use: rows = get_expertises(cursor, keyword=v1)
    Use: rows = get_expertises(cursor, supp_key=v2)
    Use: rows = get_expertises(cursor, keyword=v1, supp_key=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword - a partial keyword description (str)
        supp_key - a partial supplementary description (str)
    Returns:
        rows - (list of v_keyword_supp_key view data)
            if keyword and/or supp_key are not None:
                rows containing keyword and/or supp_key
            else:
                the entire v_keyword_supp_key view
            Sorted by keyword description, supplementary keyword description
    -------------------------------------------------------
    """
    
    if (keyword is None) and (supp_key is None):
        # Define a SQL query
        sql = "SELECT * FROM v_keyword_supp_key ORDER BY k_desc, sk_desc"
        # Execute the query from the connection cursor
        cursor.execute(sql)
        # Get the contents of the query results (raw results)
        rows = cursor.fetchall()
    
    elif (keyword is None) and (supp_key is not None):
        # Define a SQL query
        sql = "SELECT * From v_keyword_supp_key WHERE sk_desc LIKE %s ORDER BY k_desc, sk_desc"
        # Execute the query from the connection cursor
        param = ['%' + supp_key + '%']
        cursor.execute(sql, param)
        # Get the contents of the query results (raw results)
        rows = cursor.fetchall()
    
    elif (keyword is not None) and (supp_key is None):
        # Define a SQL query
        sql = "SELECT * From v_keyword_supp_key WHERE k_desc LIKE %s ORDER BY k_desc, sk_desc"
        # Execute the query from the connection cursor
        param = ['%' + keyword + '%']
        cursor.execute(sql, param)
        # Get the contents of the query results (raw results)
        rows = cursor.fetchall()
    
    else:
        # Define a SQL query
        sql = "SELECT * From v_keyword_supp_key WHERE k_desc LIKE %s AND sk_desc LIKE %s ORDER BY k_desc, sk_desc"
        # Execute the query from the connection cursor
        params = ['%' + keyword + '%', '%' + supp_key + '%']
        cursor.execute(sql, params)
        # Get the contents of the query results (raw results)
        rows = cursor.fetchall() 
    
    
    return rows






