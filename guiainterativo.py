def layout():
    print("╔════════════════════════════════════════════════════╗")
    print("║                   DECIDA SEU FUTURO                ║")
    print("╚════════════════════════════════════════════════════╝")
    print("╔════════════════════════════════════════════════════╗")
    print("║  Seu guia para descobrir cursos e áreas de estudo  ║")
    print("╚════════════════════════════════════════════════════╝")


def resposta(pergunta, opcoes):
    print(pergunta)

    for num, opcao in opcoes.items():
        print(f"{num} - {opcao}")

    escolha = ""

    while escolha not in opcoes:
        escolha = input("Sua escolha: ")

        if escolha not in opcoes:
            print("Opção inválida, tente novamente.")

    return escolha


def area_estudos():
    layout()

    opcoes1 = {
        "1": "├── Resolver problemas lógicos",
        "2": "├── Entender a vida e os seres vivos",
        "3": "├── Pensar sobre a sociedade e cultura",
        "4": "├── Criar ou expressar ideias com arte",
        "5": "├── Ensinar ou ajudar pessoas a aprender",
        "6": "└── Empreender ou planejar negócios"
    }

    resposta1 = resposta("\nO que você prefere fazer?", opcoes1)

    if resposta1 == "1":

        opcoes2 = {
            "1": "├── Tecnologia e computadores",
            "2": "└── Cálculos, estruturas e construções"
        }

        resposta2 = resposta("\nVocê prefere:", opcoes2)

        if resposta2 == "1":
            area = "Computação"
            curso = "Ciência da Computação"
        else:
            area = "Exatas"
            curso = "Engenharia"

    elif resposta1 == "2":

        opcoes2 = {
            "1": "├── Cuidar da saúde das pessoas",
            "2": "└── Estudar organismos e a natureza"
        }

        resposta2 = resposta("\nVocê prefere:", opcoes2)

        if resposta2 == "1":
            area = "Ciências da Saúde"
            curso = "Medicina"
        else:
            area = "Ciências Biológicas"
            curso = "Biologia"

    elif resposta1 == "3":

        opcoes2 = {
            "1": "├── Leis, justiça e argumentação",
            "2": "└── Comportamento humano e sociedade"
        }

        resposta2 = resposta("\nVocê prefere:", opcoes2)

        if resposta2 == "1":
            area = "Ciências Humanas e Sociais"
            curso = "Direito"
        else:
            area = "Ciências Humanas"
            curso = "Psicologia"

    elif resposta1 == "4":

        opcoes2 = {
            "1": "├── Desenho e formas visuais",
            "2": "└── Música ou performance"
        }

        resposta2 = resposta("\nVocê prefere:", opcoes2)

        if resposta2 == "1":
            area = "Artes e Design"
            curso = "Design ou Artes Visuais"
        else:
            area = "Artes Cênicas e Música"
            curso = "Música ou Teatro"

    elif resposta1 == "5":

        opcoes2 = {
            "1": "├── Ensinar crianças",
            "2": "└── Ensinar jovens e adultos"
        }

        resposta2 = resposta("\nVocê prefere:", opcoes2)

        if resposta2 == "1":
            area = "Educação e Gestão Escolar"
            curso = "Pedagogia"
        else:
            area = "Ensino de disciplinas específicas"
            curso = "Licenciatura em área específica"

    else:

        opcoes2 = {
            "1": "├── Administrar empresas e pessoas",
            "2": "└── Criar negócios e estratégias"
        }

        resposta2 = resposta("\nVocê prefere:", opcoes2)

        if resposta2 == "1":
            area = "Administração e Gestão"
            curso = "Administração"
        else:
            area = "Empreendedorismo e Negócios"
            curso = "Administração ou Gestão de Negócios"

    print()
    print("        ┌──────────────────────────────────────────┐")
    print(f"        ├── Área de estudo sugerida: {area}")
    print(f"        └── Curso sugerido: {curso}")
    print()
    print("════════════════════════════════════════════════════")


area_estudos()