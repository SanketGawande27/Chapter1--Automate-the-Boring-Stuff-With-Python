#copy with folder

import shutil, os
 from pathlib import Path
 p = Path.home()
 fold = shutil.copytree(p / 'Intern_prog', p / 'Intern_Programs')
 print(fold)
