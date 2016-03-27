echo "Begin to package the software"
cd ..
if [ ! -d "package" ]; then
  mkdir package
fi
if [ -e "blog.tar" ]; then
  rm blog.tar
fi
cp *.py package/
cp -r raw package/
cp -r static package/
cp -r template package/
cp script/start.sh package/
chmod +x package/start.sh
cp script/stop.sh package/
chmod +x package/stop.sh
tar -cvf blog.tar package
rm -rf package/
echo "Finish to package the software"
