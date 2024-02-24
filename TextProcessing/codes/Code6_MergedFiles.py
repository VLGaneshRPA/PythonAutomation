from pathlib import Path

files_dir = Path('/Users/apple/Desktop/Python/WebScrap/TextProcessing/input/Code4')

merged_content = ''
for filepath in files_dir.iterdir():
  with open(filepath, 'r') as file:
    content = file.read()
    merged_content = merged_content + content + '\n'
  
  with open('/Users/apple/Desktop/Python/WebScrap/TextProcessing/input/Code4/merged.csv', 'w') as file:
    file.write(merged_content)
    