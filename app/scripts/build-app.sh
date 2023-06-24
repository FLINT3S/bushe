cd ../client || exit

yarn run build

cd ../app || exit

rm -f -r ./www

mkdir "www"

cp -r ../client/dist/* ./www

cp -r resources ./www/resources/
