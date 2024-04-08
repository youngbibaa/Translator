stmt_main = {
    "create": """
        CREATE TABLE base (
            id TEXT,
            password TEXT
        )
    """,
    "add": """
        INSERT INTO base (id, password) VALUES (?, ?)
    """,
    "select": """
        SELECT id, password FROM base WHERE id = ?
    """,
}

stmt_storage = {
    "create": """
        CREATE TABLE storage (
            nickname TEXT,
            searches TEXT
        )
    """,
    "add": """
        INSERT INTO storage (nickname, searches) VALUES (?, ?)
    """,
    "select": """
        SELECT * FROM storage WHERE nickname = ?
    """,
}
