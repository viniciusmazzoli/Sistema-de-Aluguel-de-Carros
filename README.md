# 🚗 Sistema de Aluguel de Carros

![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django )
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python )
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite )
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap )

Projeto acadêmico desenvolvido para a disciplina de Laboratório de Desenvolvimento de Software. Trata-se de uma aplicação web completa para gestão de aluguéis de automóveis, construída com o framework Django.

---

## 📊 Diagramas e Planejamento

### Diagrama de Caso de Uso
![Diagrama de Caso de Uso](https://github.com/viniciusmazzoli/Sistema-de-Aluguel-de-Carros/blob/main/diagramas/DiagramaDeCasoDeUso2.png )

### Histórias de Usuário
| ID    | Como (ator)                  | Eu quero                                                                                   | Para que                                                                                         |
|-------|------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| US-01 | Cliente                      | Me cadastrar no sistema informando meus dados pessoais (RG, CPF, Nome, Endereço), profissão, empregadores e rendimentos | Ter acesso às funcionalidades do sistema                                                         |
| US-02 | Cliente                      | Autenticar meu login e senha                                                               | Acessar meus pedidos e contratos com segurança                                                   |
| US-03 | Agente (empresa ou banco)    | Acessar o sistema mediante autenticação                                                    | Avaliar e modificar pedidos de clientes                                                          |
| US-04 | Cliente                      | Registrar um pedido de aluguel de automóvel                                                | Solicitar a contratação de um veículo                                                            |
| US-05 | Cliente                      | Modificar um pedido já realizado                                                           | Corrigir ou ajustar os dados do pedido                                                           |
| US-06 | Cliente                      | Cancelar um pedido de aluguel                                                              | Desistir da contratação antes da aprovação                                                       |
| US-07 | Cliente                      | Consultar meus pedidos realizados                                                          | Acompanhar o status de cada solicitação                                                          |
| US-08 | Agente financeiro (banco)    | Analisar os dados financeiros do cliente e do pedido                                       | Verificar se ele tem condições de honrar o contrato                                               |
| US-09 | Agente (empresa/banco)       | Modificar pedidos de clientes                                                              | Corrigir informações inconsistentes antes da aprovação                                            |
| US-10 | Agente (empresa/banco)       | Avaliar os pedidos e emitir parecer positivo ou negativo                                   | Garantir que apenas contratos viáveis avancem para execução                                       |
| US-11 | Cliente                      | Visualizar meus contratos aprovados                                                        | Acompanhar as condições do aluguel                                                               |

---

## 🎬 Demonstração do Sistema

### Fluxo Principal (Cliente e Agente)
![Demonstração do Sistema de Aluguel](VideoProjeto/GifVideoApresentacaoSistema.gif)

### Área Administrativa (Django Admin)
![Demonstrativo da Area Administrador do Sistema](VideoProjeto/ExecucaoAreaAdminGif.gif)

---

## 📋 Funcionalidades Principais

O sistema foi projetado para atender a dois tipos de usuários: **Clientes** e **Agentes**, cada um com suas próprias permissões e painéis de controle.

### Para Clientes:
-   ✅ **Cadastro e Autenticação:** Criação de conta e login seguro.
-   🚗 **Catálogo de Veículos:** Visualização dos carros disponíveis para aluguel.
-   📝 **Solicitação de Aluguel:** Processo simplificado para fazer um novo pedido.
-   📊 **Dashboard Pessoal:** Acompanhamento em tempo real do status de todos os pedidos (`Em análise`, `Aprovado`, `Reprovado`, `Cancelado`).
-   ❌ **Cancelamento de Pedidos:** Possibilidade de cancelar um pedido que ainda não foi avaliado pelo agente.

### Para Agentes:
-   ✅ **Autenticação Segura:** Login em um painel de controle exclusivo para agentes.
-   🔍 **Dashboard de Avaliação:** Visualização de todos os pedidos de clientes que estão pendentes de análise.
-   👍 **Aprovação de Pedidos:** Capacidade de aprovar uma solicitação, o que automaticamente gera um contrato no sistema.
-   👎 **Reprovação de Pedidos:** Capacidade de reprovar uma solicitação, com a opção de deixar um parecer.
-   🗂️ **Gestão de Veículos:** CRUD completo para adicionar, visualizar, editar e remover automóveis do sistema.

---

## 🛠️ Tecnologias Utilizadas

*   **Backend:**
    *   **Python:** Linguagem principal do projeto.
    *   **Django:** Framework web robusto para desenvolvimento rápido e seguro.
    *   **SQLite:** Banco de dados padrão para desenvolvimento com Django.
*   **Frontend:**
    *   **HTML5** e **CSS3**.
    *   **Bootstrap 5:** Framework CSS para criar interfaces responsivas e modernas.
*   **Controle de Versão:**
    *   **Git** & **GitHub**.

---

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e rodar o ambiente de desenvolvimento.

**1. Pré-requisitos:**
   - Ter o [Python 3.10+](https://www.python.org/downloads/ ) instalado.
   - Ter o [Git](https://git-scm.com/downloads ) instalado.

**2. Clone o Repositório:**
   ```bash
   git clone https://github.com/viniciusmazzoli/Sistema-de-Aluguel-de-Carros.git
   cd Sistema-de-Aluguel-de-Carros
