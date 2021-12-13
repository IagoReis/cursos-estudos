Baseado em treinamentos anteriores, já sabemos que classes podem possuir dependências para realizar suas tarefas. No último vídeo, a nossa classe passou a possuir uma dependência de alguma outra implementação que consiga realizar chamadas HTTP.

Qual das alternativas a seguir é uma simples recomendação para trabalhar com dependências?

Alternativa correta
Depender sempre de abstrações, e não de implementações específicas.


Alternativa correta! Inclusive, esse é um dos princípio de SOLID (Dependency Inversion Principle, a letra D).
Devemos sempre preferir depender de abstrações, ou seja, interfaces ou classes abstratas, sempre que possível, ao invés de implementações específicas.


Quando precisamos utilizar código legado ou código de componentes externos em nosso sistema, é muito comum não ter a interface (métodos públicos) batendo com o que a gente precisa, então nesses casos nós criamos adapters.

Esse padrão é muito simples e muito utilizado no dia a dia do desenvolvimento, então vale a pena a sua leitura com mais calma: Adapter.

Nesta aula, aprendemos:

Que padrões estruturais nos ajudam a relacionar diversas classes de forma organizada
Que detalhes de infraestrutura devem ser abstraídos através de interfaces
Como o padrão Adapter pode nos ajudar a trocar detalhes de infraestrutura, sem muitas dores de cabeça