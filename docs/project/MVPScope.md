# Escopo do MVP:

- **Versão**: 0.4
- **Produto**: Syllabum - Tutor Educacional Inteligente
- **Data de Elaboração:**: 21/10/2026
- **Última Atualização**: 26/10/2026

## Objetivo do MVP:

O Syllabum permitirá validar ou não a viabilidade técnica e pedagógica de um ambiente com geração dinâmica de trilhas orientadas a objetivos, com acompanhamento em tempo real por Inteligências Artificiais Generativas, sem depender de entregas de respostas prontas.

## Funcionalidades do MVP:

Inspirando-se no **Método MoSCoW** ("Must-Have, Should-Have, Could-Have e Won't Have"):

| Categorias de Prioridade | Módulo                                      | Descrição                                                                                                                                                                                   |
| ------------------------ | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Must-Have                | Cadastro de Usuário                         | Interface para o usuário cadastrar suas informações para começar a utilizar o sistema.                                                                                                      |
| Must-Have                | Autenticação de Usuário                     | Interface para o usuário inserir suas informações para poder utilizar o sistema e ter acesso a seus próprios cursos e atividades, com segurança regida por uso de Tokens criptografados.    |
| Must-Have                | Verificação de Email                        | No ato de cadastro, um email de verificação com tempo limitado é enviado para o email cadastrado do usuário.                                                                                |
| Must-Have                | Recuperação de Senha                        | Caso o usuário esqueça sua senha de acesso, um email de recuperação de senha é enviado para o email cadastrado do usuário.                                                                  |
| Must-Have                | Entrada e Avaliação de Perfil               | Interface para o usuário declarar um briefing de seus objetivos de estudo e nível atual.                                                                                                    |
| Must-Have                | Gerador de Trilha / Roadmap de Aprendizado  | Orquestração de LLM para transformar o objetivo do usuário em um conjunto de Módulos e Tópicos Estruturados.                                                                                |
| Must-Have                | Workspace de Aprendizado                    | Instanciação de um chat dedicado a cada tópico da trilha, permitindo injeção de System Prompts dedicados a instigar o raciocínio, pedir esclarecimentos e guiar o aluno.                    |
| Must-Have                | Alternação entre Modo Tutor e Modo Debugger | Orquestração de LLM para conduzir um chamado para um workspace dedicado à resolução de problemas técnicos (bugs, erros, etc.).                                                              |
| Must-Have                | Gerador Dinâmico de Atividades              | Orquestração de LLM para detecção de dificuldades, necessidades de revisão ou solicitação direta do próprio usuário, transformando esse requisito em um conjunto estruturado de atividades. |
| Should-Have              | Acompanhamento de Desempenho Geral          | Desenvolvimento de um Dashboard que avalia o desempenho geral do usuário por métricas temporais (diárias, semanais, mensais, etc.).                                                         |
| Should-Have              | Acompanhamento de Desempenho Especifico     | Desenvolvimento de um Dashboard que avalia o desempenho do usuário para algum curso específico.                                                                                             |
| Should-Have              | Configurações e Preferências de Usuário     | Interface para o usuário modificar e testar capacidades do sistema de acordo com próprias preferências.                                                                                     |
| Won't Have               | Importação e Exportação de Arquivos         | Orquestração de LLM para leitura e elaboração de documentos (imagens, PDFs, etc.).                                                                                                          |
| Won't Have               | Sistema de Gamificação                      | Elaboração de um esquema de pontuação pública (badges, rankings) entre alunos.                                                                                                              |
| Won't Have               | Compartilhamento de Cursos                  | Um aluni pode compartilhar com outros usuários a autorização de visualização e interação com o curso.                                                                                       |

## Regras de Negócio Fundamentais (Business Rules):

| ID    | Regra de Negócio                                  | Módulo Afetado          | Descrição do Comportamento Esperado                                                                                                                                                                                                                                             |
| ----- | ------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RN-01 | Isolamento de Contexto de Chat                    | Workspaces              | Cada tópico da trilha possui um histórico de chat isolado. As mensagens de um tópico nunca são enviadas na janela de contexto (prompt) para tópicos subsequentes, com exceção de resumos estruturados com principais abstrações de tópicos (dificuldades detectadas, conceitos aprendidos, etc.), consultados apenas para contextualização e mediante decisão do modelo.                                                           |
| RN-02 | Bloqueio de Tópicos Futuros                       | Workspaces              | Novos tópicos são liberados para interações apenas quando tópicos anteriores são devidamente concluídos.                                                                                                                                                                        |
| RN-03 | Conclusão de Tópico                               | Workspaces              | Um tópico é dado como concluído apenas quando o estudante confirma que o encerrou e não possui atividades pendentes.                                                                                                                                                            |
| RN-04 | Intercepção Socrática de Código                   | Engine de IA (Tutor)    | O tutor tem liberdade para apresentar exemplos de códigos livremente, desde que no intuito de aprendizado, mas, no que tanger atividades geradas, o gabarito só é disponibilizado quando o usuário completar sua primeira tentativa, podendo esclarecer apenas dúvidas e relembrar conceitos que ajudem na resolução da atividade.                                                  |
| RN-05 | Comportamento do Modo Debugger                    | Engine de IA (Debugger) | Ao alternar para o Modo Debugger, o agente ganha permissão para analisar logs de erro, pilhas de exceção e sintaxe de código enviadas pelo aluno, escalonando o grau de ajuda (até a resolução da questão por parte do próprio assistente) conforme o usuário não entender e solucionar o problema por conta própria. |
| RN-06 | Imutabilidade de Tópicos Concluídos               | Workspaces              | Quando um tópico é marcado como "Concluído", qualquer interação nova naquele ambiente será invalidada. O histórico permanece disponível apenas para leitura e revisão.                                                                                                          |
| RN-07 | Geração de Trilhas e Atividades restritas para TI | Gerador de Trilha       | Se o aluno submete o briefing para geração de algum curso não relacionado à área de TI, o escopo não será gerado. O mesmo vale para geração de atividades de fixação e revisão.                                                                                                 | 

## Critérios de Aceitação do MVP:

1. **Geração de Trilha Personalizada**: Dado que o aluno preencheu seu objetivo e nível de conhecimento e solicitou a criação do curso, então o backend deve orquestrar a chamada ao LLM e retornar um JSON válido do escopo preliminar do curso com pelo menos 2 Módulos e 2 Tópicos sequenciais, apresentando tal estrutura através de técnicas de UX para o usuário validar ou solicitar modificações.
2. **Postura Pedagógica no Modo Tutor**: Dado que o aluno está dialogando com o tutor para resolução de alguma atividade em andamento, se o estudante pedir a resolução de alguma questão ou o gabarito definitivo, sem nem ao menos ter concluído uma tentativa de atividade, o tutor deve negar a resolução direta, mas tentar entender a dificuldade e relembrar conceitos.
3. **Alternância para o Modo Debugger**: Quando um aluno encontrar um erro de execução para o seu código e colar o traceback no chat (mesmo em Modo Tutor) ou acionar diretamente o _toggle_ para o "Modo Debugger", uma ramificação especializada do Workspace é criada para atender à exceção e apontar os erros da sintaxe sem dar a resposta diretamente, guiando o usuário à causa raiz do problema.
4. **Persistência do Histórico**: Se um aluno enviar mensagens em um chat de determinado tópico e encerrar suas atividades, então, depois de retornar à aplicação, as mensagens anteriores devem ser recarregadas na tela na ordem correta, mantendo o estado da conversa.
5. **Interação Contextualizada**: As conversas entre tutor e estudante são vinculadas especialmente ao tópico específico do curso.
