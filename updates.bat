hugo --cleanDestinationDir

cd themes/LoveIt
git pull
git add .
git commit -m "update theme"
git push

cd ../../
git pull
git add .
git commit -m "daily updates"
git push
