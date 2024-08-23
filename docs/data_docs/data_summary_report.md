# Data Summary Report

## Objetivo do Uso dos Dados

Gerar modelo preditivo que consiga prever com base em dados históricos o número de atendimentos previsto para o próximo ano, bem como o custo previsto.

Desenvolver painel com análise acerca das regiões com potencial de investimento em infraestrutura de saúde, baseados no deslocamento dos cidadãos em busca de atendimento do SUS.

## Dados

### Base dos Dados

#### Origem:

Base dos Dados:

Organização não-governamental sem fins lucrativos e open source. A Associação tem como missão universalizar o acesso a dados no Brasil, por meio da difusão de conhecimento e da criação de ferramentas, a fim de promover o desenvolvimento socioeconômico, o bem-estar social e políticas públicas baseadas em dados e evidências.

[Website Base dos Dados](basedosdados.org)

#### Dados Utilizados:

Sistema de Informações Hospitalares do SUS (SIH/SUS) - Ministério da Saúde

O SIH/SUS, ou Sistema de Informações Hospitalares do Sistema Único de Saúde, é um banco de dados que abrange todos os hospitais que utilizam o SUS, gerido pela Secretaria de Atenção Especializada à Saúde, do Ministério da Saúde. Esse sistema coleta informações sobre internações hospitalares, incluindo dados sobre o paciente, o diagnóstico, os procedimentos realizados e os valores pagos. O SIH/SUS é fundamental para o acompanhamento e gestão dos serviços hospitalares, além de ser uma importante ferramenta para a produção de estatísticas de saúde e a realização de pesquisas.

[Website dos Dados Utilizados](https://basedosdados.org/dataset/ff933265-8b61-4458-877a-173b3f38102b?table=75db9d44-42be-42c5-9fbc-7591f4dc8d5f)

#### Tabela Utilizada

Serviços Profissionais

A Tabela de Serviços Profissionais do SIH/SUS é uma parte integrante do Sistema de Informações Hospitalares do Sistema Único de Saúde. Ela é utilizada para registrar os serviços e procedimentos realizados por profissionais de saúde dentro de hospitais que atendem pelo SUS. Esta tabela inclui informações sobre o tipo de serviço ou procedimento realizado, o código identificador desse serviço, e os valores de referência para o pagamento.
Os serviços são classificados em diferentes categorias, como assistência médica, serviços de diagnóstico e terapia, e outras áreas de atuação profissional. A tabela é atualizada periodicamente para refletir mudanças nos procedimentos, incorporações de novas tecnologias e práticas clínicas.

### Nome dos Procedimentos

A tabela original da Base dos Dados traz os procedimentos em formato de código. Para traduzi-los para os efetivos nomes, utilizamos o arquivo TABELA_NACIONAL_PROCEDIMENTOS.pdf, elaborado pela Prefeitura Municipal de Camaçari. A partir desse arquivo pdf, foi possível obter o arquivo procedure_names.csv, constante da pasta ./app/data/transformed.

### Nome das Cidades



## Amostra dos Dados e Schema




Cobertura Temporal:



The procedures names originate from a pdf found in the internet, made by the Prefeitura Municipal de Camaçari.


