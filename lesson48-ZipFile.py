import os
import zipfile
from os import path

BASE_DIR = path.dirname(path.abspath(__file__))

folder = BASE_DIR + '\\modules'
zip_path = BASE_DIR + '\\test.zip'

my_zip = zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED)

# my_zip.write('news.txt', compress_type=zipfile.ZIP_DEFLATED)


for folder, subfolders, files in os.walk(folder):
    for file in files:
        print(file)
        my_zip.write(
            os.path.join(folder, file),
            os.path.relpath(os.path.join(folder, file), BASE_DIR),
            compress_type=zipfile.ZIP_DEFLATED
        )

my_zip.close()
