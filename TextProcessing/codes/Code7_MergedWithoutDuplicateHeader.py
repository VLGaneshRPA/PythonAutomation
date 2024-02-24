from pathlib import Path

files_dir = Path('/Users/apple/Desktop/Python/WebScrap/TextProcessing/input/Code4/')

merged_content = ''
for index, filepath in enumerate(files_dir.iterdir()):
  with open(filepath, 'r') as file:
    content = file.readlines()
    new_content = content[1:]
  if index == 0:
    content = ''.join(content)  
    merged_content = merged_content + content + '\n'
  else:
    new_content = ''.join(new_content)
    merged_content = merged_content + new_content + '\n'
  
  with open('/Users/apple/Desktop/Python/WebScrap/TextProcessing/input/Code4/merged.csv', 'w') as file:
    file.write(merged_content)
    