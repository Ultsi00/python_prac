#exists()

from pathlib import Path
import json

#Checks if "username.json" exists, then prints the content.
# If the file does not exists, file is created and user input is added into it
path = Path('username.json')
if path.exists():
    content = path.read_text()
    username = json.loads(content)
    print(f"hello {username}")
else:
    print("Type username: ")
    username = input()
    content = json.dumps(username)
    path.write_text(content)