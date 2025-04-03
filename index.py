import sqlite3

def fetch_users():
    """Fetch all users from the database safely."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Using parameterized queries to prevent SQL injection
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()

    conn.close()
    return users

def main():
    users = fetch_users()
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

if __name__ == "__main__":
    main()
