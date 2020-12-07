from zipfile import ZipFile

zip_file = 'assign2.zip'
file_name = 'myexample.txt'

with ZipFile(zip_file, 'w') as z:
    z.write(file_name)
