import json
import datetime
import random

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from pyfiglet import figlet_format

console = Console()

contas = []


# ==========================================================
# TÍTULO GRANDE
# ==========================================================


def titulo_principal():

    texto = figlet_format("BANCO", font="small")

    console.print(Align.center(texto, vertical="middle"), style="bold cyan")


# ==========================================================
# PAINEL PRINCIPAL
# ==========================================================


def painel():

    while True:

        console.clear()

        titulo_principal()

        console.print(
            Panel(
                Align.center("[bold cyan]SISTEMA DE CONTA BANCÁRIA[/bold cyan]"),
                border_style="cyan",
                padding=(1, 4),
            )
        )

        console.print()

        console.print("[bold blue]1[/bold blue]  Cadastro")

        console.print("[bold blue]2[/bold blue]  Login")

        console.print("[bold blue]3[/bold blue]  Recuperar senha")

        console.print("[bold blue]4[/bold blue]  Consultar bancos")

        console.print("[bold red]5[/bold red]  Sair")

        console.print()

        escolha = input("Selecione a operação desejada para continuar: ")

        if escolha == "1":

            cadastro()

        elif escolha == "2":

            console.print(
                Panel(
                    "[yellow]Login ainda não implementado.[/yellow]",
                    title="LOGIN",
                    border_style="yellow",
                )
            )

            input("\nPressione ENTER para continuar...")

        elif escolha == "3":

            console.print(
                Panel(
                    "[yellow]Recuperação de senha ainda não implementada.[/yellow]",
                    title="RECUPERAÇÃO DE SENHA",
                    border_style="yellow",
                )
            )

            input("\nPressione ENTER para continuar...")

        elif escolha == "4":

            console.print(
                Panel(
                    "[yellow]Consulta de bancos ainda não implementada.[/yellow]",
                    title="CONSULTA DE BANCOS",
                    border_style="yellow",
                )
            )

            input("\nPressione ENTER para continuar...")

        elif escolha == "5":

            console.print(
                Panel(
                    "[bold green]Obrigado por utilizar o nosso serviço![/bold green]",
                    border_style="green",
                )
            )

            break

        else:

            console.print("[bold red]Escolha inválida![/bold red]")

            input("\nPressione ENTER para continuar...")


# ==========================================================
# CADASTRO
# ==========================================================


def cadastro():

    agencia = "0001"

    console.clear()

    titulo = figlet_format("CADASTRO", font="small")

    console.print(Align.center(titulo), style="bold cyan")

    console.print(
        Panel("[bold cyan]Criação de uma nova conta[/bold cyan]", border_style="cyan")
    )

    console.print()

    # ======================================================
    # NOME
    # ======================================================

    nome = input("Digite seu nome: ")

    # ======================================================
    # DATA DE NASCIMENTO
    # ======================================================

    data_nascimento = input(
        f"OK! {nome}. Digite sua data de nascimento " "(DD/MM/AAAA): "
    )

    # ======================================================
    # VALIDAR DATA
    # ======================================================

    try:

        data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y").date()

    except ValueError:

        console.print(
            Panel(
                "[bold red]Data inválida.[/bold red]\n" "Utilize o formato DD/MM/AAAA.",
                border_style="red",
            )
        )

        input("\nPressione ENTER para voltar...")
        return

    # ======================================================
    # CALCULAR IDADE
    # ======================================================

    hoje = datetime.date.today()

    idade = hoje.year - data_nascimento.year

    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):

        idade -= 1

    console.print()

    console.print(f"[bold cyan]Nome:[/bold cyan] {nome}")

    console.print(f"[bold cyan]Idade:[/bold cyan] {idade} anos")

    # ======================================================
    # VERIFICAR MAIORIDADE
    # ======================================================

    if idade < 18:

        console.print()

        console.print(
            Panel(
                "[bold red]Cadastro não permitido.[/bold red]\n"
                "É necessário possuir 18 anos ou mais.",
                border_style="red",
            )
        )

        input("\nPressione ENTER para voltar...")
        return

    # ======================================================
    # CRIAÇÃO DA SENHA
    # ======================================================

    while True:

        console.print()

        senha = input(
            "Defina sua senha de acesso "
            "(até 8 caracteres, com pelo menos "
            "1 letra maiúscula e 1 caractere especial): "
        )

        tem_maiuscula = False
        tem_especial = False

        # ==================================================
        # ANALISAR CADA CARACTERE
        # ==================================================

        for caractere in senha:

            if caractere.isupper():

                tem_maiuscula = True

            if not caractere.isalnum():

                tem_especial = True

        # ==================================================
        # VALIDAR SENHA
        # ==================================================

        if len(senha) <= 8 and tem_maiuscula and tem_especial:

            console.print("[bold green]Senha cadastrada com sucesso![/bold green]")

            break

        else:

            console.print(
                Panel(
                    "[bold red]Senha inválida.[/bold red]\n\n"
                    "• Máximo de 8 caracteres\n"
                    "• Pelo menos 1 letra maiúscula\n"
                    "• Pelo menos 1 caractere especial",
                    border_style="red",
                )
            )

    # ======================================================
    # GERAR CONTA
    # ======================================================

    num_conta = random.randint(100000000000, 999999999999)

    console.print()

    console.print(
        Panel(
            f"[bold green]Conta criada com sucesso![/bold green]\n\n"
            f"[bold]Número da conta:[/bold] {num_conta}\n"
            f"[bold]Agência:[/bold] {agencia}",
            title="DADOS DA CONTA",
            border_style="green",
        )
    )

    # ======================================================
    # CRIAR DICIONÁRIO
    # ======================================================

    conta = {
        "nome": nome,
        "data_nascimento": data_nascimento.strftime("%d/%m/%Y"),
        "idade": idade,
        "num_conta": num_conta,
        "agencia": agencia,
        "senha": senha,
    }

    # ======================================================
    # ADICIONAR À LISTA
    # ======================================================

    contas.append(conta)

    # ======================================================
    # SALVAR NO JSON
    # ======================================================

    with open("contas.json", "w") as arquivo:

        json.dump(contas, arquivo, indent=4)

    console.print()

    console.print(
        Panel(
            "[bold green]Cadastro realizado com sucesso![/bold green]",
            border_style="green",
        )
    )

    input("\nPressione ENTER para voltar ao painel...")


# ==========================================================
# INICIAR SISTEMA
# ==========================================================

painel()
