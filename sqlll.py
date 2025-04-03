import sqlite3

def get_user_info(username):
    """Fetch user details based on the provided username (Vulnerable to SQL Injection)."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # 🚨 SQL Injection Vulnerability: Directly concatenating user input into the query
    query = f"SELECT id, name, email FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    user = cursor.fetchone()
    conn.close()
    return user

# Simulating user input (Attacker could inject SQL here)
username_input = input("Enter username: ")
user_data = get_user_info(username_input)

if user_data:
    print(f"ID: {user_data[0]}, Name: {user_data[1]}, Email: {user_data[2]}")
else:
    print("User not found.")
