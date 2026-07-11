# Guia de Entrega — Passo a Passo

Este guia cobre exatamente as partes que **precisam ser feitas por você**,
pessoalmente, na sua conta do GitHub (criar o repositório, o quadro Kanban,
os commits reais e o vídeo). O código, os testes, o pipeline de CI e o
documento teórico já estão prontos nesta entrega.

---

## 1. Criar o repositório no GitHub

1. Acesse https://github.com/new
2. Nome sugerido: `techflow-taskmanager`
3. Visibilidade: **Public** (obrigatório pelo enunciado)
4. NÃO marque "Add a README" (você já tem um pronto) — deixe o repositório vazio.
5. Clique em **Create repository**.

No seu terminal, dentro da pasta `techflow-taskmanager` que você recebeu:

```bash
cd techflow-taskmanager
git init
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/techflow-taskmanager.git
```

---

## 2. Criar o quadro Kanban (GitHub Projects)

1. No repositório, clique na aba **Projects** → **New project**.
2. Escolha o template **Board**.
3. Renomeie as colunas para: `A Fazer`, `Em Progresso`, `Concluído`.
4. Crie pelo menos 10 cards (itens), por exemplo:
   - Modelar diagrama de casos de uso
   - Modelar diagrama de classes
   - Implementar modelo `Task`
   - Implementar `TaskRepository` (CRUD)
   - Implementar rotas da API REST
   - Implementar interface HTML do Kanban
   - Escrever testes unitários (`test_models.py`)
   - Escrever testes de integração (`test_app.py`)
   - Configurar pipeline de CI (GitHub Actions)
   - Escrever README.md
   - **Priorizar tarefas críticas (mudança de escopo)** ← este card representa a gestão de mudanças
5. Distribua os cards entre as 3 colunas — deixe 2 ou 3 ainda em "A Fazer" ou
   "Em Progresso" para o quadro parecer realista (nem tudo pronto de uma vez).

---

## 3. Sequência de commits sugerida (mínimo 10)

Copie os arquivos desta entrega para dentro do repositório clonado e vá
commitando **aos poucos**, na ordem abaixo, para simular um desenvolvimento
real (não faça um único commit gigante):

```bash
# 1
git add README.md .gitignore
git commit -m "docs: adiciona README inicial com objetivo e escopo do projeto"

# 2
git add src/models.py
git commit -m "feat: implementa modelo Task e repositório em memória"

# 3
git add src/app.py
git commit -m "feat: implementa API REST de CRUD de tarefas com Flask"

# 4
git add src/templates/index.html
git commit -m "feat: adiciona interface web do quadro Kanban"

# 5
git add requirements.txt
git commit -m "chore: adiciona arquivo de dependencias do projeto"

# 6
git add tests/test_models.py
git commit -m "test: adiciona testes unitarios do repositorio de tarefas"

# 7
git add tests/test_app.py
git commit -m "test: adiciona testes de integracao da API REST"

# 8
git add .github/workflows/ci.yml
git commit -m "ci: configura pipeline de integracao continua com GitHub Actions"

# 9
git add docs/use_case_diagram.svg docs/use_case_diagram.png docs/class_diagram.svg docs/class_diagram.png
git commit -m "docs: adiciona diagramas UML de casos de uso e de classes"

# --- Aqui entra a mudança de escopo (mova o card no Kanban para "Em Progresso") ---

# 10
git add src/models.py
git commit -m "feat: adiciona priorizacao de tarefas criticas (mudanca de escopo)"

# 11
git add README.md
git commit -m "docs: documenta justificativa da mudanca de escopo no README"

git push -u origin main
```

> Dica: os commits 10 e 11 já estão refletidos no código desta entrega
> (o campo `priority` já existe em `models.py` e a justificativa já está no
> README). Você pode reproduzir esse histórico fazendo o commit inicial
> **sem** o campo `priority` e depois um segundo commit **adicionando** o
> campo, para que o histórico do Git mostre a mudança de fato acontecendo.
> Se preferir simplicidade, tudo bem commitar já com a funcionalidade
> completa — o importante é ter o card específico no Kanban e a
> justificativa no README.

Depois de cada push, acesse a aba **Actions** do repositório e confirme que
o workflow `CI - Testes Automatizados` rodou com sucesso (ícone verde ✅).

---

## 4. Prints para o documento teórico

No arquivo `docs/Documento_Teorico_TechFlow_TaskManager.docx`, substitua os
três parágrafos marcados em itálico cinza na Seção 7 pelos prints reais:

1. Print do quadro Kanban em **Projects**.
2. Print do histórico de **commits**.
3. Print da aba **Actions** com o workflow rodando (verde).

Adicione uma legenda curta abaixo de cada print explicando o que ela mostra.

---

## 5. Roteiro do vídeo pitch (até 4 minutos)

Sugestão de estrutura, com tempos aproximados:

| Tempo | Conteúdo |
|---|---|
| 0:00–0:30 | Apresentação do projeto: contexto da TechFlow Solutions e da startup de logística, objetivo do sistema. |
| 0:30–1:15 | Metodologia ágil: mostre o quadro Kanban no GitHub Projects, explique as 3 colunas e como as tarefas fluem entre elas. |
| 1:15–2:15 | Demonstração do sistema funcionando: rode `python app.py`, mostre a interface criando/movendo tarefas, incluindo uma tarefa `critical`. |
| 2:15–2:50 | Testes automatizados: mostre o arquivo `tests/` e rode `pytest -v` ao vivo, mostrando os testes passando. |
| 2:50–3:20 | GitHub Actions: mostre a aba Actions com o workflow verde após um push. |
| 3:20–3:45 | Mudança de escopo: explique o que motivou a adição da priorização e mostre o commit/card correspondente. |
| 3:45–4:00 | Reflexão final sobre a importância da Engenharia de Software (versionamento, testes, CI) no mercado de trabalho. |

Grave a tela (ex.: OBS Studio, ou a gravação nativa do Windows/Mac) e publique
no YouTube (pode ser "não listado") ou no Google Drive com link público de
visualização.

---

## 6. Checklist final antes de entregar

- [ ] Repositório público no GitHub com README.md completo
- [ ] Quadro Kanban em Projects com ≥10 cards nas 3 colunas
- [ ] ≥10 commits com mensagens descritivas
- [ ] Sistema funcional (CRUD) rodando localmente
- [ ] Testes automatizados implementados e passando
- [ ] GitHub Actions configurado e rodando com sucesso
- [ ] Mudança de escopo simulada (card + commit + explicação no README)
- [ ] Documento teórico (DOCX/PDF) com os 2 diagramas UML e os 3 prints comentados
- [ ] Vídeo pitch gravado e publicado com link público (até 4 minutos)
