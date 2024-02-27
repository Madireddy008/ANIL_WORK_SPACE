#Loops
#Using loops, you can a set of commands over and over again, until a certain condition is met. Let's see some of the loops.

#While loop
#It starts running the specified commands if the condition is true and repeats them until the condition is false.

<<Syntax

while [ condition ]
do
#set of statements
done

Syntax

#!/bin/sh
x=2
while [ $x -lt 6 ]
do
echo $x
x=`expr $x + 1`
done