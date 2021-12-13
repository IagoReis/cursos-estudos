# Microsserviços

- [Tipos de Microsserviços]()
  - [Data Service]()
  - [Business Service]()
  - [Translation Service]()
  - [Edge Service]()
- [Padrões de Projeto]()
  - [Strangler Pattern]()
  - [Sidecar Pattern]()
  - [Process Aggregator Pattern]()
- [Separando Serviços]()
- [12 Fatores]()
- [Integração]()
  - [API Gateway]()
- [Banco de Dados](#banco-de-dados)
- [Padrões de codificação](#padroes-de-codificacao)
  - [CQRS](#cqrs)
- [Logs](#logs)
- [Componentes de Microsserviços](#componentes-de-microsseviços)
- [Contrato Entre Microsserviços](#contrato-entre-microsservicos)
- [Barreiras Entre Microsserviços](#barreiras-entre-microsserviços)
- [Criação de Microsserviços](#criação-de-microsserviços)
  - [Cuidar do Host](#cuidar-do-host)




# Padrões de Projeto


## Strangler Pattern

Este padrão de projeto diz respeito a pegar um projeto monolítico e identificar seus domínios para decompr o projeto em microsserviços.

Por que é interessante quebrar a aplicação em serviços depois que ela já está desenvolvida e funcionando?

Com uma aplicação já funcional, é muito mais fácil identificar os domínios que precisam ser separados e o que não é tão crítico, além de termos mais confiança nas implementações das regras.


## Sidecar Pattern

Este padrão de projeto é utilizado quando há uma mesma funcionalidade que precisa ser utilizada por diversos microsserviços, porém podendo possuir comportamentos diferente por microsserviço.

Assim o padrão Sidecar informa que devemos utilizar um componente com uma base de código única para atualizar a utililização em todos os outros microsserviços de uma única vez.

Um exemplo seria a criação de uma biblioteca.


## Process Aggregator Pattern

Um agregador de processos utiliza serviços de negócio.

Um serviço de negócio utiliza serviços de domínio.

Observando que um agredador de processos pode e deve realizar seus próprios processamentos, como unir as respostas dos serviços utilizados.

Sendo assim um agredador de serviço **não é** um proxy, pois este apenas chama e devolve as requisições sem processamento.


## Edge Pattern

Edge service se adequa as necessidades do cliente para que o processo seja otimizado.

O Edge Pattern define a criação de Edge Services, sendo esses "serviços de ponta" que são utilizados diretamente pelo cliente, podendo até substituir o API Gateway.

Pode haver diversos Edge Services com a mesma funcionalidade, porém com customizações para cada cliente que os utiliza.

#### Quando um Edge Service é interessante?

```shell
Quando clientes diferentes possuem necessidades diferentes
```





# Tipos de Microsseviços


## Data Service

Tipo de serviço para exposição de dados, sendo uma aplicação que repesenta uma camada mais fina antes do banco de dados.

Esse tipo de serviço é responsável por receber os dados e fazer os processamentos necessários para manter as informações consistentes.


## Business Service

Fornece operações de regras de negócio.


## Translation Service

Tipo de serviço responsável por disponibilizar serviços externos.


## Edge Service

Tipo de serviço que é entregue diretamente ao cliente





# Banco de Dados


## Single Service Database

Single Service Database, Single Service Single Database, Single Database Service.

A ideia é que um serviço tenha apenas um banco de dados e que um banco de dados seja utilizado por apenas um serviço.

A escalabilidade de um serviço está diretamente realizada ao banco dados utilizado.


## Shared Service Database

Quando um banco de dados precisa ser utilizado por um ou mais microsserviços.

O problema desta abordagem é que todo o banco será escalado para suprir as necessidades do serviço que mais consome recursos.

Assim causando desperdício, pois haverá tabelas que serão escaladas sem necessidade.

Porém mesmo estando na mesma base de dados, cada serviço deve possuir seu próprio comportamento, fazendo sua própria conexão com o banco de dados e consumindo suas próprias tabelas.

Desta forma os seriços deverão funcionar de maneira independente, embora estejam em um mesmo banco de dados.

#### Entendemos que cada serviço deve acessar seu próprio banco de dados apenas. Qual a vantagem de termos bancos de dados diferentes para cada serviço que precisa de acesso a dados?

```shell
Escalabilidade. Com cada serviço tendo seu próprio banco, a escalabilidade do serviço e banco pode ser feita em conjunto. Assim, serviços que recebem poucos acessos podem ter bancos menos potentes e mais baratos, e vice-versa.
```





# Padrões de Codificação


## CQRS

Command Query Responsibility Segregation

A ideia do CQRS é separar a aplicação entre as responsabilidades de **Leitura** e **Escrita**.

#### Descomplicando CQRS

https://www.youtube.com/watch?v=yd6V4w19iJU


#### Tipos de Microservices

https://cursos.alura.com.br/tipos-de-microservices-c698



APL - Application Performance Management

Fornecem ferramentas para agregar logs e formar uma call stack / trace stack.





# Logs

#### Em microsserviços ou não, logs são uma parte fundamental de um sistema. Por que logs são tão importantes?

```shell
São os logs que nos informam o estado e a saúde do sistema.
Logs estão para a saúde do sistema assim como exames estão para nossa saúde física. Através de logs podemos identificar informações muito valiosas sobre nossa aplicação.
```

#### Por que logs são ainda mais importantes em microsserviços?

```shell
Pois sem eles não poderíamos rastrear as chamadas de uma execução.
Os logs são o que nos permitem montar uma espécie de call stack ou stack trace, ou seja, através de logs conseguimos reproduzir uma execução e depurá-la.
```





# Componentes de Microsserviços

#### O que significa um "componente" (API, banco de dados, processador de mensagens, etc) no contexto de um microsserviços?

```shell
Um servidor, uma aplicação ou infraestrutura de apoio.
Uma máquina (servidor) pode ser considerada um componente. Várias aplicações em uma mesma máquina podem ser vários componentes.
Um serviço de apoio (como banco de dados ou fila de mensageria) pode ser um componente.
Qualquer coisa que efetivamente componha o serviço, é um componente.
```





# Contrato Entre Microsserviços





# Barreiras Entre Microsserviços

Não existe regras para definifir quais funcionalidades deverão ficar em cada microsserviço. Sendo assim cada caso deve ser analisado conforme suas especificidades.

Algo mais específico que nos ajuda a separar conceitos de domínio são os Contextos Delimitados (Bounded Contexts) do DDD (Domain-Driven Design).



# Criação de Microsserviços

## Cuidar do Host

- Máquinas Virtuais
  - Vagrant
  - Puppet
- Cloud
  - PaaS (Kubernetes / Openshift)
  - AWS / Azure / GPC (Google Cloud Plartform)


# Anexos


## O que é arquitetura

https://dias.dev/2020-04-10-o-que-e-arquitetura/


## Domain-Driven Design (DDD) - O que é?

https://cursos.alura.com.br/domain-driven-design-ddd-o-que-e--c283


## Formação Arquitetura e Design de Projetos Java

https://cursos.alura.com.br/formacao-arquitetura-design-projetos-java


## Literatura

Acho que esses 3 aqui são os mais conhecidos e indicados pra todos:

https://amzn.to/37T6hqs
https://amzn.to/2Xzt2Ow
https://amzn.to/3jYs5qC

De 2 deles eu achei versões em Português, se preferir:

https://amzn.to/3CRQt5Q
https://amzn.to/3ySVQPT




Corretora: 1 mensagem do lote por segundo
Conta: 20 mensagens do lote por segundo
Vínculo: 10 mensagens do lote por segundo



34191.75595 05910.312528 50451.630003 8 000