#!/bin/bash
echo "Enter a number"
read n
t=1
total=0
while [ $t -le $n ]
do
        total=$((t+total))
        t=$((t+1))
done
echo "sum is $total"

t=1
mul=1
while [ $t -le $n ]
do
        mul=$((mul*t))
        t=$((t+1))
done
echo "Factorial is $mul"
