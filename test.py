# test_vuln.py - Sample vulnerable code for testing

import sqlite3
import os
import subprocess

def vulnerable_sql(username, password):
    # SQL Injection vulnerability
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)
    return cursor.fetchall()

def vulnerable_command(user_input):
    # Command Injection vulnerability
    os.system("ls " + user_input)

def vulnerable_path(filename):
    # Path Traversal vulnerability
    with open("/var/www/uploads/" + filename, "r") as f:
        return f.read()

def hardcoded_secret():
    # Hardcoded secret
    API_KEY = "sk_live_abc123def456ghi789"
    return API_KEY

if __name__ == "__main__":
    vulnerable_sql("admin' --", "anything")
    vulnerable_command("test.txt; rm -rf /")
    vulnerable_path("../../etc/passwd")
    hardcoded_secret()
