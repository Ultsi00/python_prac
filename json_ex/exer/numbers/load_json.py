#json.loads()

from pathlib import Path
import json

#reads content from .json file and prints it
path = Path('numbers.json')
content = path.read_text()
numbers = json.loads(content)
print(numbers)

