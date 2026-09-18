# ChargeGrid Intelligence

## GoodWe Challenge - Sprint 3
### Prototipagem Funcional e Integração

## Integrantes

- Gustavo Naville Tobara — RM570674
- Guilherme Marques dos Santos — RM573112
- Guilherme Wadt de Oliveira — RM569375
- Pedro Henrique Silva Santos — RM571537

## Sobre o Projeto

O ChargeGrid Intelligence é uma proposta de sistema inteligente para gerenciamento de estações de recarga de veículos elétricos em ambientes comerciais.

O projeto foi desenvolvido com base no desafio da GoodWe, buscando integrar energia renovável, automação, controle de demanda, tarifação, comunicação entre dispositivos e otimização inteligente.

## Objetivo

O objetivo do protótipo é simular o funcionamento integrado de uma estação comercial de recarga de veículos elétricos.

O sistema permite:

- Gerenciar sessões de recarga
- Controlar a demanda de energia
- Priorizar o uso de energia solar
- Utilizar energia armazenada em bateria
- Utilizar a rede elétrica quando necessário
- Calcular tarifas de recarga
- Simular pagamentos
- Integrar diferentes carregadores
- Gerar relatórios de consumo
- Aplicar regras de otimização inteligente

## Pilares do ChargeGrid

O projeto considera os quatro principais pilares estudados durante o GoodWe Challenge:

### 1. Controle de Demanda

O sistema verifica o consumo atual do estabelecimento antes de liberar uma nova recarga.

Caso a demanda ultrapasse o limite configurado, a potência do carregador pode ser reduzida automaticamente.

### 2. Protocolos Abertos

O protótipo simula a integração de carregadores utilizando protocolos e tecnologias como:

- OCPP
- MQTT
- API REST

Esses padrões permitem a comunicação entre diferentes dispositivos e sistemas.

### 3. Tarifação e Pagamento

O sistema calcula o custo da recarga considerando a quantidade de energia utilizada e o horário.

Também é possível simular métodos de pagamento como:

- PIX
- Cartão
- Aplicativo

### 4. Otimização Inteligente

O sistema analisa informações de consumo, disponibilidade de energia solar e nível da bateria.

Com base nesses dados, o sistema pode recomendar ações como:

- Reduzir a potência dos carregadores
- Priorizar energia solar
- Utilizar energia armazenada
- Evitar horários de alta demanda

## Sustentabilidade

O sistema prioriza fontes de energia renovável.

A ordem de utilização de energia é:

1. Energia solar
2. Energia armazenada em bateria
3. Rede elétrica

Isso reduz o consumo da rede elétrica e aumenta a eficiência energética da estação.

## Tecnologias Utilizadas

- Python
- GitHub
- Programação Orientada a Objetos
- Estruturas de dados
- Automação baseada em regras
- Simulação de energia renovável
- Simulação de protocolos de comunicação

## Estrutura do Projeto

```text
ChargeGrid-Intelligence-Sprint3/
│
├── README.md
├── src/
│   └── chargegrid.py
├── diagramas/
├── dados/
└── imagens/
