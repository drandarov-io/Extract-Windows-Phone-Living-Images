import os
import shutil
import zipfile

for filename in os.listdir(os.curdir):
    if filename.startswith('WP_'):
        print(filename)
        with zipfile.ZipFile(filename) as z:
            with z.open('formats/living/living.mp4') as zf, open(filename.replace('.jpg', '') + '_motion.mp4', 'wb') as f:
                shutil.copyfileobj(zf, f)
