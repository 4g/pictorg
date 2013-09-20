pictorg
=======

pict-org

Picture organizer for linux. Given source and destination folder , it will organize all pictures in the source 
folder by exif-date on the image. If duplicate images are detected they are not copied. Since it uses hashing to compare , 
duplicate detection works even when images have different names.

Uses xxpyhash and exifread. 

Speed : Limited by disk read capacity. Gives around 60MB/s on a 5400RPM internal harddrive.     

Run as : sh run.sh src/ dest/
