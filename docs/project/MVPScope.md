# Escopo do MVP:

- **Versão**: 0.1
- **Produto**: Syllabum - Tutor Educacional Inteligente

## Objetivo do MVP:

O Syllabum permitirá validar ou não se um ambiente com geração dinâmica de trilhas orientadas a objetivos, com acompanhamento em tempo real por Inteligências Artificiais Generativas, melhora a retenção e autonomia de aprendizado de estudantes de TI, sem depender de entregas de respostas prontas.

## Funcionalidades do MVP:

Inspirando-se no **Método MoSCoW** ("Must-Have, Should-Have, Could-Have e Won't Have"):

| Categorias de Prioridade | Módulo                                      | Descrição                                                                                                                                                                |
| ------------------------ | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Must-Have                | Entrada e Avaliação de Perfil               | Interface para o usuário declarar um briefing de seus objetivos de estudo e nível atual.                                                                                 |
| Must-Have                | Gerador de Trilha / Roadmap de Aprendizado  | Orquestração de LLM para transformar o objetivo do usuário em um conjunto de Módulos e Tópicos Estruturados.                                                             |
| Must-Have                | Workspace de Aprendizado                    | Instanciação de um chat dedicado a cada tópico da trilha, permitindo injeção de System Prompts dedicados a instigar o raciocínio, pedir esclarecimentos e guiar o aluno. |
| Must-Have                | Alternação entre Modo Tutor e Modo Debugger | Orquestração de LLM para conduzir um chamado para um chat limitado dedicado à resolução de problemas técnicos (bugs, erros, etc.).                                       |
| Must-Have                | Gerador Dinâmico de Atividades              | Orquestração de LLM para detecção de dificuldades ou necessidades de revisão, transformando esse requisito em um conjunto estruturado de atividades.                     |
| Should-Have              | Acompanhamento de Desempenho Geral          | Desenvolvimento de um Dashboard que avalia o desempenho geral do usuário por métricas temporais (diárias, semanais, mensais, etc.).                                      |
| Should-Have              | Acompanhamento de Desempenho Especifico     | Desenvolvimento de um Dashboard que avalia o desempenho do usuário para algum curso específico.                                                                          |
| Could-Have               | Importação e Exportação de Arquivos         | Orquestração de LLM para leitura e elaboração de documentos (imagens, PDFs, etc.).                                                                                       |
| Won't Have               | Sistema de Gamificação                      | Elaboração de um esquema de pontuação pública (badges, rankings) entre alunos.                                                                                           |
| Won't Have               | Compartilhamento de Cursos                  | Um aluni pode compartilhar com outros usuários a autorização de visualização e interação com o curso.                                                                    |

## Regras de Negócio Fundamentais (Business Rules):

| ID    | Regra de Negócio                    | Módulo Afetado          | Descrição do Comportamento Esperado                                                                                                                                                                                                         |
| ----- | ----------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RN-01 | Isolamento de Contexto de Chat      | Workspace / Backend     | Cada tópico da trilha possui um histórico de chat isolado. As mensagens de um tópico X nunca são enviadas na janela de contexto (prompt) para um Tópico subsequente, reduzindo custos e evitando alucinações.                               |
| RN-02 | Intercepção Socrática de Código     | Engine de IA (Tutor)    | Se o aluno solicitar diretamente a solução pronta ou código completo de uma tarefa, o agente no Modo Tutor deve recusar a entrega direta e responder com orientações, perguntas instigantes ou trechos parciais de documentação.            |
| RN-03 | Comportamento do Modo Debugger      | Engine de IA (Debugger) | Ao alternar para o Modo Debugger, o agente ganha permissão para analisar logs de erro, pilhas de exceção e sintaxe de código enviadas pelo aluno, apontando a causa raiz do problema sem resolver o problema conceitual de fundo do tópico. |
| RN-04 | Imutabilidade de Tópicos Concluídos | Workspace / Banco       | Quando um tópico é marcado como "Concluído", a geração de novas respostas pelo LLM naquele chat são congelados. O histórico permanece disponível apenas para leitura e revisão.                                                             |
| RN-05 | Regeneração de Trilha Limitada      | Gerador de Trilha       | Se o aluno optar por regenerar uma trilha por não se adequar ao seu nível, os chats e dados associados à trilha antiga são arquivados, gerando um novo mapa de estudos do zero.                                                             |

## Critérios de Aceitação do MVP:

1. **Geração de Trilha Personalizada**: Dado que o aluno preencheu seu objetivo e nível de conhecimento e solicitou a criação do curso, então o backend deve orquestrar a chamada ao LLM e retornar um JSON válido com pelo menos 2 Módulos e 4 Tópicos sequenciais, salvando a estrutura no banco de dados.
2. **Postura Pedagógica no Modo Tutor**: Dado que o aluno está interagindo no chat de um tópico no Modo Tutor, quando o aluno solicita a solução para algo, a IA deve responder sem fornecer blocos de código funcionais completos, utilizando uma abordagem socrática que oriente o aluno a escrever o código por conta própria.
3. **Alternância para o Modo Debugger**: Quando um aluno encontrar um erro de execução para o seu código e colar o traceback no chat (mesmo em Modo Tutor) ou acionar diretamente o _toggle_ para o "Modo Debugger", uma seção limitada e objetiva é criada para atender à exceção e apontar os erros da sintaxe sem dar a resposta e solução diretamente.
4. **Persistência do Histórico**: Se um aluno enviar mensagens em um chat de determinado tópico e encerrar suas atividades, então, depois de retornar à aplicação, as mensagens anteriores devem ser recarregadas na tela na ordem correta, mantendo o estado da conversa.
