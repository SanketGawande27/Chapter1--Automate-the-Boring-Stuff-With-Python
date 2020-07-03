#copy file to another folder

import shutil, os
 from pathlib import Path
 p = Path.home()
 cpy = shutil.copy(p / 'read.txt', p / 'Intern_Prog')
 print(cpy)
