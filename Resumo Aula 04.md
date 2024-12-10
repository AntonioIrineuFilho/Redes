# Redes - Modos de Transmissão e Topologias

Simplex: Comunicação unidirecional, ou seja, apenas um lado fala e o outro recebe. Um exemplo, é a televisão, que envia a informação para o telespectador que só recebe.

Duplex: Comunicação bidirecional, podendo ser half ou full.

Half-Duplex: Comunicação bidirecional alternada, ou seja, qaulquer dos comunicadores pode enviar e receber, no entanto, um de cada vez. Exemplo é o walkie talkie, em que um lado envia a informação e após receber o outro lado retorna.

Full-Duplex: Comunicação bidirecional simultânea, ou seja, ambos comunicadores podem enviar e receber ao mesmo tempo. Exemplo, uma ligação telefônica. Dobra a velocidade total da rede.

Topologia: Forma como os enlaces físicos estão arranajdos e organizados em uma rede, a fim de possibilitar uma comunicação eficiente emtre os dispositivos da borda.

## Tipos de ligação

Ponto-a-ponto: Conexão entre dois dispositivos sem intermédiarios entre eles, por exemplo, dois computadores conectado a um cabo Ethernet.

Multi-ponto: Conexão entre três ou mais dispositivos por meio de um intermediário, como um hub, switch ou roteador. Por exemplo, dispositivos que se comunicam via IP possuem um roteador como intermediário na maioria das vezes, e essa comunicação pode ser recebida por outros dispositivos conectados ao roteador.

## Características das topologias

Topologias conhecidas: Barra, anel, estrela, mista.

Redes locais: Baixo custo, alta confiabilidade e alta velocidade.

Redes geograficamente distribuidas -> Altíssimo custo, baixa confiabilidade e alta velocidade.

Custo é um fator muito importante para escolher uma topologia.

### Estrela(rede local)

Dispositivos ligados a uma central(hub/switch), todo tráfego passa pela central.

A rede possui um ponto único de falha, que é a própria central.

Podem haver comunicações simultâneas.

### Mista(rede geograficamente distribuida)

Considerar o custo ao desenvolver sistemas desse porte.

A existência de redundãncia é essencial para fins de disponibilidade e backup de dados.

Maximizar a quantidade de ligações para aumentar a capacidade e a interconexão.

## Topologia física x lógica

Define a configuração da rede independente do arranjo físico.

Permite a configuração de diversas redes virtuais, as quais compartilham a mesma topologia física.
