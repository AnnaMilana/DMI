#!/bin/bash

#val1=`expr $c / $d` 
#val=`expr $a / $b`
#echo "dalīt: $val1"
#echo "dalīt: $val"
#val=`expr $a %  $b`
#echo "Total value 3 : $val"

#val=`expr 37 + 28 + 11 - 10`
#echo "Total value : $val"

#val=`expr $a / $b + $a \* $b`
#echo "dalīt un summēt : $val"

#val1=`expr $c / $d` 
#val=`expr $a / $b`
#echo "dalīt: $val1"
#echo "dalīt: $val"
#val=`expr $a %  $b`
#echo "Total value 3 : $val"

a=$1
b=$2

if [ $a == $b ]
then
   echo "a is equal to b"
fi

if [ $a != $b ]
then
   echo "a is not equal to b"
fi

#piem.1
#a=$1
#b=$2
#val1=`expr $a / $b` 
#echo "dalīt: $val1"
#val=`expr $a / $b + $a \* $b`
#echo "dalīt un summēt : $val"

