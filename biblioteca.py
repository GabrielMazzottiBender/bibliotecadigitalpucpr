documentos = []

def cadastrar_documento():
    print("\n--- Cadastro de Documento ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    tipo = input("Tipo de documento (Artigo, Tese, Livro...): ")
    ano = input("Ano de publicação: ")
    formato = input("Formato (PDF, ePUB, etc.): ")

    documento = {
        "título": titulo,
        "autor": autor,
        "tipo": tipo,
        "ano": ano,
        "formato": formato
    }

    documentos.append(documento)
    print("Documento cadastrado com sucesso!")

def listar_documentos():
    print("\n--- Lista de Documentos ---")
    if not documentos:
        print("Nenhum documento cadastrado.")
    else:
        for i, doc in enumerate(documentos, start=1):
            print(f"{i}. {doc['título']} ({doc['tipo']}, {doc['ano']}) - {doc['formato']} | Autor: {doc['autor']}")

def listar_por_tipo_e_ano():
    print("\n--- Documentos Organizados por Tipo e Ano ---")
    if not documentos:
        print("Nenhum documento cadastrado.")
        return

    organizados = {}
    for doc in documentos:
        tipo = doc["formato"]
        ano = doc["ano"]
        if tipo not in organizados:
            organizados[tipo] = {}
        if ano not in organizados[tipo]:
            organizados[tipo][ano] = []
        organizados[tipo][ano].append(doc)

    for tipo, anos in organizados.items():
        print(f"\nFormato: {tipo}")
        for ano, docs in sorted(anos.items()):
            print(f"  Ano: {ano}")
            for doc in docs:
                print(f"    - {doc['título']} ({doc['tipo']}) | Autor: {doc['autor']}")

def renomear_documento():
    listar_documentos()
    try:
        indice = int(input("Digite o número do documento que deseja renomear: ")) - 1
        if 0 <= indice < len(documentos):
            novo_titulo = input("Digite o novo título: ")
            documentos[indice]["título"] = novo_titulo
            print("Título alterado com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

def remover_documento():
    listar_documentos()
    try:
        indice = int(input("Digite o número do documento que deseja remover: ")) - 1
        if 0 <= indice < len(documentos):
            removido = documentos.pop(indice)
            print(f"Documento '{removido['título']}' removido com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\n===== Biblioteca Digital =====")
        print("1. Cadastrar documento")
        print("2. Listar documentos")
        print("3. Listar por tipo e ano")
        print("4. Renomear documento")
        print("5. Remover documento")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_documento()
        elif escolha == "2":
            listar_documentos()
        elif escolha == "3":
            listar_por_tipo_e_ano()
        elif escolha == "4":
            renomear_documento()
        elif escolha == "5":
            remover_documento()
        elif escolha == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()