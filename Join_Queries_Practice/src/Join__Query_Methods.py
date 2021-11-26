"""
------------------------------------------------------------------------
SQL functions - grabbing from dcris db; focus on join
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-02-25"
------------------------------------------------------------------------
"""
#imports


def get_member_publications(cursor, title=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = get_member_publications(cursor)
    Use: rows = get_member_publications(cursor, title=v1)
    Use: rows = get_member_publications(cursor, pub_type_id=v2)
    Use: rows = get_member_publications(cursor, title=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        title - a partial title (str)
        pub_type_id - a publication type (str)
    Returns:
        rows - (list of member's last name, a member's first
            name, the title of a publication, and the full publication
            type (i.e. 'article' rather than 'a') data)
            if title and/or pub_type_id are not None:
                rows containing title and/or pub_type_id
            else:
                all member and publication rows
            Sorted by last name, first name, title
    -------------------------------------------------------
    """
    
    #get lname, fname, pub_title, type
    #('Clearwater', 'John Murray', 'Canadian Nuclear Weapons', 'Book')
    
    #if title and pub id are given
    if (title is not None) and (pub_type_id is not None):
        # Define a SQL query
        #Note: INNER JOIN = common elements on condition (intersection)
       
        
        sql = """
        SELECT M.last_name, M.first_name, P.p_title, PD.pt_desc
        FROM pub AS P 
        INNER JOIN member AS M ON P.member_id = M.member_id 
        INNER JOIN pub_type AS PD ON P.pub_type_id = PD.pub_type_id
        WHERE P.p_title LIKE %s AND PD.pub_type_id = %s
        ORDER BY M.last_name, M.first_name, P.p_title;
        """
        
        params = ['%' + title + '%', pub_type_id]
        
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    #if title given and pub id not given
    elif (title is not None) and (pub_type_id is None):
        # Define a SQL query
        
        sql = """
        SELECT M.last_name, M.first_name, P.p_title, PD.pt_desc
        FROM pub AS P 
        INNER JOIN member AS M ON P.member_id = M.member_id 
        INNER JOIN pub_type AS PD ON P.pub_type_id = PD.pub_type_id
        WHERE P.p_title LIKE %s
        ORDER BY M.last_name, M.first_name, P.p_title;
        """
        params = ['%' + title + '%']
        
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    #if title not given and pub id given
    elif (title is None) and (pub_type_id is not None):
        # Define a SQL query
        
        sql = """
        SELECT M.last_name, M.first_name, P.p_title, PD.pt_desc
        FROM pub AS P 
        INNER JOIN member AS M ON P.member_id = M.member_id 
        INNER JOIN pub_type AS PD ON P.pub_type_id = PD.pub_type_id
        WHERE PD.pub_type_id = %s
        ORDER BY M.last_name, M.first_name, P.p_title;
        """
        params = [pub_type_id]
        
        cursor.execute(sql, params)
        rows = cursor.fetchall() 
         
         
    else: #both are none
        sql = """ SELECT M.last_name, M.first_name, P.p_title, PD.pt_desc
        FROM pub AS P 
        INNER JOIN member AS M ON P.member_id = M.member_id 
        INNER JOIN pub_type AS PD ON P.pub_type_id = PD.pub_type_id
        ORDER BY M.last_name, M.first_name, P.p_title;
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        

    
    return rows
    
    
    
    

def get_publication_counts(cursor, member_id=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = get_publication_counts(cursor)
    Use: rows = get_publication_counts(cursor, member_id=v1)
    Use: rows = get_publication_counts(cursor, pub_type_id=v2)
    Use: rows = get_publication_counts(cursor, member_id=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
        pub_type_id - a publication type (str)
    Returns:
        rows - (list of member's last name, a member's first
            name, and the number of publications of type
            pub_type_id data)
            if member_id or pub_type_id is not None:
                rows containing member_id and/or pub_type_id
            else:
                all member names and publication counts
            Sorted by last name, first name
    -------------------------------------------------------
    """
    
    #get lname, fname, # of pub, type of data
    #[('Bain', 'William', 4)]

    
    #if memberid and pub_type_id given 
    if (member_id is not None) and (pub_type_id is not None):
        
        sql = """
        SELECT M.last_name, M.first_name, COUNT(P.pub_type_id)
        FROM pub AS P 
        INNER JOIN member AS M ON P.member_id = M.member_id 
        WHERE M.member_id = %s AND P.pub_type_id = %s
        ORDER BY M.last_name, M.first_name;
        """
        
        params = [member_id, pub_type_id]
        
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    #if memberid given and pub_type_id not given 
    elif (member_id is not None) and (pub_type_id is None):
        
        sql = """
        SELECT M.last_name, M.first_name, COUNT(P.pub_type_id)
        FROM pub AS P 
        INNER JOIN member AS M ON P.member_id = M.member_id 
        WHERE M.member_id = %s
        ORDER BY M.last_name, M.first_name;
        """
        params = [member_id]
        
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    #if memberid not given and pub_type_id given 
    elif (member_id is None) and (pub_type_id is not None):
        
        sql = """
        SELECT M.last_name, M.first_name, COUNT(P.pub_type_id)
        FROM pub AS P 
        INNER JOIN member AS M ON P.member_id = M.member_id 
        WHERE P.pub_type_id = %s
        GROUP BY P.member_id
        ORDER BY M.last_name, M.first_name;
        """
        params = [pub_type_id]
        
        cursor.execute(sql, params)
        rows = cursor.fetchall() 
         
         
    else: #both are none
        sql = """
        SELECT M.last_name, M.first_name, COUNT(P.pub_type_id)
        FROM pub AS P 
        INNER JOIN member AS M ON P.member_id = M.member_id
        GROUP BY P.member_id
        ORDER BY M.last_name, M.first_name;
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
    
    return rows
    
    
    

def get_keyword_counts(cursor, member_id=None):
    """
    -------------------------------------------------------
    Queries the member and keyword tables.
    Use: rows = get_keyword_counts(cursor)
    Use: rows = get_keyword_counts(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - (list of member's last name, a member's first
            name, and the number of expertises (i.e. keywords)
            they hold data)
            if member_id is not None:
                rows containing member_id
            else:
                all member and expertise rows
            Sorted by last name, first name
    -------------------------------------------------------
    """
    
    #lname, fname, #expertises
    #[('Copp', 'Terry', 2)]
    
    #member_id given 
    if (member_id is not None):
        
        sql = """
        SELECT M.last_name, M.first_name, COUNT(KW.k_desc)
        FROM member AS M
        INNER JOIN member_keyword AS MK ON M.member_id = MK.member_id 
        INNER JOIN keyword AS KW ON MK.keyword_id = KW.keyword_id
        WHERE M.member_id = %s
        ORDER BY M.last_name, M.first_name;
        """
        
        params = [member_id]
        
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    #member_id not given 
    else:
        sql = """
        SELECT M.last_name, M.first_name, COUNT(KW.k_desc)
        FROM member AS M
        INNER JOIN member_keyword AS MK ON M.member_id = MK.member_id 
        INNER JOIN keyword AS KW ON MK.keyword_id = KW.keyword_id
        GROUP BY M.last_name, M.first_name
        ORDER BY M.last_name, M.first_name;
        """
                
        cursor.execute(sql)
        rows = cursor.fetchall()
        
    
    return rows
    
    

def get_all_expertises(cursor, member_id=None):
    """
    -------------------------------------------------------
    Queries the member, keyword, and supp_key tables
    Use: rows = get_all_expertises(cursor)
    Use: rows = get_all_expertises(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - (list of member's last name, a member's first
            name, a keyword description, and a supplementary
            keyword description data)
            if member_id is not None:
                rows containing member_id
            else:
                all member and expertise rows
            Sorted by last name, first name, keyword description, supplementary
                keyword description
    -------------------------------------------------------
    """
    
    #lname, fname, key desc., supp_keyword
    #[… ('Copp', 'Terry', 'Military History', 'First World War') …]
    
    #member_id given 
    if (member_id is not None):
        
        sql = """
        SELECT M.last_name, M.first_name, KW.k_desc, SK.sk_desc 
        FROM member AS M
        INNER JOIN member_keyword AS MK ON M.member_id = MK.member_id 
        INNER JOIN keyword AS KW ON MK.keyword_id = KW.keyword_id
        INNER JOIN supp_key AS SK ON MK.keyword_id = SK.keyword_id
        WHERE M.member_id = %s
        ORDER BY M.last_name, M.first_name, KW.k_desc, SK.sk_desc;
        """
        
        params = [member_id]
        
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    #member_id not given 
    else:
        sql = """
        SELECT M.last_name, M.first_name, KW.k_desc, SK.sk_desc 
        FROM member AS M
        INNER JOIN member_keyword AS MK ON M.member_id = MK.member_id 
        INNER JOIN keyword AS KW ON MK.keyword_id = KW.keyword_id
        INNER JOIN supp_key AS SK ON MK.keyword_id = SK.keyword_id
        GROUP BY M.last_name, M.first_name,KW.k_desc, SK.sk_desc
        ORDER BY M.last_name, M.first_name, KW.k_desc, SK.sk_desc;
        """
                
        cursor.execute(sql)
        rows = cursor.fetchall()
        

    
    return rows
    
    
    
    
    
    
    
    

