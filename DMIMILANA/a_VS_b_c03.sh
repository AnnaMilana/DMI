#!/bin/bash

echo "Napiwi a:"
read a
echo "Napiwi b:"
read b
echo "Napiwi c:"
read c

if [ $a -eq $b -a $a -eq $c ]
then 
  echo "vse chisla ravni"
fi

if [ $a -gt $b -a $a -gt $c ]
then
 if [ $c -gt $b ] 
 then echo " $b,$c,$a "
 else echo " $c, $b, $a "
 fi
fi


if
 [ $b -gt $a -a $b -gt $c ]
then 
 if [ $c -gt $a ]
 then echo " $a,$c,$b "
 else echo " $c,$a,$b "
 fi
fi

if
 [ $c -gt $a -a $c -gt $b ]
then 
 if [ $b -gt $a ]
 then echo " $a,$b,$c "
 else echo " $b,$a,$c "
 fi
fi

