"""
------------------------------------------------------------------------
functions file for calling dcris schema information
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2021-03-17"
------------------------------------------------------------------------
"""


def get_table_info(cursor, table_schema, table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLES for metadata.
    Use: rows = get_table_info(cursor, table_schema)
    Use: rows = get_table_info(cursor, table_schema, table_name=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        table_name - a table name (str)
    Returns:
        rows - (list of the TABLE_NAME, TABLE_TYPE, TABLE_ROWS,
            and TABLE_COMMENT fields data)
            if table_name is not None:
                rows containing table_name
            else:
                all TABLES rows
            Sorted by TABLE_NAME, TABLE_TYPE
    -------------------------------------------------------
    """
    
    #use information_schema.TABLES
    #table_schema will be "dcris"
    
    if table_name is not None: 
        sql = """
            SELECT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT
            FROM information_schema.TABLES
            WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s
            ORDER BY TABLE_NAME, TABLE_TYPE
            """
            
        params = [table_schema, table_name]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    else:
        
        sql = """
            SELECT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT
            FROM information_schema.TABLES
            WHERE TABLE_SCHEMA = %s
            ORDER BY TABLE_NAME, TABLE_TYPE
            """
        
        params = [table_schema]
        cursor.execute(sql, params)
        rows = cursor.fetchall()

    
    return rows;




def get_column_info(cursor, table_schema, table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.COLUMNS for metadata.
    Use: rows = get_column_info(cursor, table_schema)
    Use: rows = get_column_info(cursor, table_schema, table_name=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        table_name - a table name (str)
    Returns:
        rows - (list of the TABLE_NAME, COLUMN_NAME, IS_NULLABLE,
            and DATA_TYPE fields data)
            if table_name is not None:
                rows containing table_name
            else:
                all COLUMNS rows
            Sorted by TABLE_NAME, COLUMN_NAME
    -------------------------------------------------------
    """
    
    #use information_schema.COLUMNS
    
    if table_name is not None:
        sql = """
            SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE
            FROM information_schema.COLUMNS
            WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s
            ORDER BY TABLE_NAME, COLUMN_NAME
            """
            
        params = [table_schema, table_name]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    else:
        
        sql = """
            SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE
            FROM information_schema.COLUMNS
            WHERE TABLE_SCHEMA = %s
            ORDER BY TABLE_NAME, COLUMN_NAME
            """
        
        params = [table_schema]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    
    
    return rows;


    
        
    
def get_constraint_info(cursor, table_schema, constraint_type=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLE_CONSTRAINTS for metadata.
    Use: rows = get_constraint_info(cursor, table_schema)
    Use: rows = get_constraint_info(cursor, table_schema, constraint_type=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        constraint_type - a database constraint type (str)
    Returns:
        rows - (list of the CONSTRAINT_NAME, TABLE_NAME,
            and CONSTRAINT_TYPE fields data)
            if constraint_type is not None:
                rows containing constraint_type
            else:
                all TABLE_CONSTRAINTS rows
            Sorted by CONSTRAINT_NAME, TABLE_NAME
    -------------------------------------------------------
    """
    
    #get from information_schema.TABLE_CONSTRAINTS
    #constraint types like p and f keys
    
    if constraint_type is not None:
    
        sql = """
            SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE
            FROM information_schema.TABLE_CONSTRAINTS
            WHERE TABLE_SCHEMA = %s AND CONSTRAINT_TYPE = %s
            ORDER BY CONSTRAINT_NAME, TABLE_NAME
            """
         
        params = [table_schema, constraint_type]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    else:
        
        
        sql = """
            SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE
            FROM information_schema.TABLE_CONSTRAINTS
            WHERE TABLE_SCHEMA = %s
            ORDER BY CONSTRAINT_NAME, TABLE_NAME
            """
        
        params = [table_schema]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    
    
    return rows;

    
def get_foreign_key_info(cursor, constraint_schema, table_name=None, ref_table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.REFERENTIAL_CONSTRAINTS for metadata.
    Use: rows = get_foreign_key_info(cursor, constraint_schema)
    Use: rows = get_foreign_key_info(cursor, constraint_schema, table_name=v1)
    Use: rows = get_foreign_key_info(cursor, constraint_schema, ref_table_name=v2)
    Use: rows = get_foreign_key_info(cursor, constraint_schema, table_name=v1, ref_table_name=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        constraint_schema - the database constraint schema (str)
        table_name - a table name (str)
        ref_table_name - a table name (str)
    Returns:
        rows - (list of the CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE,
            TABLE_NAME, and REFERENCED_TABLE_NAME fields data)
            if table_name and/or ref_table_name are not None:
                rows containing table_name and/or ref_table_name
            else:
                all REFERENTIAL_CONSTRAINTS rows
            Sorted by CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME
    -------------------------------------------------------
    """
    
    #get from information_schema.REFERENTIAL_CONSTRAINTS
    #four conditions are needed
    #the table name example is pub
    #the referenced table name example is member
    
    if table_name is not None and ref_table_name is not None:
    
        sql = """
            SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, 
                TABLE_NAME, REFERENCED_TABLE_NAME
            FROM information_schema.REFERENTIAL_CONSTRAINTS
            WHERE CONSTRAINT_SCHEMA = %s AND TABLE_NAME = %s AND REFERENCED_TABLE_NAME = %s 
            ORDER BY CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME
            """
         
        params = [constraint_schema, table_name, ref_table_name]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    
    elif table_name is not None and ref_table_name is None:
        
        
        sql = """
            SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, 
                TABLE_NAME, REFERENCED_TABLE_NAME
            FROM information_schema.REFERENTIAL_CONSTRAINTS
            WHERE CONSTRAINT_SCHEMA = %s AND TABLE_NAME = %s 
            ORDER BY CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME
            """
        
        params = [constraint_schema, table_name]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    

    elif table_name is None and ref_table_name is not None:
        
        sql = """
            SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, 
                TABLE_NAME, REFERENCED_TABLE_NAME
            FROM information_schema.REFERENTIAL_CONSTRAINTS
            WHERE CONSTRAINT_SCHEMA = %s AND REFERENCED_TABLE_NAME = %s 
            ORDER BY CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME
            """
            
        params = [constraint_schema, ref_table_name]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    
    else:
        
        sql = """
            SELECT CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE, 
                TABLE_NAME, REFERENCED_TABLE_NAME
            FROM information_schema.REFERENTIAL_CONSTRAINTS
            WHERE CONSTRAINT_SCHEMA = %s 
            ORDER BY CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME
            """
        
        params = [constraint_schema]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    

    
    return rows;





def get_key_info(cursor, constraint_schema, table_name=None, ref_table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.KEY_COLUMN_USAGE for metadata.
    Use: rows = get_key_info(cursor, constraint_schema)
    Use: rows = get_key_info(cursor, constraint_schema, table_name=v1)
    Use: rows = get_key_info(cursor, constraint_schema, ref_table_name=v2)
    Use: rows = get_key_info(cursor, constraint_schema, table_name=v1, ref_table_name=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        constraint_schema - the database constraint schema (str)
        table_name - a table name (str)
        ref_table_name - a table name (str)
    Returns:
        rows - (list of the CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME,
            REFERENCED_TABLE_NAME, and REFERENCED_COLUMN_NAME fields data)
            if table_name and/or ref_table_name are not None:
                rows containing table_name and/or ref_table_name
            else:
                all KEY_COLUMN_USAGE rows
            Sorted by TABLE_NAME, COLUMN_NAME
    -------------------------------------------------------
    """
    
    #get from information_schema.KEY_COLUMN_USAGE
    #four conditions are needed
    #example table name is pub
    #example ref table name is pub_type
    
    
    if table_name is not None and ref_table_name is not None:
    
        sql = """
            SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, 
                REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
            FROM information_schema.KEY_COLUMN_USAGE
            WHERE CONSTRAINT_SCHEMA = %s AND TABLE_NAME = %s AND REFERENCED_TABLE_NAME = %s
            ORDER BY TABLE_NAME, COLUMN_NAME
            """
         
        params = [constraint_schema, table_name, ref_table_name]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    
    elif table_name is not None and ref_table_name is None:
        
        
        sql = """
            SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, 
                REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
            FROM information_schema.KEY_COLUMN_USAGE
            WHERE CONSTRAINT_SCHEMA = %s AND TABLE_NAME = %s
            ORDER BY TABLE_NAME, COLUMN_NAME
            """
        
        params = [constraint_schema, table_name]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    

    elif table_name is None and ref_table_name is not None:
        
        sql = """
            SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, 
                REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME 
            FROM information_schema.KEY_COLUMN_USAGE
            WHERE CONSTRAINT_SCHEMA = %s AND REFERENCED_TABLE_NAME = %s
            ORDER BY TABLE_NAME, COLUMN_NAME
            """
            
        params = [constraint_schema, ref_table_name]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
    
    else:
        
        
        sql = """
            SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, 
                REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
            FROM information_schema.KEY_COLUMN_USAGE
            WHERE CONSTRAINT_SCHEMA = %s
            ORDER BY TABLE_NAME, COLUMN_NAME
            """
        
        params = [constraint_schema]
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    
    return rows;

    
    