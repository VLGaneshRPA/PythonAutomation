


#w - nonbinary file, wb -binary file liek image, pdf,docx etc.,
with open('/Users/apple/Desktop/Python/WebScrap/TextProcessing/input/file2.csv', 'r') as file:
  content = file.read()
  
  
#remove last char to remove lash char comma
print(content[0:-1])

#w - nonbinary file, wb -binary file liek image, pdf,docx etc.,
with open('/Users/apple/Desktop/Python/WebScrap/TextProcessing/input/file2_new.csv', 'w') as file:
  file.write(content[:-1])