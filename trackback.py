#Trackback of a String 
 
 
import traceback
try:
        raise Exception('This is the error message.')
except:
        errorFile = open('errorinfo.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written to errorInfo.txt.')
