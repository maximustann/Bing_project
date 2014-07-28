#/bin/bash
output=`ls *.ui`
for i in ${output}
do
	p=$((`expr index $i "."` - 1))
	name=`expr substr "$i" 1 $p`
	pyuic4 -x $i -o ${name}.py
	sed -i "5d" ${name}.py
	if [ ! -e ../project/ui/"Ui_"${name}.py ]
	then
		cp ${name}.py ../project/ui/"Ui_"${name}.py
	fi

	diff -u ${name}.py ../project/ui/"Ui_"${name}.py
	if [ 0 -ne $? ]
	then
		cp ${name}.py ../project/ui/"Ui_"${name}.py
	fi
	rm ${name}.py
done
