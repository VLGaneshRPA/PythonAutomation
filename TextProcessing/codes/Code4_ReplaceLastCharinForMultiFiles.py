from pathlib import Path

files_dir = Path('/Users/apple/Desktop/Python/WebScrap/TextProcessing/input/Code4')

count = 0
for filepath in files_dir.iterdir():
  with open(filepath, 'r') as file:
    content = file.read()
    new_content = content[:-1]
  count+=1
  with open('/Users/apple/Desktop/Python/WebScrap/TextProcessing/input/Code4/'+str(count)+'_.csv', 'w') as file:
    file.write(new_content)
    