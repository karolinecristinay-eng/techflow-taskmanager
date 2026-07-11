# TechFlow TaskManager

Sistema de gerenciamento de tarefas desenvolvido pela **TechFlow Solutions**
para uma startup de logística, permitindo acompanhar o fluxo de trabalho em
tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe.

Projeto acadêmico da disciplina de Engenharia de Software, aplicando
conceitos de metodologias ágeis, versionamento, testes automatizados e
integração contínua em um ciclo de desenvolvimento realista.

## 🎯 Objetivo e escopo

Construir um sistema web simples de CRUD (Create, Read, Update, Delete) de
tarefas que sirva de base para uma equipe ágil acompanhar seu trabalho,
com:

- Cadastro, listagem, atualização e remoção de tarefas.
- Organização visual por status (`A Fazer`, `Em Progresso`, `Concluído`),
  espelhando o quadro Kanban do GitHub Projects.
- Priorização de tarefas críticas (ver seção "Gestão de Mudanças" abaixo).

## 🧭 Metodologia ágil adotada

O projeto foi conduzido com **Kanban**, por ser o método mais aderente ao
tipo de trabalho (fluxo contínuo, sem sprints fixos), utilizando o **GitHub
Projects** como ferramenta de gestão visual, com três colunas:

| A Fazer | Em Progresso | Concluído |
|---|---|---|
| Backlog priorizado de funcionalidades | Itens sendo implementados no momento | Itens já entregues e testados |

Cada card do quadro corresponde a uma *issue*/tarefa técnica, e cada entrega
foi versionada através de commits pequenos e frequentes, seguindo o
princípio ágil de entregas incrementais.

## 🏗️ Arquitetura e estrutura de diretórios

```
techflow-taskmanager/
├── app.py                 # Camada web (Flask): rotas da API REST e da UI
├── models.py              # Camada de domínio: Task e TaskRepository (regra de negócio)
├── templates/
│   └── index.html         # Interface simples do quadro Kanban
├── tests/
│   ├── test_models.py     # Testes unitários da regra de negócio
│   └── test_app.py        # Testes de integração da API REST
├── docs/                  # Diagramas UML e documentação complementar
├── requirements.txt
└── README.md
```

A separação entre `models.py` (regra de negócio) e `app.py` (camada web)
segue o princípio de **separação de responsabilidades**, facilitando os
testes unitários independentemente do framework web.

## 🚀 Como executar o sistema

```bash
# 1. Clonar o repositório
git clone <URL_DO_SEU_REPOSITORIO>
cd techflow-taskmanager

# 2. Criar ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Rodar a aplicação
python app.py
```

Acesse **http://127.0.0.1:5000** no navegador para ver o quadro Kanban.

A API REST fica disponível em `/api/tasks`:

| Método | Rota | Descrição |
|---|---|---|
| GET | `/api/tasks` | Lista todas as tarefas (filtros opcionais `?status=` e `?priority=`) |
| POST | `/api/tasks` | Cria uma nova tarefa |
| GET | `/api/tasks/<id>` | Consulta uma tarefa específica |
| PUT | `/api/tasks/<id>` | Atualiza uma tarefa |
| DELETE | `/api/tasks/<id>` | Remove uma tarefa |

## ✅ Testes automatizados e controle de qualidade

O projeto usa **Pytest** para testes unitários (regra de negócio) e de
integração (API). Para rodar localmente:

```bash
pip install -r requirements.txt
pytest -v
```

Uma pipeline de **Integração Contínua** pode ser adicionada com GitHub Actions
ou outra ferramenta, garantindo que os testes sejam executados a cada `push`
ou `pull request` na branch `main`.

## 🔄 Gestão de Mudanças (alteração de escopo)

**Justificativa:** durante o desenvolvimento, identificou-se que o escopo
inicial (CRUD simples de tarefas com apenas título, descrição e status) não
atendia por completo ao requisito do cliente de **"priorizar tarefas
críticas"**, citado no desafio original. Uma equipe de logística lida com
prazos e urgências diferentes a cada tarefa (ex.: atraso de entrega vs.
ajuste de rotina), e sem um campo de prioridade essa diferenciação era
impossível.

**Mudança implementada:** adição do campo `priority` (`low`, `medium`,
`high`, `critical`) ao modelo `Task`, com:
- Validação de valores permitidos (`ValidationError` em caso de valor
  inválido).
- Ordenação automática da listagem de tarefas por prioridade, para que
  tarefas críticas apareçam sempre no topo do quadro.
- Testes automatizados cobrindo a nova regra (`test_list_all_orders_by_priority`,
  `test_create_task_invalid_priority_raises`, entre outros).

**Como foi conduzida a mudança no processo ágil:**
1. Criação de um novo card no quadro Kanban (coluna "A Fazer") descrevendo a
   necessidade.
2. Movimentação do card para "Em Progresso" durante a implementação.
3. Commit dedicado implementando a funcionalidade (`feat: adiciona
   priorização de tarefas críticas`).
4. Atualização deste README com a justificativa (você está lendo agora).
5. Card movido para "Concluído" após os testes passarem no pipeline de CI.

Essa dinâmica demonstra, na prática, como um projeto conduzido com Kanban
absorve mudanças de escopo sem comprometer o que já foi entregue — um dos
principais diferenciais das metodologias ágeis frente a modelos em cascata.

## 👥 Papéis e beneficiários

- **Equipe de desenvolvimento:** acompanha o andamento técnico e organiza o
  próprio fluxo de trabalho pelo quadro Kanban.
- **Gestor de projeto / Product Owner:** monitora o progresso geral e
  identifica gargalos observando a distribuição de cards entre as colunas.
- **Cliente (startup de logística):** ganha visibilidade sobre o que está
  sendo feito e pode confiar que tarefas críticas (ex.: falhas na entrega)
  são tratadas com prioridade.

## 🛠️ Tecnologias utilizadas

- **Python 3.11** + **Flask** — API REST e interface web.
- **Pytest** — testes automatizados (unitários e de integração).
- **GitHub Projects** — quadro Kanban de gestão ágil.
- **GitHub Actions** — pipeline de integração contínua (CI).

## 📄 Licença

Projeto acadêmico, sem fins comerciais.
