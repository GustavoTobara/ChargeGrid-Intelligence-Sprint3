# Arquitetura do ChargeGrid Intelligence

O diagrama abaixo representa a integração dos principais componentes do protótipo.

```mermaid
flowchart TD

    SOLAR[Painéis Solares]
    BAT[Bateria de Armazenamento]
    REDE[Rede Elétrica]

    CG[ChargeGrid Intelligence]

    DEMANDA[Controle de Demanda]
    OTIMIZA[Otimização Inteligente]
    TARIFA[Tarifação]
    PAGAMENTO[Pagamento]

    C1[Carregador 1 - OCPP]
    C2[Carregador 2 - MQTT]
    C3[Carregador 3 - API REST]

    V1[Veículo Elétrico]
    V2[Veículo Elétrico]
    V3[Veículo Elétrico]

    RELATORIO[Relatórios e Dados de Recarga]

    SOLAR --> CG
    BAT --> CG
    REDE --> CG

    CG --> DEMANDA
    DEMANDA --> OTIMIZA

    OTIMIZA --> C1
    OTIMIZA --> C2
    OTIMIZA --> C3

    C1 --> V1
    C2 --> V2
    C3 --> V3

    CG --> TARIFA
    TARIFA --> PAGAMENTO

    C1 --> RELATORIO
    C2 --> RELATORIO
    C3 --> RELATORIO

    RELATORIO --> CG
```

## Funcionamento

O ChargeGrid Intelligence recebe energia de diferentes fontes e gerencia sua utilização de forma automatizada.

A prioridade do sistema é utilizar fontes mais eficientes e sustentáveis, considerando:

1. Energia solar disponível
2. Energia armazenada na bateria
3. Rede elétrica

O controle de demanda verifica a potência disponível antes de permitir uma nova recarga.

O módulo de otimização analisa as condições do sistema e define como os carregadores devem operar.

Os carregadores simulam comunicação por protocolos como OCPP, MQTT e API REST.

As sessões de recarga geram informações utilizadas nos módulos de tarifação, pagamento e relatórios.
