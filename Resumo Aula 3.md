A arquitetura das redes de computadores é organizada conceitualmente em um modelo de camadas.

Os principais modelos são o RM-OSI(Modelo de Referencia para Interconexão de Sistemas Abertos e o TCP/IP.

Ambos modelos são semelhantes e possuem inspiração mutua, uma vez que foram criados na mesma época.

As camadas do modelo OSI são: Física, Enlace, Rede, Transporte, Sessão, Apresentação e Aplicação.

Cada camada especifica o que deve ser feito, mas não como.

As camadas do modelo TCP/IP são: Física, Enlace, Rede, Transporte e Aplicação(engloba a de Sessão, Apresentação e Aplicação na mesma camada).

Cada camada especifica o que e como as funcionalidades devem ser implementadas.

## Camada Física:

A camada física realiza a escolha do meio físico, a transmissão bruta dos bits por meio dos cabos de cobre, fibra óptica, ou mesmo por onda de rádio entre outros meios sem fio. 

Protocolos: xDSL, HFC, SDH, V.35.

## Camada de Enlace:

A camada de enlace realiza o controle do acesso ao meio físico e da transmissão dos bits, incluindo controle de erros e de fluxo, além de realizar o endereçamento físico dos dispositivos(endereço MAC).

Protocolos: Ethernet, Wi-Fi, Bluetooth, PPP, HDLC, DOCSIS, Frame Relay.

## Diferença fundamental:

A camada física define como os bits serão transmitidos, a forma. A camada de enlace controla o acesso, por exemplo, se a conexão com a internet será realizada pelo cabo ou pelo wi-fi.

## Camada de Rede:

Controla o roteamento dos pacotes em redes distintas e realiza o endereçamento lógico das redes por meio do protocolo IP.

*Protocolo ARP -> Converte o IP de dispositivos em uma rede local nos seus endereços MAC, para possibilitar comunicação local.

Protocolos: IPv4, IPv6, ARP, RARP, ICMP, IGMP.

## Camada de Transporte:

Vai realizar a transmissão dos pacotes roteados na camada anterior até o destino, controlando fluxo, congestionamento e etc. Os principais protocolos que realizarão esse transporte é o TCP e o UDP.

TCP x UDP -> O TCP é um protocolo orientado a conexão, logo, ele vai primeiro definir uma rota segura antes de transportar os dados. Já o UDP transportará direto, sem definir rota. O TCP é mais seguro quanto à integridade do pacote, no entanto, mais lento.

Protocolos: TCP, UDP, RTP.

## Camada de Sessão:

Realiza o controle de sessão, mantendo a comunicação ativa mesmo em caso de interrupções.

## Camada de Apresentação:

Realiza a tradução dos dados como são entendidos na rede para como são entendidos pelos usuários.

## Camada de Aplicação:

Realiza a interação direta com o usuário, fornecendo serviços de rede. Um dos protocolos mais populares é o HTTP/HTTPS, que realiza a comunicação web do cliente com o servidor.

Protocolos(Sessão + Apresentação + Aplicação): HTTP/HTTPS, DNS, FTP, SSH, POP3, IMAP, SIP IRC, SNMP, NTP, ETC. 

## Protocolos por Camada no Modelo TCP/IP

Camada de Aplicação: HTTP, FTP, DNS, SMTP, SSH, Telnet, LDAP, BitTorrent, etc.

Camada de Transporte: TCP, UDP, RTP.

Camada de Rede: IPv4, IPv6, ARP, RARP, ICMP, IGMP.

Camada de Enlace: Ethernet, Wi-Fi, PPP, HDLC, Frame Relay, Bluetooth.

Camada Física: 10BaseT, 100BaseT, xDSL, SDH, V.35.
