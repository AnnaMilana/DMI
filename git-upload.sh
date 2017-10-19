#!/bin/bash
if [ $# == 1 ]
then
git config --global user email miilkyyway@gmail.com
git add . 
#git commit -m "201710_11_50"
git commit -m $1
git push origin master
fi
