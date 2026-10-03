def lookup_user(connection, name):
    return connection.execute(f"SELECT * FROM users WHERE name='{name}'")

