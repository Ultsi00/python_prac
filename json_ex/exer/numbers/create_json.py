#json.dumps()

from pathlib import Path
import json

#writes number list to a .json file
number = [1, 4, 5, 8]
path = Path('numbers.json')
content = json.dumps(number)
path.write_text(content)