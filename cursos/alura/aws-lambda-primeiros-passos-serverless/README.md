Para organizar melhor seu código, o AWS Lambda oferece dois recursos interessantes: o versionamento e o alias.

Ao publicar o código, é automaticamente atribuída a versão $LATEST.

Sempre que fazemos uma publicação, ela recebe a tag LATEST, mas você pode criar versões a partir dela.

É possível apontar um trigger para o alias, mesmo que este não corresponda à última versão publicada (LATEST).

Esta é uma prática muito interessante. Imagine o seguinte cenário: você aponta o trigger para um alias PROD e a partir daí, mesmo você publicando uma nova versão da sua aplicação, o ambiente de produção não é alterado.

Ao publicar uma nova versão, a mesma automaticamente recebe um alias.

Mas o alias, apesar de muito útil, precisa ser atribuído manualmente no console ou mesmo na CLI.
