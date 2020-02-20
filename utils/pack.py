# Zip Packer (DO NOT TOUCH)

from zipfile import ZipFile
from glob import glob
from utils.constants import SOLUTION_ZIP, PACK_EXCLUDE
import os

def packSolution():
    if os.path.exists(SOLUTION_ZIP):
        os.remove(SOLUTION_ZIP)

    with ZipFile(SOLUTION_ZIP, 'w') as zipObj:
        for f in glob("./*.py"):
            if not f in PACK_EXCLUDE:
                zipObj.write(f)