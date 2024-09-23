import csv
import os

filename = 'itens.csv'

def carregar_itens():
    itens = []
    if os.path.exists(filename):
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                itens.append(row)
    return itens

def salvar_itens(itens):
    with open(filename, mode='w', newline='') as file:
        fieldnames = itens[0].keys() if itens else ['id', 'nome', 'descricao', 'preco']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(itens)

def cadastrar_item(itens):
    id = input("Digite o ID do item: ")
    nome = input("Digite o nome do item: ")
    descricao = input("Digite a descrição do item: ")
    preco = input("Digite o preço do item: ")
    
    itens.append({'id': id, 'nome': nome, 'descricao': descricao, 'preco': preco})
    salvar_itens(itens)
    print("Item cadastrado com sucesso!")

def listar_itens(itens):
    if not itens:
        print("Nenhum item cadastrado.")
        return
    
    for item in itens:
        print(f"ID: {item['id']}, Nome: {item['nome']}, Descrição: {item['descricao']}, Preço: {item['preco']}")

def buscar_item(itens):
    nome = input("Digite o nome do item para buscar: ")
    encontrado = False
    
    for item in itens:
        if item['nome'].lower() == nome.lower():
            print(f"Item encontrado - ID: {item['id']}, Nome: {item['nome']}, Descrição: {item['descricao']}, Preço: {item['preco']}")
            encontrado = True
            break
    
    if not encontrado:
        print("Item não encontrado.")

def remover_item(itens):
    nome = input("Digite o nome do item para remover: ")
    encontrado = False
    
    itens[:] = [item for item in itens if item['nome'].lower() != nome.lower()]
    
    with open(filename, mode='w', newline='') as file:
        fieldnames = itens[0].keys() if itens else ['id', 'nome', 'descricao', 'preco']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(itens)
    
    if encontrado:
        print(f"Item '{nome}' removido com sucesso.")
    else:
        print("Item não encontrado.")

def main():
    itens = carregar_itens()
    
    while True:
        print("\nMenu:")
        print("1. Cadastrar item")
        print("2. Listar itens")
        print("3. Buscar item")
        print("4. Remover item")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            cadastrar_item(itens)
        elif escolha == "2":
            listar_itens(itens)
        elif escolha == "3":
            buscar_item(itens)
        elif escolha == "4":
            remover_item(itens)
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
