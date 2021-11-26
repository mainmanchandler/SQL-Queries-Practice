"""
------------------------------------------------------------------------
Queries with Sub-queries, METHODS 
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-03-03"
------------------------------------------------------------------------
"""

def get_all_pub_counts(cursor, member_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = pub_counts(cursor)
    Use: rows = pub_counts(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - (list of member's last name, a member's first
            name, and the numbers of publications of each type data.
            Name these three fields "articles", "papers", and "books")
            if member_id is not None:
                rows containing member_id
            else:
                all member and publication rows
            Sorted by last name, first name
    -------------------------------------------------------
    """
    
     
    #lname, fname, # of publications, name the three fields
    #[(Bedeski), (Robert), (1), (2), (0)]
    
    #assignment focuses on subqueries 
    #dcris views are allowed
    
    #member_id given 
    if (member_id is not None):
        
        #a subquery is needed for each type of publication
        sql = """
        SELECT M.last_name, M.first_name, 
            (SELECT COUNT(P.pub_type_id) 
            FROM pub AS P
            INNER JOIN member AS M ON P.member_id = M.member_id
            WHERE P.pub_type_id = "a" AND M.member_id = %s) AS articles,
            
            (SELECT COUNT(P.pub_type_id) 
            FROM pub AS P
            INNER JOIN member AS M ON P.member_id = M.member_id
            WHERE P.pub_type_id = "p" AND M.member_id = %s) AS papers,
            
            (SELECT COUNT(P.pub_type_id) 
            FROM pub AS P
            INNER JOIN member AS M ON P.member_id = M.member_id
            WHERE P.pub_type_id = "b" AND M.member_id = %s) AS books
             
        FROM member AS M
        WHERE M.member_id = %s
        ORDER BY M.last_name, M.first_name;
        """
        
        params = [member_id, member_id, member_id, member_id]
        
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    #member_id not given 
    else:
        
        sql = """
        SELECT M.last_name, M.first_name,
            (SELECT COUNT(P.pub_type_id) 
            FROM pub AS P
            WHERE P.pub_type_id = "a" AND P.member_id = M.member_id) AS articles,
            
            (SELECT COUNT(P.pub_type_id) 
            FROM pub AS P
            WHERE P.pub_type_id = "p" AND P.member_id = M.member_id) AS papers,
            
            (SELECT COUNT(P.pub_type_id) 
            FROM pub AS P
            WHERE P.pub_type_id = "b" AND P.member_id = M.member_id) AS books
             
        FROM member AS M
        ORDER BY M.last_name, M.first_name;
        """
             
        cursor.execute(sql)
        rows = cursor.fetchall()
        
    
    return rows
    
    
    
    
    
def get_expertise_counts(cursor, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = get_expertise_counts(cursor)
    Use: rows = get_expertise_counts(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - (list of member's last name, a member's first
            name, and the number of keywords and supplementary keywords
            for the member data. Name these fields "keywords" and "supp_keys")
            if member_id is not None:
                rows containing member_id
            else:
                all member, keyword, and supplementary keyword rows
            Sorted by last name, first name
   -------------------------------------------------------
    """
    
    #lname, fname, # of keywords, # of sup keywords
    #[(Bedeski), (Robert), (6), (5)]
    
    #member_id given 
    if (member_id is not None):
        
        #similar to question done in assignment #2
        sql = """
        SELECT M.last_name, M.first_name,
            
            (SELECT COUNT(KW.k_desc)
            FROM member AS M
            INNER JOIN member_keyword AS MK ON M.member_id = MK.member_id 
            INNER JOIN keyword AS KW ON MK.keyword_id = KW.keyword_id
            WHERE M.member_id = %s) AS keywords,
            
            (SELECT COUNT(SK.sk_desc)
            FROM member AS M
            INNER JOIN member_supp_key AS MSK ON M.member_id = MSK.member_id 
            INNER JOIN supp_key AS SK ON MSK.supp_key_id = SK.supp_key_id 
            WHERE M.member_id = %s) AS supp_keys
            
        FROM member AS M
        WHERE M.member_id = %s
        ORDER BY M.last_name, M.first_name;
        """
        
        params = [member_id, member_id, member_id]
        
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    #member_id not given 
    else:
        
        #different approach will be needed with more members
        #if the member is in the member_keyword table OR member_supp_key table, then count the values
        sql = """
        SELECT M.last_name, M.first_name,
            (SELECT COUNT(keyword_id)
            FROM member_keyword AS MK
            WHERE MK.member_id = M.member_id) AS keywords,
            
            (SELECT COUNT(supp_key_id)
            FROM member_supp_key AS MSK
            WHERE MSK.member_id = M.member_id) AS supp_keys
            
        FROM member AS M
        ORDER BY M.last_name, M.first_name
        """
        
        
        cursor.execute(sql)
        rows = cursor.fetchall()
        
    
    return rows
    
    




def get_keyword_counts(cursor, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = get_keyword_counts(cursor)
    Use: rows = get_keyword_counts(cursor, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - (list of a keyword's description and the number of
            supplementary keywords that belong to it data. Name the
            second field "supp_key_count".)
            if keyword_id is not None:
                rows containing keyword_id
            else:
                all keyword and supplementary keyword rows
            Sorted by keyword description
    -------------------------------------------------------
    """
    
    #kdesc, # of supp_key
    # ('Arms Control and Non-Proliferation Studies', 25)
    
    if (keyword_id is not None):
        
        #keyword description is 'static', need to count its supp_keys
        sql = """
            SELECT KE.k_desc,
                (SELECT COUNT(SUPP.keyword_id)
                FROM supp_key AS SUPP
                WHERE KE.keyword_id = SUPP.keyword_id) AS supp_key_count
            FROM keyword AS KE
            WHERE keyword_id = %s
            ORDER BY KE.k_desc
        """
        
        params = [keyword_id]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
        
    #keyword_id not given 
    else:
        
        #keyword description is 'static', need to count its supp_keys
        sql = """
            SELECT KE.k_desc,
                (SELECT COUNT(SUPP.keyword_id)
                FROM supp_key AS SUPP
                WHERE KE.keyword_id = SUPP.keyword_id) AS supp_key_count
            FROM keyword AS KE
            ORDER BY KE.k_desc
        """
             
        cursor.execute(sql)
        rows = cursor.fetchall()
        
    
    return rows
    
    
    
    
def get_keyword_member_counts(cursor, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = get_keyword_member_counts(cursor)
    Use: rows = get_keyword_member_counts(cursor, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - (list of a keyword description and the number of members
            that have it data. Name the second field "member_count".)
            if keyword_id is not None:
                rows containing keyword_id
            else:
                all member and keyword rows
            Sorted by keyword description
    -------------------------------------------------------
    """
    
    #kdesc, # of members w/data
    #('Civil-Military Relations', 15)
    
    if (keyword_id is not None):
        
        #need to get the # members that have the keyword 
        sql = """
        SELECT KE.k_desc, COUNT(DISTINCT M.member_id) AS member_count
        FROM keyword AS KE, member AS M
        INNER JOIN member_keyword AS MK ON M.member_id = MK.member_id 
        WHERE MK.keyword_id = KE.keyword_id AND KE.keyword_id = %s
        GROUP BY KE.k_desc
        ORDER BY KE.k_desc
        """


        params = [keyword_id]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
        
    #keyword_id not given 
    else:
        
        #same thing just dont add the %s
        sql = """
        SELECT KE.k_desc, COUNT(DISTINCT M.member_id) AS member_count
        FROM keyword AS KE, member AS M
        INNER JOIN member_keyword AS MK ON M.member_id = MK.member_id 
        WHERE MK.keyword_id = KE.keyword_id
        GROUP BY KE.k_desc
        ORDER BY KE.k_desc
        """
          
        cursor.execute(sql)
        rows = cursor.fetchall()
        
    
    return rows
    
    
def get_supp_key_member_counts(cursor, supp_key_id=None):
    """
    -------------------------------------------------------
    Use: rows = get_supp_key_member_counts(cursor)
    Use: rows = get_supp_key_member_counts(cursor, supp_key_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        supp_key_id - a supp_key ID number (int)
    Returns:
        rows - (list of a keyword's description, a supplementary
            keyword description, and the number of members that have that
            supplementary expertise data. Name the last field "member_count".)
            if supp_key_id is not None:
                rows containing supp_key_id
            else:
                all member, keyword, and supplementary keyword rows
            Sorted by keyword description, supplementary keyword description
    -------------------------------------------------------
    """
    
    #kdesc, skdesc, # of members that have skdata data
    
    if (supp_key_id is not None):
        
        #grabbing from table with views
        sql = """
        SELECT VSK.k_desc, VSK.sk_desc,
            (SELECT COUNT(VMK.member_id)
            FROM v_member_supp_key AS VMK
            WHERE VMK.supp_key_id = %s) AS member_count
        FROM v_keyword_supp_key AS VSK
        WHERE VSK.supp_key_id = %s
        ORDER BY VSK.k_desc, VSK.sk_desc
        """        
        
        params = [supp_key_id, supp_key_id]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
        
    #supp_key_id not given 
    else:
        
        #grabbing from table with views, no where needed
        sql = """
        SELECT VSK.k_desc, VSK.sk_desc,
            (SELECT COUNT(VMK.member_id)
            FROM v_member_supp_key AS VMK
            WHERE VMK.supp_key_id = VSK.supp_key_id) AS member_count
        FROM v_keyword_supp_key AS VSK
        ORDER BY VSK.k_desc, VSK.sk_desc
        """
          
        cursor.execute(sql)
        rows = cursor.fetchall()
        
    
    return rows
    
    
    
    
    