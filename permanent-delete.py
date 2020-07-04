#permanently Deleting Files 

import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):
    os.unlink(filename)
