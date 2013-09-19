import exifread
 
def get_date(fname):
    f = open(fname, 'rb')   
    TAGS = exifread.process_file(f, stop_tag='EXIF DateTimeOriginal',details=False)    
    return str(TAGS['EXIF DateTimeOriginal']).split(" ")[0]    
