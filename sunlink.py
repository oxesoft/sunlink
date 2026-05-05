import os

# Nome do arquivo onde os dados serão salvos
ARQUIVO_DADOS = "dados.txt"

def carregar_dados():
    """
    Lê o arquivo de texto e retorna uma lista de dicionários.
    Cada dicionário representa um anúncio.
    """
    anuncios = []
    # Verifica se o arquivo existe antes de tentar abrir
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            for linha in f:
                # Remove espaços em branco e divide a linha pelo caractere '|'
                campos = linha.strip().split("|")
                if len(campos) == 7:
                    anuncio = {
                        "id": campos[0],
                        "tipo": campos[1],
                        "titulo": campos[2],
                        "localizacao": campos[3],
                        "area": campos[4],
                        "preco": campos[5],
                        "contato": campos[6]
                    }
                    anuncios.append(anuncio)
    return anuncios

def salvar_dados(anuncios):
    """
    Recebe a lista de anúncios e salva no arquivo de texto.
    """
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        for a in anuncios:
            # Junta os campos com '|' e escreve no arquivo
            linha = f"{a['id']}|{a['tipo']}|{a['titulo']}|{a['localizacao']}|{a['area']}|{a['preco']}|{a['contato']}\n"
            f.write(linha)

def adicionar_anuncio():
    print("\n--- Adicionar Novo Anúncio ---")
    anuncios = carregar_dados()
    
    # Gera um ID simples baseado no último ID da lista
    novo_id = "1"
    if anuncios:
        ultimo_id = int(anuncios[-1]["id"])
        novo_id = str(ultimo_id + 1)
    
    print("Selecione o tipo:")
    print("1. Terreno (Proprietário)")
    print("2. Investidor (Procura terreno)")
    opcao_tipo = input("Opção: ")
    tipo = "TERRENO" if opcao_tipo == "1" else "INVESTIDOR"
    
    titulo = input("Título do anúncio: ")
    localizacao = input("Localização (Cidade/Estado): ")
    area = input("Área (em hectares): ")
    preco = input("Preço (R$): ")
    contato = input("Contato (Telefone/Email): ")
    
    novo_anuncio = {
        "id": novo_id,
        "tipo": tipo,
        "titulo": titulo,
        "localizacao": localizacao,
        "area": area,
        "preco": preco,
        "contato": contato
    }
    
    anuncios.append(novo_anuncio)
    salvar_dados(anuncios)
    print("\n[Sucesso] Anúncio adicionado com sucesso!")

def listar_anuncios():
    print("\n--- Lista de Anúncios ---")
    anuncios = carregar_dados()
    
    if not anuncios:
        print("Nenhum anúncio cadastrado.")
        return

    # Exibe os anúncios de forma organizada
    for a in anuncios:
        print(f"ID: {a['id']} | [{a['tipo']}] {a['titulo']}")
        print(f"   Local: {a['localizacao']} | Área: {a['area']} ha | Preço: R$ {a['preco']}")
        print(f"   Contato: {a['contato']}")
        print("-" * 30)

def atualizar_anuncio():
    listar_anuncios()
    anuncios = carregar_dados()
    
    if not anuncios:
        return

    id_busca = input("\nDigite o ID do anúncio que deseja atualizar: ")
    encontrado = False
    
    for a in anuncios:
        if a["id"] == id_busca:
            print(f"\nEditando: {a['titulo']}")
            a["titulo"] = input(f"Novo Título (atual: {a['titulo']}): ") or a["titulo"]
            a["localizacao"] = input(f"Nova Localização (atual: {a['localizacao']}): ") or a["localizacao"]
            a["area"] = input(f"Nova Área (atual: {a['area']}): ") or a["area"]
            a["preco"] = input(f"Novo Preço (atual: {a['preco']}): ") or a["preco"]
            a["contato"] = input(f"Novo Contato (atual: {a['contato']}): ") or a["contato"]
            
            encontrado = True
            break
    
    if encontrado:
        salvar_dados(anuncios)
        print("\n[Sucesso] Anúncio atualizado!")
    else:
        print("\n[Erro] ID não encontrado.")

def excluir_anuncio():
    listar_anuncios()
    anuncios = carregar_dados()
    
    if not anuncios:
        return

    id_busca = input("\nDigite o ID do anúncio que deseja excluir: ")
    
    # Cria uma nova lista sem o anúncio que tem o ID informado
    novos_anuncios = [a for a in anuncios if a["id"] != id_busca]
    
    if len(novos_anuncios) < len(anuncios):
        salvar_dados(novos_anuncios)
        print("\n[Sucesso] Anúncio excluído!")
    else:
        print("\n[Erro] ID não encontrado.")

def menu_principal():
    """
    Função principal que controla o fluxo do programa.
    """
    while True:
        print("\n=== SunLink: Classificados de Energia Renovável ===")
        print("1. Adicionar Anúncio")
        print("2. Listar Anúncios")
        print("3. Atualizar Anúncio")
        print("4. Excluir Anúncio")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            adicionar_anuncio()
        elif opcao == "2":
            listar_anuncios()
        elif opcao == "3":
            atualizar_anuncio()
        elif opcao == "4":
            excluir_anuncio()
        elif opcao == "5":
            print("Encerrando o sistema... Até logo!")
            break
        else:
            print("[Erro] Opção inválida. Tente novamente.")

# Ponto de entrada do script
if __name__ == "__main__":
    menu_principal()
