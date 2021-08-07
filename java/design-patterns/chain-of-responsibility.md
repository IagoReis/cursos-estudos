

Em diversas ocasiões, o instrutor cita que ter diversos if pode ser um problema, e que ter uma classe que "pode crescer para sempre" também é um problema.

Qual o problema real deste cenário, onde uma classe tem muitos if ou pode crescer para sempre?

Se eu precisar editar um pedaço de código, para implementar uma nova funcionalidade, as chances de quebrar funcionalidades existentes são grandes


Alternativa correta! Sempre que uma nova funcionalidade for implementada, o ideal é que possamos criar código novo e editar o mínimo possível de código já existente.
Este é um dos principais pontos do princípio Aberto-Fechado (Open-Closed Principle) do SOLID. Ao editar código existente, podemos acabar quebrando funcionalidades já implementadas e funcionais.



Assim como qualquer outro conceito em computação, existe mais de uma forma de implementar o padrão de projeto Chain of Responsibility.

Para saber mais sobre a parte teórica deste padrão, e analisar diferentes implementações, você pode conferir este link:

https://refactoring.guru/design-patterns/chain-of-responsibility.