Para que você entenda melhor como aplicar o padrão State em outras situações, é interessante conhecer toda sua parte teórica, como motivação, aplicações, etc.

Para isso, você pode conferir este link: https://refactoring.guru/design-patterns/state.

O padrão de projetos Command é, provavelmente, um dos que mais gera confusão, principalmente no mundo de desenvolvimento web em geral, já que alguns conceitos mais específicos pro mundo da web surgiram.

Para você entender melhor sobre o padrão Command "original" (definido no livro da GoF), você pode dar uma olhada nesse link: https://refactoring.guru/design-patterns/command.

Também é muito interessante o estudo de alguns padrões de arquitetura de software, como Domain Driven Design e Clean Architecture, pois você vai esbarrar no padrão de Command Handlers (que foi aplicado de forma bem simples nesta aula).

Que um caso de uso em nossa aplicação pode ter várias ações (salvar no banco, enviar e-mail, etc);
Que um caso de uso deve ser extraído para uma classe específica, ao invés de estar no arquivo da CLI, controller ou algo do tipo;
Que a técnica de extração do caso de uso para uma classe específica pode ser chamada de padrão Command;
A diferença do padrão Command da GoF para o padrão que utiliza Command Handler (muito utilizado no padrão de arquitetura Domain Driven Design).


O padrão Observer é comumente utilizado por diversas bibliotecas que trabalham com eventos. Muitas tecnologias em Java, como o Spring e o CDI, possuem componentes que nos auxiliam a trabalhar com eventos.

A forma como o padrão foi implementado aqui na aula é a mais simples e pura, mas existem diversas modificações que podem ser feitas.

Para entender mais sobre a teoria deste padrão, você pode conferir este link: https://refactoring.guru/design-patterns/observer.