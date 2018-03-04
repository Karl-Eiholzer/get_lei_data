''' functions to handle search through the LEI files '''

def search_LEI_main():
    'Search Control Function'
    discover_LEI_structure()
    print('Search!')

def search_LEI():
    'Search Control Function'
    print('Search!')

def discover_LEI_structure():
    'Get nodes associated with XML Function'
    target_file = './Download/GMEIIssuedFullFile_20180304T023209.zip'
    import zipfile
    import xml.etree.ElementTree as ET
    '''zipinfo.target_file'''
    if zipfile.is_zipfile(target_file):
        print('')
        print('It thinks it is a zip file!!')
        print('')
    else:
        print('Not a zip file!!')
    '''tree = ET.parse('country_data.xml')'''
    print('Search!')