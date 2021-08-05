## Domain Name Service

Através do site [https://root-servers.org/](https://root-servers.org/) é possível ver o mapa de distribuição dos servidores raiz de DNS ao redor do globo.

---

Quando a internet começou, havia poucas máquinas,onde todas eram acessíveis diretamente via IP.

Pois eram poucas máquinas, assim sendo fácil decoradar o IP das máquinas.

Mas com o aumento de máquinas na internet, chegou-se a conclusão de que era inviável ficar guardando endereços IP.

Pois é mais fácil guardar e decorar nomes para as máquinas do que sequências numéricas.

Com isso surgiu o arquivo de Host, ele começou com essa proposta de uma base “de” “para”, onde há os endereços IP e os nomes pertinentes a esses endereços.

Segindo assim o príncipio do que viria a ser o DNS.

---

DNS - Domain Name System

É o serviço capaz de transformar IPs em domínios e domínios em IPs.

Sendo estas a únicas funções do DNS.

---

### Comando host (terminal linux)

```
% host google.com.br 
google.com.br has address 142.250.218.163
google.com.br has IPv6 address 2800:3f0:4001:811::2003
google.com.br mail is handled by 0 smtp.google.com.
% 
```

---

## O que faz o DNS

Converter nomes para IPs: Esta é a função mais utilizada do DNS, a resolução de nomes.

Converter IPs em nomes: possível quando há um endereço reverso cadastrado.

Fazer cache dos endereços resolvidos: além da resolução de nomes, por default, o servidor armazena a informação em cache para futuras resoluções.

---

## O que NÃO é o DNS

O DNS não checa se o host no qual está apontando está disponível, isto não é função do DNS!

---
