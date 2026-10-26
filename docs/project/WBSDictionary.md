# Dicionário do EAP:

**Versão**: 0.5
**Produto**: Syllabum - Tutor Educacional Inteligente
**Data de Publicação**: 22/10/2026
**Última Atualização**: 26/10/2026

## Estrutura Analítica do Projeto:

![Diagrama de EAP](../assets/diagrams/WBS.png)

## Dicionário de EAP:

### 1. Construção e Gerenciamento de Cursos:

| ID   | Pacote de Trabalho                                   | Descrição                                                                                                                                     |
| ---- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.1. | Estruturação de Briefing e Objetivos de Aprendizado. | Interface para coleta de briefing de necessidades do usuário, seus objetivos e atual nível de abstração.                                      |
| 1.2. | Geração de Escopo Simplificado de Curso.             | Orquestração de LLM para usar informações de usuário para gerar versões preliminares do curso e apresentar para usuário.                      |
| 1.3. | Avaliação de Escopo Simplificado de Curso.           | Interface de usuário para análise do Escopo Simplificado e identificar necessidade de alterações antes de prosseguir para a geração do curso. |
| 1.4. | Geração Completa de Tópicos de Curso.                | Orquestração de LLM para gerar todos os módulos e tópicos de acordo com o escopo aprovado pelo usuário.                                       |
| 1.5. | Painel Geral de Cursos.                              | Interface de usuário para facilitar visualização e interação com cursos do usuário, finalizados ou não.                                       |

### 2. Workspace de Aprendizado / Modo Tutor:

| ID   | Pacote de Trabalho                        | Descrição                                                                                                                                                              |
| ---- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.1. | Interação Contextualizada.                | Construção de diálogo com tutor vinculado ao tópico.                                                                                                                   |
| 2.2. | Tratamento de Perguntas e Respostas.      | Tutor adequado para responder perguntas do usuário e tratar desvios de contexto, guiando mensagens acordo com a Intercepção Socrática.                                 |
| 2.3. | Geração Dinâmica de Atividades.           | Orquestração de LLM para detectar necessidade de construção de atividades de fixação/revisão, com gabarito disponibilizado apenas após a primeira tentativa concluída.                         |
| 2.4. | Arquivamento de Workspace após Conclusão. | Após o conteúdo abordado ser dado como concluído, o diálogo com o Tutor daquele tópico é devidamente encerrado, permitido apenas para visualização, mas sem interação. |
| 2.5. | Histórico e Contexto.                     | Orquestração de LLM para facilitar a continuidade das interações em um tópico a partir de resumos estruturados de tópicos anteriores, consultados apenas mediante decisão do modelo..                                                                                         |

### 3. Assistência à Resolução de Problemas Técnicos / Modo Debugger:

| ID   | Pacote de Trabalho                           | Descrição                                                                                                                                                                                                    |
| ---- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 3.1. | Detecção de Intenção.                        | Orquestração de LLM para detectar intenção de usuário por ajuda em quesitos técnicos (envio de informações de traceback, bugs de código, linhas de código, etc.) para criar bifurcação para o Modo Debugger. |
| 3.2. | Toggle de Alternação entre Workspaces.       | Opção de usuário para alternar e iniciar diretamente a bifurcação com o Modo Debugger.                                                                                                                       |
| 3.3. | Workspace dedicado à Resolução de Problemas. | Interface de Usuário voltada especificamente para o atendimento de problemas técnicos (bugs, tracebacks, etc.).                                                                                              |
| 3.4. | Tratamento de Perguntas e Respostas.         | Técnico adequado para responder perguntas do usuário e tratar desvios de contexto.                                                                                                                           |
| 3.5. | Arquivamento de Workspace após Conclusão.    | Após o problema ser dado como solucionado, o Workspace de atendimento à problemas técnicos é encerrado e arquivado apenas para consultas posteriores, retornando novamente ao contexto da conversa com o Modo Tutor, de onde parou.                                                        |

### 4. Dashboard Geral de Desempenho:

| ID   | Pacote de Trabalho                 | Descrição                                                                                                                                                                                         |
| ---- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4.1. | Dashboard Geral de Desempenho      | Acompanhamento do desempenho do usuário com base em métricas de esforço ("streak", cursos concluídos, média temporal semanal, entre outros.).                                                     |
| 4.2. | Dashboard Específico de Desempenho | Acompanhamento do desempenho do usuário para determinado curso com base em métricas de esforço (progresso, atividades resolvidas, quantidade de Workspaces de Problemas Técnicos, entre outros.). |

### 5. Cadastro e Autenticação de Usuário:

| ID   | Pacote de Trabalho                           | Descrição                                                                                  |
| ---- | -------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 5.1. | Formulário de Cadastro de Usuário            | Coleta de informações necessárias e opcionais para registro de usuário.                    |
| 5.2. | Formulário de Login de Usuário               | Coleta de informações necessárias para login de usuário.                                   |
| 5.3. | Perfil de Usuário                            | Interface para visualização de informações do usuário cadastrado.                          |
| 5.4. | Recuperação de Senha (notificação por email) | Disparo automático de email para recuperação de senha do usuário.                          |
| 5.5. | Verificação de Email (notificação por email) | Disparo automático de email para verificação de email do usuário, após ser cadastrado.     |
| 5.6. | Segurança (uso de Access e Refresh Tokens)   | Utilização de Access e Refresh Tokens como técnicas de segurança e permanência de usuário. |

### 6. Preferências de Usuário:

| ID   | Pacote de Trabalho   | Descrição                                                                  |
| ---- | -------------------- | -------------------------------------------------------------------------- |
| 6.1. | Configurações Gerais | Interface para modificações gerais, de acordo com preferências de usuário. |
