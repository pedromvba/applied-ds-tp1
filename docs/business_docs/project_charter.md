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



# Dúvidas


Estruture seu projeto utilizando os métodos CRISP-DM (Cross-Industry Standard Process for Data Mining) e TDSP (Team Data Science Process).

Compreenda as diferentes fases do ciclo de vida do TDSP e como elas se aplicam ao seu projeto.

Crie uma organização de diretórios que reflita as diferentes fases do ciclo de vida do TDSP.

Project_Charter tb vai ser construído aos poucos, assim como o Bussiness Canvas



## Falta

Estabeleça as metas e os indicadores que determinarão o sucesso do projeto.

Arquitetura






	
## Metrics







* What are the qualitative objectives? (e.g. reduce user churn)
* What is a quantifiable metric  (e.g. reduce the fraction of users with 4-week inactivity)
* Quantify what improvement in the values of the metrics are useful for the customer scenario (e.g. reduce the  fraction of users with 4-week inactivity by 20%) 
* What is the baseline (current) value of the metric? (e.g. current fraction of users with 4-week inactivity = 60%)
* How will we measure the metric? (e.g. A/B test on a specified subset for a specified period; or comparison of performance after implementation to baseline)



## Architecture
* Data
  * What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.)
* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
  * all the data, 
  * after some pre-aggregation on-prem,
  * Sampled data enough for modeling 

* What tools and data storage/analytics resources will be used in the solution e.g.,
  * ASA for stream aggregation
  * HDI/Hive/R/Python for feature construction, aggregation and sampling
  * AzureML for modeling and web service operationalization
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
  * Data movement pipeline in production
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

