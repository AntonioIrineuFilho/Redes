# Redes - Fundamentos e Abrangência

Definição -> Computadores interconectados compartilhando recursos e trocando informações por meio de um sistema de comunicação, o qual será a própria rede.

Sistema de comunicação -> Arranjo por meio de topologias que interliga os equipamentos por meio de enlaces físicos e de um conjunto de regras que organizam a comunicação(protocolos).

Protocolos definem o formato e ordem das mensagens enviadas e recebidas e ações a serem tomadas no envio e recepção das mesmas.

Por exemplo, assim como quando você pergunta as horas para alguém você espera receber quais horas são, quando o cliente(computador) acessa o endereço de um site ele está pedindo o arquivo do site ao servidor e espera que o servidor mande.

A internet nada mais é que milhões de elementos interconectados, desde computadores, notebooks, dispositivos móveis, servidores e outros equipamentos. A internet não possui um gestor, suas aplicações são distribuídas e a rede é interligada por meio de enlaces físicos de comunicação, como fibra, cabos de cobre, radio e satélite. A rede se comunica enviando e recebendo pacotes por meio dos roteadores.

## Borda da rede

São os sistemas finais, executam os aplicativos e serão clientes(requisitando ao servidor) ou servidores(enviando para o cliente).

Modelo cliente/servidor -> O uma maquina cliente toma iniciativa enviando pedidos os quais são respondidos por outra maquina, o servidor.

Modelo peer-to-peer(P2P) -> Ambas maquinas podem ser cliente e servidor.

## Núcleo da rede

Dispositivos que encaminham pacotes de um dispositivo ao outro, possibilitando a interligação e a formação da rede, como roteadores, switchs e outros dispositivos.

O roteador vai utilizar o protocolo TCP/IP para encaminhar os pacotes até o servidor e trazer de volta o resultado, independe de entender ou não o conteúdo do pacote.

Por exemplo, uma comunicação web funciona por meio do protocolo HTTP ou HTTPS(seguro com conexão criptografada), o roteador vai levar a requisição e trazer o resultado sem entender o pacote, afinal ele entende TCP/IP.

O roteador vai buscar o melhor caminho para encaminhar o pacote, considerando o congestionamento e a integridade, para assim encaminhar o pacote sem danos e da forma mais eficiente.

## Abrangência

A internet é uma rede de escala global(WAN - Wide Area Network), todas as demais escalas de rede se conectam a ela por meio de um ISP(provedor de internet), os provedores vão possuir a infraestrutura necessária a WAN, como uma grande rede de fibra óptica, cabos metálicos e demais enlaces físicos.

O ISP distribui a conexão para as demais redes menores por meio do modem e do roteador, o modem converte o sinal do ISP em um sinal utilizável e o roteador distribui o sinal para os dispositivos da rede.

PAN - Personal Area Network 

Rede de curtíssimo alcance, normalmente conexão de dois dispositivos próximos.

Enlace: Bluetooth ou USB.

LAN - Local Area Network

Rede de alcance limitado, como uma residência, escritório, edifício, pode conectar vários dispositivos e possui núcleos de redes como  o roteador.

Enlace: Cabo de Ethernet ou Sinal de Wi-Fi.

MAN - Metropolitan Area Network

Interligações de diversas LANs, cobrindo uma cidade ou até um grande campus, como uma rede que conecta diversos prédios ou instituições espalhadas pela cidade.

Enlace: Fibras ópticas e tecnologias sem fio de longo alcance.

WAN - Wide Area Network

Redes que cobrem uma grande área geográfica, como um pais ou continente, e conectam múltiplas LANs e MANs, sendo a internet o maior exemplo.

Enlace: Cabos submarinos, satélites, rádio e fibra óptica.



