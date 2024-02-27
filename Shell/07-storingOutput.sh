#Storing the output of commands
#You can store the output of commands inside a variable in a shell script. There are two ways to do so.

#Syntax 1
#var=$(a valid linux command)
#Syntax 2
#var2=`a valid linux command`


#!/bin/sh
b=$(pwd)
c=`pwd`
echo $b
echo $c
d=$(ls /bin | grep bash)
echo $d