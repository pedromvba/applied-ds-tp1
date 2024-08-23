# Project Charter

## Contexto Negocial, ODS e Público Alvo

O sistema de saúde público no Brasil é bastante abrangente, tanto em termos de procedimentos que podem ser realizados gratuitamente quanto no espaço geográfico que ele deve cobrir, considerando as dimensões do Brasil. 

Ao mesmo tempo, devido a essas características, bem como a definição na Constituição Nacional de que a saúde é direito do cidadão, o sistema de saúde brasileiro necessita de um bom planejamento de investimentos. Nesse sentido, é importe que os gestores da saúde consigam ter uma visão resumida dos atendimentos realizados, bem como dos investimentos despendidos, de forma a planejar as despesas nos anos posteriores.

Além disso, uma das realidades que acomete o povo brasileiro é a infraestrutura de saúde mais simples longe das capitais, fazendo com que o público tenha que se deslocar grandes distâncias para ser atendido nas capitais. 

Assim, de forma a subsidiar o planejamento de gestores dos Ministério da Saúde para o ano posterior, bem como indicar localidades nas quais há espaço para incremento/investimento em infraestrutura de saúde, o aplicativo criado apresenta de forma compreensível e prática tais informações para que sejam utilizada por Prefeituras, parlamentares/candidatos, ONGs e Empresários do Setor da Saúde no suporte das justificativas das busca de seus objetivos, sejam eles votos, recursos financeiros, etc.

## Escopo

O escopo do projeto compreenderá:

* Análise dos dados de atendimento do SUS para o Estado de Roraima (RR); 

* Modelo de regressão linear para prever com base em dados históricos o número de atendimentos previsto para o próximo ano, bem como o custo previsto.

* Identificação de regiões com potencial de investimento em infraestrutura de saúde, baseados no deslocamento dos cidadãos em busca de atendimento do SUS.

* Front-End desenvolvido em Streamlit para comunicar os resultados.

# Stakeholders

* Prefeituras 
* Ministério da Saúde 
* Datasus
* Gestores Públicos da Saúde 
* Prefeituras
* Parlamentares e Candidatos 
* ONGs
* Empresários do Setor da Saúde
* Cientista de Dados

## Comunicação

* Reports semanais entre o cientista de dados e o idealizador da aplicação para o acompanhamento do desenvolvimento do projeto.

* Aplicativo Web para comunicação dos resultados com o cliente.

* Email disponibilizado no aplicativo web para sugestão de melhorias, reclamações e contato com o cientista de dados/desenvolvedor.

## Fases

### 1. Conhecimento do Negócio

Entendimento do problema decisório e dados relacionados.

Milestone: Entrega da primeira versão do Project Charter e Business Canvas

### 2. Preparação dos Dados

Entendimento das fontes de dados, dos tipos, análise exploratória e representação.

Milestones: Aplicação demo com:

* título do projeto, 
* descrição do problema de negócio e dos objetivos do projeto 
* links úteis para as iniciativas e fontes de inspiração do projeto 
* tabela exibindo amostras dos dados

### 3. Modelagem

Seleção, extração de atributos e treinamento do modelo.

Milestones: 

* Modelo preditivo que consiga prever com base em dados históricos o número de atendimentos previsto para o próximo ano, bem como o custo previsto.

* Desenvolvimento de painel com análise acerca das regiões com potencial de investimento em infraestrutura de saúde, baseados no deslocamento dos cidadãos em busca de atendimento do SUS.

### 4. Avaliação

Avaliação do trabalho desenvolvido pelo idealizador da aplicação e implementação de melhorias

Milestones: O de acordo do idealizador do projeto 


### 5. Implantação

Implantação da aplicação em produção.

Milestone: aplicação acessível e funcional via navegador web.


## Metas e Indicadores

*  Indicador: Número de Contratos Assinados até o final de 2025.

  * Meta: 1 Prefeitura,  2 Parlamentares/Candidatos, 1 Empresário


## Arquitetura
