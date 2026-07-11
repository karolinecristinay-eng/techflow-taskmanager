# Quadro Kanban — TechFlow TaskManager (5 etapas)

Versão expandida do quadro Kanban, com 5 colunas em vez de 3, para refletir
com mais granularidade o fluxo de trabalho da equipe: itens ainda não
priorizados (Backlog), o que está planejado (A Fazer), o que está sendo
implementado (Em Progresso), o que está em validação (Em Revisão / Testes)
e o que já foi entregue (Concluído).

Copie o conteúdo abaixo para a aba **Projects** do seu repositório
(https://github.com/karolinecristinay-eng/techflow-taskmanager).

---

## 🗂️ Backlog

- [ ] Persistir dados em banco de dados (SQLite)
- [ ] Adicionar autenticação de usuários (login)
- [ ] Adicionar filtro de tarefas por data de criação

## 📋 A Fazer

- [ ] Gravar vídeo pitch de apresentação do projeto
- [ ] Revisar comentários no código-fonte

## 🔧 Em Progresso

- [ ] Configurar pipeline de CI (GitHub Actions)

## 🔍 Em Revisão / Testes

- [ ] **Priorizar tarefas críticas (mudança de escopo)** — em validação pelos testes automatizados
- [ ] Revisão de código do módulo `models.py`

## ✅ Concluído

- [x] Modelar diagrama de casos de uso
- [x] Modelar diagrama de classes
- [x] Implementar modelo `Task` (CRUD)
- [x] Implementar rotas da API REST
- [x] Implementar interface HTML
- [x] Escrever testes unitários
- [x] Escrever testes de integração
- [x] Escrever README.md
- [x] Escrever GUIA_DE_ENTREGA.md

---

### Por que 5 etapas em vez de 3?

O enunciado pede no mínimo as 3 colunas básicas (A Fazer, Em Progresso,
Concluído), mas um quadro com 5 colunas deixa mais claro o **controle de
qualidade** do processo: nada vai direto de "Em Progresso" para "Concluído"
sem passar por uma etapa explícita de revisão/teste — o que conecta
diretamente com a Seção 6 do documento teórico (testes automatizados) e com
o pipeline de CI.

### Observação importante

No momento desta entrega, o repositório real
(https://github.com/karolinecristinay-eng/techflow-taskmanager) possui 11
commits, mas ainda **não tem** o arquivo `.github/workflows/ci.yml` nem um
quadro Projects criado. Ambos foram incluídos nesta entrega
(`techflow-taskmanager.zip`) para você adicionar/commitar. Depois de
enviar o `ci.yml` e criar o quadro no Projects com os cards acima, tanto a
aba **Actions** quanto o quadro **Kanban** do seu repositório vão refletir
exatamente o que está documentado no PDF.
