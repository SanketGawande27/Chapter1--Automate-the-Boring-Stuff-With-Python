import send2trash
 delFile = open('delete.txt', 'a')
 delFile.write('Ready to delete')
 delFile.close()
 dfile = send2trash.send2trash('delete.txt')
 print(dfile)
