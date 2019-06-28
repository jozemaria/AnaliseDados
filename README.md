sudo pip3 install request

sudo pip3 intall bs4

sudo apt install python-matplotlib

sudo apt install pandas

sudo pip install jupyter


//bash
cat teste.csv | sed 's/Mês ano/Mês,ano/' | sed 's/13.406.686\/0001-67 - //' | tr / , > new.csv

//gambis de levs
cat new.csv | cut -f11 -d" " | cut -f4,5 -d"," | tr -d , | tr -d '"' | tr -d . > valores.csv



