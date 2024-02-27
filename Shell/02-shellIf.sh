<<multi
Comparison Operators:
--------------------
You can compare two variables in shell scripting. We do these comparisons to make decisions, we will see how to do that later in this article, but before that, here is a list of some comparison operators.

Integer comparison:
------------------
Operator	Description
-eq	        is equal to
-ne	        is not equal to
-gt	        is greater than
-ge	        is greater than or equal to
-lt	        is less than
-le	        is less than or equal to

String Comparison:
-----------------
Operator	Description
==	        is equal to
!=	        is not equal to
\<	        is less than, in ASCII alphabetical order
\>	        is greater than, in ASCII alphabetical order
multi

#!/bin/sh
x=10
y=11
if [ $x -ne $y ] 
then
echo "Not equal"
fi