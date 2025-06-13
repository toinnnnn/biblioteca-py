# 📚 Biblioteca - Sistema de Empréstimo de Livros

Este projeto implementa um sistema de gerenciamento de uma biblioteca utilizando os princípios **SOLID**, com foco em **design orientado a objetos**, **tratamento de erros**, **testes unitários** e **diagrama de classes UML**.

## ✅ Funcionalidades

- Cadastro de livros e usuários
- Empréstimo e devolução de livros
- Cálculo de multas
- Tratamento de erros robusto
- Testes unitários com `unittest`
- Arquitetura modular e clara
- Diagrama UML (estrutura e relacionamentos)

## 🧱 Estrutura do Projeto

```
biblioteca_completa/
│
├── main.py                  # Exemplo de uso da biblioteca
├── models/
│   ├── livro.py             # Classe Livro
│   ├── usuario.py           # Classe Usuario
│   ├── emprestimo.py        # Classe Emprestimo
│   └── biblioteca.py        # Classe Biblioteca (regra de negócio)
│
├── exceptions/
│   └── erros.py             # Exceções customizadas
│
├── tests/
│   └── test_biblioteca.py   # Testes unitários
│
├── uml_diagrama.txt         # Diagrama UML da solução
└── README.md                # Este arquivo
```

## ▶️ Como Executar

1. **Clonar ou baixar o repositório**  
   Baixe o `.zip` ou clone este projeto.

2. **Executar o script principal**  
   ```bash
   python main.py
   ```

3. **Executar os testes unitários**  
   No terminal, rode:
   ```bash
   python -m unittest tests/test_biblioteca.py
   ```

## 🧪 Exemplo de Testes

Testes validam:

- Cadastro de usuários e livros
- Empréstimos e devoluções corretos
- Multas para livros não devolvidos
- Tratamento de erros esperados

## 📈 Diagrama UML

O diagrama `uml_diagrama.txt` descreve as classes e relações entre elas:

- `Biblioteca` usa `Livro`, `Usuario` e `Emprestimo`
- `Emprestimo` possui relação entre um `Usuario` e um `Livro`

## 💡 Tecnologias e Conceitos Aplicados

- Python 3.x
- POO (Programação Orientada a Objetos)
- SRP (Responsabilidade Única)
- Tratamento de exceções
- `unittest` para testes
- Diagrama UML textual
