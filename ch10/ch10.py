#pathlib module, Path(), reading from file: read_text(), writing to file: write_text(),
# splitlines(), enumerate(), replace(), try-except-else, pass

from pathlib import Path

#Relative path (Absolute path same syntax)
path0 = Path('file0.txt')
content0 = path0.read_text()
print(f"{content0}\n")

path1 = Path('folder0/fol0.txt')
content1 = path1.read_text()
print(f"{content1}\n")

#Split file content into lines
# enumerate(): using path1_lines as index
path1_lines = content1.splitlines()
for i, line in enumerate(path1_lines):
    print(f"line {i}:\n  {line.strip()}\n")
    
#replace(): ("what to replace", "with what to replace")
path2 = Path('folder0/fol0_rep.txt')
content2 = path2.read_text()
content2 = content2.replace('item','dog')
content2 = content2.replace('action','jump')
path2_lines = content2.splitlines()
for line in path2_lines:
    print(line)
print("\n")

#write_text(): overwrites the entire file content, creates the file if it doesnt exist
path3 = Path('folder0/fol0_write.txt')
content3 = path3.read_text()
print(f"content3 before writing: {content3}")
path3.write_text("11 text ...")
content3 = path3.read_text()
print(f"content3 after writing: {content3}\n")

#try, except ZeroDivisionError/FileNotFoundError
try:
    print(3/0)
except ZeroDivisionError:
    print("cannot divide by 0.\n")
path_not_found_0 = Path('folder0/folder1/not_found.txt')
try:
    content_false0 = path_not_found_0.read_text()
    print(content_false0)
except FileNotFoundError:
    print("File not found.\n")

#Reading multiple files
filenames = ['folder1/text0.txt', 'folder1/text1.txt']
for filename in filenames:
    path = Path(filename)
    content = path.read_text()
    print(content)
print("\n")

#pass
i = -1
while i < 2:
    try:
        division = 1/i
    except ZeroDivisionError:
        pass
    else:
        print(f"division: {division}")
    i += 1