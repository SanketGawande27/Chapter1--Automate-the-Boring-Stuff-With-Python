
import zipfile, os
while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(newzipfile):
            break
        number = number + 1

        print(f'Creating {myProj}...')
        backupZip = zipfile.ZipFile(myProj, 'w')
        print('Done.')

backupToZip('/home/sanket/Desktop/InternPrograms/Intern_Prog')


