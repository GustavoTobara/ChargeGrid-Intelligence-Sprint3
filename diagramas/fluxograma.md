# Fluxograma de Funcionamento do ChargeGrid

Este fluxograma mostra o processo de uma sessão de recarga no protótipo ChargeGrid Intelligence.

```mermaid
flowchart TD

    A[Início] --> B[Cadastrar ou selecionar carregador]

    B --> C[Veículo solicita recarga]

    C --> D[Informar energia necessária]

    D --> E[ChargeGrid verifica demanda do estabelecimento]

    E --> F{Demanda ultrapassa o limite?}

    F -- Sim --> G[Reduzir potência automaticamente]

    F -- Não --> H[Manter potência solicitada]

    G --> I[Verificar horário da recarga]

    H --> I

    I --> J{Horário de pico?}

    J -- Sim --> K[Aplicar tarifa de pico]

    J -- Não --> L[Aplicar tarifa normal]

    K --> M[Verificar fontes de energia]

    L --> M

    M --> N{Energia solar disponível?}

    N -- Sim --> O[Utilizar energia solar]

    N -- Não --> P{Bateria disponível?}

    O --> P

    P -- Sim --> Q[Utilizar energia da bateria]

    P -- Não --> R[Utilizar rede elétrica]

    Q --> S{Ainda falta energia?}

    S -- Sim --> R

    S -- Não --> T[Concluir recarga]

    R --> T

    T --> U[Calcular custo]

    U --> V[Selecionar forma de pagamento]

    V --> W[PIX / Cartão / Aplicativo]

    W --> X[Registrar sessão]

    X --> Y[Atualizar relatório]

    Y --> Z[Fim]
```

## Resumo do Processo

O ChargeGrid realiza as seguintes etapas:

1. Identifica o carregador utilizado.
2. Recebe a solicitação de energia do veículo.
3. Verifica o limite de demanda do estabelecimento.
4. Reduz a potência automaticamente caso seja necessário.
5. Define a tarifa de acordo com o horário.
6. Prioriza energia solar.
7. Utiliza a bateria quando necessário.
8. Utiliza a rede elétrica como fonte complementar.
9. Calcula o custo da sessão.
10. Simula o pagamento.
11. Registra os dados para geração de relatórios.
