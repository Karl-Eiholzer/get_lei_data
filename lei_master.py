'''Import necessary libraries'''

import time
import xml
from Functions.file_retrieve       import search_LEI_directory
from Functions.download_LEI        import LEI_downloader
from Functions.URL_and_connections import update_LEI_URL
from Functions.LEI_searching       import search_LEI, discover_LEI_structure, search_LEI_main

'''Set loop parameters'''
run = 1
  


while run == 1:
    print(' ------ M E N U -------')
    print('')
    print('  D - to download latest file')
    print('  S - to search through last file downloaded')
    print('  U - to update the URL ')
    print('')    
    activity_type = raw_input('Make a choice (or "Q" to quit): ')
    if activity_type.upper() == 'Q':
        print('')
        print('Thank you for playing')
        print('Good bye!!')
        print('')
        run = 0
    elif activity_type.upper() == 'D':
        LEI_downloader()
        print('')
    elif activity_type.upper() == 'S':
        search_LEI_main()
        print('')
    elif activity_type.upper() == 'U':
        update_LEI_URL()
        print('')
    else:
        print('Input not recognized. Try again')