# SunLink — Classificados de Energia Renovável

## Sobre o Projeto

Este é um **projeto acadêmico** desenvolvido com fins **puramente educacionais**. O objetivo principal é o **aprendizado dos envolvidos**, servindo como exercício prático de programação em Python.

O SunLink é um sistema simples de classificados que conecta proprietários de terrenos a investidores interessados em projetos de energia renovável. Os dados são armazenados localmente em um arquivo de texto (`dados.txt`).

> ⚠️ Este projeto **não tem finalidade comercial** e não deve ser utilizado em ambiente de produção.

## Funcionalidades

- Adicionar anúncio (terreno ou investidor)
- Listar anúncios cadastrados
- Atualizar anúncio existente
- Excluir anúncio

## Pré-requisitos

- Python 3.8 ou superior

## Como Usar

### macOS

1. Abra o Terminal.
2. Verifique se o Python está instalado:
   ```bash
   python3 --version
   ```
   Se não estiver instalado, recomenda-se utilizar o [Homebrew](https://brew.sh):
   ```bash
   brew install python
   ```
3. Navegue até a pasta do projeto:
   ```bash
   cd caminho/para/sunlink
   ```
4. Execute o programa:
   ```bash
   python3 sunlink.py
   ```

### Linux (baseado em Debian)

1. Abra o Terminal.
2. Verifique se o Python está instalado:
   ```bash
   python3 --version
   ```
   Se não estiver instalado, instale via **apt**:
   ```bash
   sudo apt update
   sudo apt install python3
   ```
3. Navegue até a pasta do projeto:
   ```bash
   cd caminho/para/sunlink
   ```
4. Execute o programa:
   ```bash
   python3 sunlink.py
   ```

### Windows

1. Abra o **Prompt de Comando** (CMD) ou **PowerShell**.
2. Verifique se o Python está instalado:
   ```cmd
   python --version
   ```
   Se não estiver instalado, instale via **winget**:
   ```cmd
   winget install Python.Python.3.12
   ```
   Após a instalação, feche e reabra o terminal para que o `python` fique disponível no PATH.
3. Navegue até a pasta do projeto:
   ```cmd
   cd caminho\para\sunlink
   ```
4. Execute o programa:
   ```cmd
   python sunlink.py
   ```

## Estrutura do Projeto

```
sunlink/
├── sunlink.py    # Programa principal
├── dados.txt     # Arquivo de dados (criado automaticamente)
└── README.md     # Este arquivo
```

## Licença

Projeto acadêmico sem fins lucrativos. Uso livre para estudo e aprendizado.
