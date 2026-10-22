# Dicionário do EAP:

**Versão**: 0.1
**Produto**: Syllabum - Tutor Educacional Inteligente
**Data de Publicação**: 22/10/2026

## Estrutura Analítica do Projeto:

![Diagrama de EAP](../assets/diagrams/EAP.png)

## Dicionário de EAP:

### 1. Construção e Gerenciamento de Cursos:

| ID   | Pacote de Trabalho                                  | Descrição                                                                                                                |
| ---- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 1.1. | Estruturação de Briefing e Objetivos de Aprendizado | Interface para coleta de briefing de necessidades do usuário, seus objetivos e atual nível de abstração.                 |
| 1.2. | Geração de Escopo Simplificado de Curso             | Orquestração de LLM para usar informações de usuário para gerar versões preliminares do curso e apresentar para usuário. |
| 1.3. | Geração de Tópicos de Curso                         | Orquestração de LLM para gerar módulos e tópicos específicos para diálogos com tutor virtual.                            |
| 1.4. | Painel Geral de Cursos                              | Interface de usuário para facilitar visualização e interação com cursos do usuário, finalizados ou não.                  |

### 2. Experiência de Aprendizagem:

| ID   | Pacote de Trabalho                        | Descrição                                                                                                                                                              |
| ---- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.1. | Workspace de Aprendizado para cada Tópico | Construção de ambiente de diálogo com IA Generativa                                                                                                                    |
| 2.2. | Modo Tutor (LLM)                          | Aprendizado do usuário pautado em técnicas pedagógicas inspiradas em técnicas e abstrações socrásticas.                                                                |
| 2.3. | Geração Dinâmica de Atividades            | Orquestração de LLM para detectar dificuldades e necessidades de revisão para viabilizar e facilitar o aprendizado.                                                    |
| 2.4. | Fechamento de Workspace após Conclusão    | Após o conteúdo abordado ser dado como concluído, o diálogo com o Tutor daquele tópico é devidamente encerrado, permitido apenas para visualização, mas sem interação. |

### 3. Assistência à Resolução de Problemas Técnicos:

| ID   | Pacote de Trabalho                          | Descrição                                                                                                                                             |
| ---- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3.1. | Workspace dedicado à Resolução de Problemas | Interface de Usuário voltada especificamente para o atendimento de problemas técnicos (bugs, tracebacks, etc.).                                       |
| 3.2. | Modo Debugger (LLM)                         | Orquestração de LLM para identificar e entender erros recorrentes de códigos, ensinando a solução através do Método Socrástico.                       |
| 3.3. | Fechamento de Workspace após Conclusão      | Após o problema ser dado como solucionado, o Workspace de atendimento à problemas técnicos é encerrado e arquivado apenas para consultas posteriores. |

### 4. Dashboard Geral de Desempenho:

| ID   | Pacote de Trabalho                 | Descrição                                                                                                                                                                                        |
| ---- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 4.1. | Dashboard Geral de Desempenho      | Acompanhamento do desempenho do usuário com base em métricas de esforço ("streak", cursos concluídos, média temporal semanal, entre outros.)                                                     |
| 4.2. | Dashboard Específico de Desempenho | Acompanhamento do desempenho do usuário para determinado curso com base em métricas de esforço (progresso, atividades resolvidas, quantidade de Workspaces de Problemas Técnicos, entre outros.) |

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

| ID   | Pacote de Trabalho       | Descrição                                                                 |
| ---- | ------------------------ | ------------------------------------------------------------------------- |
| 6.1. | Configurações Gerais     | Interface para modificações gerais, de acordo com preferências de usuário |
| 6.2. | Modo Claro / Modo Escuro | Alternação entre Modo Claro e Escuro                                      |
