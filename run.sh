echo "Usage: sh run.sh src/ dest/"
echo "Checking for requirements"
sh setup.sh > $1/err
echo "Starting ===================== "
echo "Determining redundancies . . . "
python organizer.py $1 $2

numred=$(wc -l < $1/copyjobs.jb)
echo "Number of new files      = $numred"

echo "Making directories       . . . "
sh $1/mkdirjobs.jb 2> $1/err

echo "Copying files            . . . "
sh $1/copyjobs.jb 2> $1/err

echo "Cleaning up              . . . "
rm $1/mkdirjobs.jb
rm $1/copyjobs.jb
rm $1/err

echo "Done =========================="
