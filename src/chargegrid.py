# ============================================================
# GOODWE CHALLENGE - SPRINT 3
# CHARGEGRID INTELLIGENCE
# Protótipo funcional e simulado para ambiente comercial
# ============================================================


class Carregador:
    def __init__(self, identificacao, potencia_kw, protocolo):
        self.identificacao = identificacao
        self.potencia_kw = potencia_kw
        self.protocolo = protocolo
        self.status = "Disponível"


class SessaoRecarga:
    def __init__(self, id_sessao, veiculo, energia_kwh, carregador, horario):
        self.id_sessao = id_sessao
        self.veiculo = veiculo
        self.energia_kwh = energia_kwh
        self.carregador = carregador
        self.horario = horario

        self.potencia_liberada_kw = 0.0
        self.tarifa_kwh = 0.0
        self.energia_solar_kwh = 0.0
        self.energia_bateria_kwh = 0.0
        self.energia_rede_kwh = 0.0
        self.custo_total = 0.0
        self.pagamento = "Pendente"


class ChargeGrid:
    def __init__(self):
        # Dados simulados do ambiente comercial
        self.limite_demanda_kw = 100.0
        self.consumo_predio_kw = 45.0

        # Fontes de energia disponíveis
        self.energia_solar_kwh = 40.0
        self.bateria_kwh = 25.0
        self.capacidade_bateria_kwh = 100.0

        self.carregadores = []
        self.sessoes = []


    # ========================================================
    # PROTOCOLOS ABERTOS
    # ========================================================

    def cadastrar_carregador(self):

        print("\n=== CADASTRO DE CARREGADOR ===")

        identificacao = input("ID do carregador: ").strip()

        if identificacao == "":
            print("ID inválido.")
            return

        for carregador in self.carregadores:
            if carregador.identificacao == identificacao:
                print("Já existe um carregador com esse ID.")
                return

        try:
            potencia = float(
                input("Potência do carregador em kW: ").replace(",", ".")
            )

        except ValueError:
            print("Potência inválida.")
            return

        if potencia <= 0:
            print("A potência deve ser maior que zero.")
            return

        print("\nProtocolos simulados:")
        print("1 - OCPP")
        print("2 - MQTT")
        print("3 - API REST")

        escolha = input("Escolha o protocolo: ")

        protocolos = {
            "1": "OCPP",
            "2": "MQTT",
            "3": "API REST"
        }

        if escolha not in protocolos:
            print("Protocolo inválido.")
            return

        novo = Carregador(
            identificacao,
            potencia,
            protocolos[escolha]
        )

        self.carregadores.append(novo)

        print("\nCarregador cadastrado com sucesso.")
        print("ID:", novo.identificacao)
        print("Potência:", novo.potencia_kw, "kW")
        print("Protocolo:", novo.protocolo)


    # ========================================================
    # CONTROLE DE DEMANDA
    # ========================================================

    def controlar_demanda(self, potencia_solicitada):

        demanda_prevista = (
            self.consumo_predio_kw
            + potencia_solicitada
        )

        print("\n=== CONTROLE DE DEMANDA ===")

        print(
            "Consumo atual do prédio:",
            self.consumo_predio_kw,
            "kW"
        )

        print(
            "Potência solicitada:",
            potencia_solicitada,
            "kW"
        )

        print(
            "Demanda prevista:",
            demanda_prevista,
            "kW"
        )

        print(
            "Limite de demanda:",
            self.limite_demanda_kw,
            "kW"
        )

        if demanda_prevista <= self.limite_demanda_kw:

            print("Demanda dentro do limite.")

            return potencia_solicitada

        potencia_disponivel = (
            self.limite_demanda_kw
            - self.consumo_predio_kw
        )

        if potencia_disponivel <= 0:

            print("Limite de demanda atingido.")

            print(
                "Recarga bloqueada temporariamente."
            )

            return 0.0

        print("Automação ativada.")

        print(
            "Potência reduzida automaticamente para",
            potencia_disponivel,
            "kW."
        )

        return potencia_disponivel


    # ========================================================
    # TARIFAÇÃO
    # ========================================================

    def calcular_tarifa(self, horario):

        # Valores simulados para demonstração

        if 18 <= horario <= 21:

            tarifa = 1.20
            faixa = "Horário de pico"

        else:

            tarifa = 0.75
            faixa = "Fora do horário de pico"

        print("\n=== TARIFAÇÃO ===")

        print("Faixa:", faixa)

        print(
            "Tarifa: R$",
            f"{tarifa:.2f}",
            "por kWh"
        )

        return tarifa


    # ========================================================
    # GERENCIAMENTO DE ENERGIA
    # ========================================================

    def distribuir_energia(self, sessao):

        restante = sessao.energia_kwh

        # 1 - Prioridade para energia solar

        uso_solar = min(
            restante,
            self.energia_solar_kwh
        )

        sessao.energia_solar_kwh = uso_solar

        self.energia_solar_kwh -= uso_solar

        restante -= uso_solar


        # 2 - Depois utiliza bateria

        uso_bateria = min(
            restante,
            self.bateria_kwh
        )

        sessao.energia_bateria_kwh = uso_bateria

        self.bateria_kwh -= uso_bateria

        restante -= uso_bateria


        # 3 - Se ainda faltar, utiliza a rede elétrica

        sessao.energia_rede_kwh = max(
            restante,
            0.0
        )


        print("\n=== DISTRIBUIÇÃO DE ENERGIA ===")

        print(
            "Solar:",
            f"{sessao.energia_solar_kwh:.2f}",
            "kWh"
        )

        print(
            "Bateria:",
            f"{sessao.energia_bateria_kwh:.2f}",
            "kWh"
        )

        print(
            "Rede elétrica:",
            f"{sessao.energia_rede_kwh:.2f}",
            "kWh"
        )


    # ========================================================
    # NOVA SESSÃO DE RECARGA
    # ========================================================

    def nova_sessao(self):

        print("\n=== NOVA SESSÃO DE RECARGA ===")

        if len(self.carregadores) == 0:

            print(
                "Cadastre pelo menos um carregador primeiro."
            )

            return


        try:

            id_sessao = int(
                input("ID da sessão: ")
            )

        except ValueError:

            print("ID inválido.")
            return


        for sessao in self.sessoes:

            if sessao.id_sessao == id_sessao:

                print(
                    "Já existe uma sessão com esse ID."
                )

                return


        veiculo = input(
            "Identificação do veículo: "
        ).strip()


        if veiculo == "":

            print("Veículo inválido.")
            return


        try:

            energia = float(
                input(
                    "Energia solicitada em kWh: "
                ).replace(",", ".")
            )

        except ValueError:

            print("Energia inválida.")
            return


        if energia <= 0:

            print(
                "A energia deve ser maior que zero."
            )

            return


        print("\nCarregadores disponíveis:")


        for indice, carregador in enumerate(
            self.carregadores,
            start=1
        ):

            print(
                f"{indice} - "
                f"{carregador.identificacao} | "
                f"{carregador.potencia_kw} kW | "
                f"{carregador.protocolo}"
            )


        try:

            escolha = int(
                input("Escolha o carregador: ")
            )

            carregador = self.carregadores[
                escolha - 1
            ]

        except (ValueError, IndexError):

            print("Carregador inválido.")
            return


        try:

            horario = int(
                input(
                    "Horário da recarga (0 a 23): "
                )
            )

        except ValueError:

            print("Horário inválido.")
            return


        if horario < 0 or horario > 23:

            print("Horário inválido.")
            return


        # Controle automático de demanda

        potencia_liberada = self.controlar_demanda(
            carregador.potencia_kw
        )


        if potencia_liberada == 0:

            return


        nova = SessaoRecarga(
            id_sessao,
            veiculo,
            energia,
            carregador,
            horario
        )


        nova.potencia_liberada_kw = potencia_liberada


        # Tarifação

        nova.tarifa_kwh = self.calcular_tarifa(
            horario
        )


        # Distribuição inteligente de energia

        self.distribuir_energia(
            nova
        )


        # Custo total da sessão

        nova.custo_total = (
            nova.energia_kwh
            * nova.tarifa_kwh
        )


        self.sessoes.append(
            nova
        )


        energia_renovavel = (
            nova.energia_solar_kwh
            + nova.energia_bateria_kwh
        )


        percentual_renovavel = (
            energia_renovavel
            / nova.energia_kwh
        ) * 100


        print("\n=== SESSÃO REGISTRADA ===")

        print(
            "Veículo:",
            nova.veiculo
        )

        print(
            "Energia:",
            f"{nova.energia_kwh:.2f}",
            "kWh"
        )

        print(
            "Potência liberada:",
            f"{nova.potencia_liberada_kw:.2f}",
            "kW"
        )

        print(
            "Custo: R$",
            f"{nova.custo_total:.2f}"
        )

        print(
            "Uso de solar + bateria:",
            f"{percentual_renovavel:.2f}%"
        )

        print(
            "Pagamento:",
            nova.pagamento
        )


    # ========================================================
    # PAGAMENTO
    # ========================================================

    def realizar_pagamento(self):

        print("\n=== PAGAMENTO ===")

        if len(self.sessoes) == 0:

            print(
                "Nenhuma sessão cadastrada."
            )

            return


        try:

            id_sessao = int(
                input("ID da sessão: ")
            )

        except ValueError:

            print("ID inválido.")
            return


        sessao_encontrada = None


        for sessao in self.sessoes:

            if sessao.id_sessao == id_sessao:

                sessao_encontrada = sessao
                break


        if sessao_encontrada is None:

            print("Sessão não encontrada.")
            return


        if sessao_encontrada.pagamento == "Pago":

            print(
                "Essa sessão já está paga."
            )

            return


        print(
            "Valor: R$",
            f"{sessao_encontrada.custo_total:.2f}"
        )

        print("1 - PIX")
        print("2 - Cartão")
        print("3 - Aplicativo")


        metodo = input(
            "Forma de pagamento: "
        )


        metodos = {
            "1": "PIX",
            "2": "Cartão",
            "3": "Aplicativo"
        }


        if metodo not in metodos:

            print(
                "Forma de pagamento inválida."
            )

            return


        sessao_encontrada.pagamento = "Pago"


        print(
            "Pagamento aprovado via",
            metodos[metodo] + "."
        )


    # ========================================================
    # OTIMIZAÇÃO INTELIGENTE
    # ========================================================

    def otimizacao_inteligente(self):

        print("\n=== OTIMIZAÇÃO INTELIGENTE ===")


        percentual_demanda = (
            self.consumo_predio_kw
            / self.limite_demanda_kw
        ) * 100


        print(
            "Uso atual da demanda:",
            f"{percentual_demanda:.2f}%"
        )


        if percentual_demanda >= 80:

            print("\nRecomendação:")

            print(
                "- Reduzir a potência dos carregadores."
            )

            print(
                "- Adiar sessões não prioritárias."
            )

            print(
                "- Priorizar energia solar e bateria."
            )


        elif self.energia_solar_kwh >= 30:

            print("\nRecomendação:")

            print(
                "- Momento favorável para novas recargas."
            )

            print(
                "- Boa disponibilidade de energia solar."
            )


        elif self.bateria_kwh < 20:

            print("\nRecomendação:")

            print(
                "- Preservar a bateria."
            )

            print(
                "- Priorizar energia solar."
            )


        else:

            print(
                "Sistema operando em condições normais."
            )


    # ========================================================
    # STATUS
    # ========================================================

    def status_sistema(self):

        print("\n=== STATUS DO CHARGEGRID ===")

        print(
            "Limite de demanda:",
            self.limite_demanda_kw,
            "kW"
        )

        print(
            "Consumo do prédio:",
            self.consumo_predio_kw,
            "kW"
        )

        print(
            "Energia solar disponível:",
            f"{self.energia_solar_kwh:.2f}",
            "kWh"
        )

        print(
            "Bateria disponível:",
            f"{self.bateria_kwh:.2f}",
            "kWh"
        )

        print(
            "Carregadores cadastrados:",
            len(self.carregadores)
        )

        print(
            "Sessões registradas:",
            len(self.sessoes)
        )


    # ========================================================
    # RELATÓRIO
    # ========================================================

    def relatorio(self):

        print("\n=== RELATÓRIO CHARGEGRID ===")


        if len(self.sessoes) == 0:

            print(
                "Nenhuma sessão registrada."
            )

            return


        energia_total = 0.0
        solar_total = 0.0
        bateria_total = 0.0
        rede_total = 0.0
        faturamento = 0.0


        for sessao in self.sessoes:

            energia_total += sessao.energia_kwh

            solar_total += (
                sessao.energia_solar_kwh
            )

            bateria_total += (
                sessao.energia_bateria_kwh
            )

            rede_total += (
                sessao.energia_rede_kwh
            )

            faturamento += (
                sessao.custo_total
            )


        renovavel_total = (
            solar_total
            + bateria_total
        )


        percentual_renovavel = (
            renovavel_total
            / energia_total
        ) * 100


        print(
            "Sessões realizadas:",
            len(self.sessoes)
        )

        print(
            "Energia total:",
            f"{energia_total:.2f}",
            "kWh"
        )

        print(
            "Energia solar:",
            f"{solar_total:.2f}",
            "kWh"
        )

        print(
            "Energia da bateria:",
            f"{bateria_total:.2f}",
            "kWh"
        )

        print(
            "Energia da rede:",
            f"{rede_total:.2f}",
            "kWh"
        )

        print(
            "Participação de solar + bateria:",
            f"{percentual_renovavel:.2f}%"
        )

        print(
            "Faturamento simulado: R$",
            f"{faturamento:.2f}"
        )


        print("\nDetalhes das sessões:")


        for sessao in self.sessoes:

            print("\n------------------------------")

            print(
                "ID:",
                sessao.id_sessao
            )

            print(
                "Veículo:",
                sessao.veiculo
            )

            print(
                "Carregador:",
                sessao.carregador.identificacao
            )

            print(
                "Protocolo:",
                sessao.carregador.protocolo
            )

            print(
                "Energia:",
                f"{sessao.energia_kwh:.2f}",
                "kWh"
            )

            print(
                "Custo: R$",
                f"{sessao.custo_total:.2f}"
            )

            print(
                "Pagamento:",
                sessao.pagamento
            )


# ============================================================
# MENU PRINCIPAL
# ============================================================

def menu():

    sistema = ChargeGrid()


    while True:

        print("\n========================================")
        print("       CHARGEGRID INTELLIGENCE")
        print("       GOODWE CHALLENGE - SPRINT 3")
        print("========================================")

        print("1 - Cadastrar carregador")
        print("2 - Nova sessão de recarga")
        print("3 - Realizar pagamento")
        print("4 - Otimização inteligente")
        print("5 - Status do sistema")
        print("6 - Relatório")
        print("7 - Encerrar")


        opcao = input(
            "\nEscolha uma opção: "
        )


        if opcao == "1":

            sistema.cadastrar_carregador()


        elif opcao == "2":

            sistema.nova_sessao()


        elif opcao == "3":

            sistema.realizar_pagamento()


        elif opcao == "4":

            sistema.otimizacao_inteligente()


        elif opcao == "5":

            sistema.status_sistema()


        elif opcao == "6":

            sistema.relatorio()


        elif opcao == "7":

            print(
                "\nSistema encerrado."
            )

            break


        else:

            print(
                "\nOpção inválida."
            )


if __name__ == "__main__":
    menu()
