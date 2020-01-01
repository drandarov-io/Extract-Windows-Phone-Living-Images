import os
import shutil
import zipfile

for filename in os.listdir(os.curdir):
    if filename.startswith('WP_') and filename.endswith('.jpg') and zipfile.is_zipfile(filename):
        with zipfile.ZipFile(filename) as z:
            print(filename + ' - Bad files: ' + str(z.testzip()))
            if not z.testzip():
                with z.open('formats/living/living.mp4') as zf, open(filename.replace('.jpg', '') + '_motion.mp4', 'wb') as f:
                    shutil.copyfileobj(zf, f)
