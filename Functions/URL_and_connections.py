''' handles the URL management and any related connectivity functions '''
''' https://www.gmeiutility.org/restricted/availableFileDownload.jsp# '''

def update_LEI_URL():
    'Change the URL Control Function'
    with open('./Params/LEI_URL.txt', 'r') as myfile:
         LEI_saved_URL = myfile.read()
    print('')
    print('The current URL is: ' + LEI_saved_URL)     
    print('')  
    replacement_URL = raw_input('Enter the new URL to use: ')

    print('')  
    print(LEI_saved_URL + '  has been replaced with  ' + replacement_URL)     
    return LEI_saved_URL

