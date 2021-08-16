#!/bin/bash
head='https://m.shouji.com.cn/down/'
html='.html'

echo "开始数字"
read start
echo "结束数字"
read endnum
mkdir ./$start-$endnum
var=$start
while(( $var<=$endnum ))
do
	echo "$var"
	echo "$head$var$html" >> ./$start-$endnum/urls_$start-$endnum.txt
	let "var++"
done