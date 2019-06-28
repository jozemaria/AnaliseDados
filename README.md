sudo pip3 install request

sudo pip3 intall bs4

sudo apt install python-matplotlib

# Scrapping 
## Programação em Ambientes de Redes

> Scrapping realizado na página do portal da [transparência](http://transparencia.gov.br/) de forma bem básica e tratamento de CSV via bash. Afim de concluir mais rapidamente o projeto solicitado em aula.

#### Instalação Linux:

```bash
sudo pip install jupyter
>> Instalando o Jupyter Notebook para manipulação de dados

sudo apt install pandas
>> Biblioteca para manipulação e analize de dados
```

```bash
cat teste.csv | sed 's/Mês ano/Mês,ano/' | sed 's/13.406.686\/0001-67 - //' | tr / , > new.csv
cat new.csv | cut -f11 -d" " | cut -f4,5 -d"," | tr -d , | tr -d '"' | tr -d . > dad0s.csv

>> tratamentos dados de forma improvisada
```


### Aluno: José Maria Jr