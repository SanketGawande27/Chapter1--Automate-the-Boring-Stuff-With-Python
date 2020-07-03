#Backup folder into ZIP file

import zipfile, os

def backupToZip(folder):
     folder = os.path.abspath(folder)  
     # Figure out the filename this code should use based on
     # what files already exist.
     number = 1
     while True:
       zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
       if not os.path.exists(zipFilename):
         break
       number = number + 1
       
       # Create the ZIP file.
     print(f'Creating {backup.zip}...')
     backupZip = zipfile.ZipFile(backup.zip, 'w')
     # Walk the entire folder tree and compress the files in each folder.
     for InternPrograms, subfolders, filenames in os.walk(folder):
          print(f'Adding files in {backup}...')
          # Add the current folder to the ZIP file.
          backupZip.write(InternPrograms)

         # Add all the files in this folder to the ZIP file.
     for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
              continue   # don't back up the backup ZIP files
            backupZip.write(os.path.join(InternPrograms, filename))
            backupZip.close()
            print('Done.')


backupToZip('/home/sanket/Desktop/InternPrograms/Intern_Prog')
