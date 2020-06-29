for foldername, subfolders, filenames in os.walk(folder):
         print(f'Adding files in {myProj}...')
       
      backupZip.write(foldername)
       
      for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue 
             backupZip.write(os.path.join(foldername, filename))
     backupZip.close()
     print('Successfully Added')

backupToZip('/media/sanket/Sanku')
