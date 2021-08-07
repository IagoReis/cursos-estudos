# Chain of Responsibility

Em português é traduzido como Cadeia de Responsabilidade ou Corrente de Responsabilidade.

---

Ter diversos if em nosso código pode ser um problema, e ter uma classe que "pode crescer para sempre" também é um problema.

Mas qual o problema real deste cenário, onde uma classe tem muitos if ou pode crescer para sempre?

**Resposta:** Se eu precisar editar um pedaço de código, para implementar uma nova funcionalidade, as chances de quebrar funcionalidades existentes são grandes.

Sempre que uma nova funcionalidade for implementada, o ideal é que possamos criar código novo e editar o mínimo possível de código já existente.

Este é um dos principais pontos do princípio Aberto-Fechado (Open-Closed Principle) do SOLID. Ao editar código existente, podemos acabar quebrando funcionalidades já implementadas e funcionais.

---

Assim como qualquer outro conceito em computação, existe mais de uma forma de implementar o padrão de projeto Chain of Responsibility.

Para saber mais sobre a parte teórica deste padrão, e analisar diferentes implementações, você pode conferir este link:

https://refactoring.guru/design-patterns/chain-of-responsibility.

---