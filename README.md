# README

## Objetivo do Projeto

Subsidiar o planejamento de gestores dos Ministério da Saúde para o ano posterior, bem como indicar localidades nas quais há espaço para incremento/investimento em infraestrutura de saúde

## Instalação do Ambiente e Biblioteca

As dependências necessárias para a execução do projeto estão registradas no arquivo requirements.txt. Todavia, logo após a criação do virtual environment, deve ser realizada a instalação primeiro da biblioteca Base dos Dados. Isso porque, a referida biblioteca, além de ser necessária para se utilizar a API, irá instalar outras dependências como por exemplo o pandas.

Um ponto de atenção, é o fato da biblioteca Base dos Dados necessitar de ** Python >=3.7.1, <3.11**.

Assim, recomenda-se que sejam seguidos os seguintes passos: 

``` shell
python3.10 -m venv .venv
source .venv/bin/activate
pip install basedosdados
```

Conforme registrado, durante a instalação da biblioteca base dos dados, diversas outras são instaladas, como por exemplo pandas e numpy. Ocorre que identificou-se uma incompatibilidade com a versão do numpy instalado, sendo necessária a correção das mesma por meio da instalação de uma versão mais antiga: 

``` shell
pip unistall numpy
pip install numpy==1.24.0
```

## Github do Projeto

[Link do Projeto](https://github.com/pedromvba/applied-ds-tp1)

## Dados do Projeto

Devido ao tamanho dos dados, a pasta data não foi replicada no Github. Os dados podem ser obtidos recriando-se o ambiente e executando os scripts conforme registrado no Data Summary Report, ou podem ser obtidos diretamente no seguinte [link](https://drive.google.com/file/d/1sNKzhx4-ATKZ2tqLI8mPeVx1YYeMMoiv/view?usp=share_link).

Caso opte pelo download, observe a necessidade de colocar o diretório data na raiz do projeto, juntamente com outras pastas como docs, notebooks e app.








