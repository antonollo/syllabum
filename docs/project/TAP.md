# Termo de Abertura do Projeto:

- **Projeto**: Syllabum - Tutor Educacional Inteligente
- **Versão do documento**: 1.3
- **Data de Elaboração**: 19/10/2026
- **Última Atualização**: 26/10/2026

## Identificação do Projeto:

| Campo                    | Descrição                                           |
| ------------------------ | --------------------------------------------------- |
| Nome do Projeto          | Syllabum - Tutor Educacional Inteligente            |
| Natureza do Projeto      | Projeto independente de desenvolvimento de software |
| Responsável pelo projeto | Antonio Gabriel Nunes Martins                       |
| Responsável pelo produto | Antonio Gabriel Nunes Martins                       |
| Organização solicitante  | Não se aplica - iniciativa independente             |
| Patrocinador             | Não há                                              |
| Prazo estimado           | 10 semanas                                           |
| Orçamento preliminar     | Ainda não estimado                                  |

## Contexto e Justificativa:

A área de TI reúne inúmeras especialidades, tecnologias e abordagens para a resolução de problemas. Iniciantes mergulham na variedade de tecnologias emergentes, mas, ao analisar o mercado atual, é muito provável que esse público se depare com pelo menos alguma das seguintes perguntas:

1. _"O que eu preciso aprender para me inserir no mercado de trabalho? E em que ordem?"_
2. _"Como eu pratico o que eu vou estudar, com exercícios e retorno sobre o que eu errei?"_
3. _"Partindo do que eu já sei, para onde eu vou e o que eu posso fazer em seguida?"_

Como o mercado de tecnologia é extremamente maleável e imprevisível, com novas tecnologias inovadoras surgindo dia após dia, sendo capazes de virar de "ponta-cabeça" os mercados atuais, dificulta-se para novatos entrarem e crescerem na área justamente pela grande quantidade de possíveis decisões para tomar. Embora muitos veteranos da área já ofertem guias estruturadas (roteiros de estudos, _roadmaps_, etc.) para novatos utilizarem no aprendizado, ainda não lidam integralmente com todas as particularidades de um indivíduo, como:

1. **Condições** (financeiras, pessoais, etc.);
2. **Formato de Aprendizado**;
3. **Tempo dedicável**;
4. **Objetivos particulares**;
5. Entre muitos outros.

O Syllabum, então, entra como uma plataforma educacional inteligente para aprendizagem de competências relacionadas à área de TI, ofertando uso de Inteligência Artificial para potencializar o aprendizado e poder oferecer orientação individualizada. De que forma?

- **Identificar conhecimentos prévios e dificuldades de aprendizado**;
- **Orientar atividades de estudo e boas práticas**;
- **Elaborar roteiros de aprendizado direcionados ao atendimento de restrições, objetivos e formato de aprendizado do estudante**;
- **Aprendizado focado e promovido no desenvolvimento de projetos práticos**.

A justificativa do projeto está na oportunidade de explorar como sistemas baseados em Inteligência Artificial podem contribuir para uma experiência de aprendizagem mais alinhada às necessidades e aos objetivos individuais. Para tanto, o desenvolvimento do MVP deverá implementar e avaliar um conjunto inicial de funcionalidades que permita demonstrar a proposta e verificar seu funcionamento.

## Objetivo Geral e Objetivos Específicos:

### Objetivo Geral:

Desenvolver e disponibilizar, em prazo de até 10 semanas, um MVP para uma plataforma educacional inteligente para aprendizagem de competências relacionadas à área de TI, podendo potencializar o aprendizado e orientação individual com uso de Inteligência Artificial Generativa. As técnicas pedagógicas do Tutor Educacional Inteligente se inspiram na Intercepção Socrática, onde o desenvolvimento de raciocínio se desenvolve a partir de perguntas retóricas sem implementação de soluções diretas.

### Objetivos Específicos:

- Implementar um mecanismo de Inteligência Artificial Generativa capaz de elaborar uma proposta estruturada de curso de acordo com os objetivos de aprendizagem e restrições informados pelo estudante;
- Implementar o mecanismo de criação e cadastro de cursos a partir das estruturas geradas pela Inteligência Artificial;
- Desenvolver um ambiente de diálogo adaptativo entre Assistente Virtual e estudante, focado no atendimento específico de tópicos gerados para os cursos;
- Implementar camadas de orquestração de Inteligências Artificiais para permitir que o Assistente Virtual alterne entre "Modo Tutor" e "Modo Debugger";
- Permitir ao usuário acompanhar o próprio desempenho geral, além do desempenho específico para cada curso;
- Implementar um mecanismo de Inteligência Artificial Generativa capaz de elaborar o escopo de atividades de acordo com dificuldades detectadas pelo estudante;
- Impedir a criação de cursos, roteiros de estudo e atividades que não estejam relacionados à área de TI;
- Validar fluxos essenciais por meio da validação de testes funcionais.

## Descrição de Alto Nível:

O Syllabum será uma plataforma web voltada para o uso individual de estudantes dos mais variados níveis de conhecimento na área de TI.

A solução deve permitir que usuários apresentem um briefing que representa o que desejam aprender e porquê querem aprender, nisso, uma Inteligência Artificial impulsiona esse briefing ao nível de gerar cursos completos e roteiros de estudo que viabilizem esse aprendizado da melhor forma. Cada curso é estruturado por vários chats especializados que oferecem o acompanhamento de um tutor virtual que tanto ensina a respeito de determinado tópico selecionado durante a elaboração do curso através do "Modo Tutor", como também mitiga dúvidas e aponta erros de código sem dar a solução direta através do "Modo Debugger".

O produto será desenvolvido de forma incremental, permitindo que funcionalidades sejam implementadas, testadas e revisadas em ciclos semanais. A solução deverá ser acessível por navegadores web em computadores.

## Escopo:

### Itens incluídos no Escopo:

- Cadastro e consulta de informações do estudante;
- Estruturação de cursos por IA Generativa;
- Cadastro e consulta de cursos do estudante;
- Estruturação de atividades por IA Generativa, dependendo de dificuldades do estudante;
- Chat entre Assistente Virtual e estudante;
- Testes funcionais dos fluxos principais;
- Documentação básica para instalação, configuração e utilização;
- Integração com Sistemas Externos (provedores de LLM, serviços de email, etc.).

### Itens excluídos do Escopo:

- Aplicativo móvel nativo para Android e iOS;
- Padrões de Gamificação como forma de incentivo ao estudante;
- Cursos compartilhados entre estudantes;
- Importação e Exportação de Arquivos e Artefatos.

**Observações**: Funcionalidades excluídas poderão ser avaliadas em versões futuras, mediante análise de prioridade, esforço e disponibilidade de recursos.

## Principais Entregas:

| ID  | Entrega                                                   | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| E1  | Documentação e planejamento do MVP                        | Escopo definitivo e requisitos prioritários.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| E2  | Mecanismo de estruturação de cursos por IA Generativa     | Funcionalidade capaz de receber informações relevantes fornecidas pelo estudante e gerar uma proposta estruturada de um curso, alinhada aos objetivos de aprendizagem informados.                                                                                                                                                                                                                                                                                                                                                                           |
| E3  | Mecanismo de cadastro e persistência de cursos            | Funcionalidade responsável por receber a estrutura gerada, registrá-la no sistema e a disponibilizá-la pela IA Generativa, desde que satisfeitas as condições de que o curso não é duplicado e que o contexto do curso envolve explicitamente alguma área de TI.                                                                                                                                                                                                                                                                                            |
| E4  | Experiência de Aprendizagem orientada pelo tutor          | Funcionalidades que permitem ao estudante acessar o curso, receber atividades de fixação e revisão, diálogos com tutor para receber orientações e feedbacks, além de acompanhar o próprio desempenho geral e específico no aprendizado.                                                                                                                                                                                                                                                                                                                     |
| E5  | Identificação contextual entre Modo Debugger e Modo Tutor | Funcionalidade que identifica a intenção da interação do estudante e direciona o comportamento da IA Generativa. O envio de código-fonte, mensagens de erro ou registros de falha pode acionar o Modo Debugger, ramificação especializada do Workspace do Tutor voltado à análise e resolução de problemas técnicos com aumento escalonado no grau de ajuda ao estudante (fornecendo a resolução real apenas em último caso), enquanto interações voltadas à compreensão de conceitos e ao desenvolvimento de conhecimentos são conduzidas pelo Modo Tutor. |
| E6  | MVP Integrado e Validado                                  | Versão funcional do Syllabum que integra os componentes essenciais e permite avaliar e validar o fluxo principal de utilização através de testes funcionais.                                                                                                                                                                                                                                                                                                                                                                                                |
| E7  | Documentação técnica e disponibilização                   | Instruções necessárias para executar e demonstração do sistema, acompanhada de registros de validação pertinentes.                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Critérios de Sucesso:

O projeto será considerado bem-sucedido quando os seguintes critérios forem atendidos:

1. As funcionalidades essenciais definidas no escopo estiverem implementadas e disponíveis para avaliação.
2. Os testes dos fluxos críticos de mecanismos de estruturação e criação de cursos, além de experiência de aprendizagem orientada pelo tutor, forem aprovados conforme os critérios estabelecidos.
3. A identificação contextual entre Modo Debugger e Modo Tutor for devidamente implementada.
4. O estudante conseguir conseguir executar as operações essenciais sem depender de intervenção técnica do desenvolvedor.
5. A versão final estiver documentada e disponibilizada até o prazo aprovado, respeitando o limite orçamentário estabelecido.

## Marcos Principais:

| ID  | Marco                       | Resultado Esperado                                                           | Prazo Estimado |
| --- | --------------------------- | ---------------------------------------------------------------------------- | -------------- |
| M1  | Iniciação e Levantamento    | Necessidades e escopo preliminar validados.                                  | Semana 1       |
| M2  | Planejamento e prototipação | Requisitos prioritários, backlog e protótipos definidos.                     | Semana 2       |
| M3  | Desenvolvimento do Núcleo   | Cadastros de Cursos e Experiência de Aprendizagem implementados e validados. | Semana 3 a 7   |
| M4  | Testes e Correções          | Verificação de fluxos críticos e falhas prioritárias corrigidas.             | Semana 8       |
| M5  | Implantação e demonstração  | Sistema disponibilizado.                                                     | Semana 9       |
| M6  | Aceite e encerramento       | Entregas avaliadas, documentação concluída e lições aprendidas registradas.  | Semana 10      |

**Observações**: Os prazos são preliminares e deverão ser revisados após o levantamento das necessidades e a decomposição das tarefas.

## Premissas e Restrições:

### Premissas:

- A solução poderá ser implementada com ferramentas e tecnologias de custo compatível com o orçamento previsto.

### Restrições:

- O projeto deverá ser concluído dentro do prazo estimado de nove semanas;
- O desenvolvimento será conduzido por um único desenvolvedor, com disponibilidade limitada;
- O escopo deve permanecer restrito às funcionalidades essenciais do MVP;
- O tratamento dos dados deverá observar as exigências aplicáveis de segurança e proteção de dados pessoais (Lei Geral de Proteção de Dados).

**Observações**: Premissas e Restrições ainda são suscetíveis a modificações a longo prazo.

## Riscos Iniciais:

| Risco                                                                    | Impacto Potencial                                                             | Resposta Preliminar                                                                 |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Expansão excessiva do escopo                                             | Atrasos e impossibilidade de concluir o MVP.                                  | Priorizar funcionalidade essenciais e filtrar mudanças relevantes.                  |
| Requisitos incompletos                                                   | Retrabalho e funcionalidades inadequadas ao uso real.                         | Validar fluxos principais antes de implementar.                                     |
| Dificuldades técnicas                                                    | Aumento do esforço e atraso nas entregas.                                     | Desenvolver fluxos essenciais e testar antecipadamente as integrações críticas.     |
| Problemas de segurança / Exposição de dados sensíveis                    | Risco à confidencialidade de usuários                                         | Limitação de acesso, desenvolvimento de medidas adequadas de segurança              |
| Qualidade e Alucinação dos modelos de Inteligência Artificial Generativa | Comprometimento de respostas e estrutura de tópicos.                          | Ajustes e testes contínuos com técnicas de Engenharia de Prompt.                    |
| Disponibilidade do Provedor                                              | Atraso e impossilidade de gerar respostas e realizar decisões em tempo hábil. | Busca de um provedor, preferencialmente referência no mercado, com bons resultados. |

**Observações**: Os riscos serão revisados periodicamente durante a execução do projeto, com atualização das respostas conforme necessário.

## Abordagem de Gerenciamento:

O projeto adotará uma abordagem ágil, com desenvolvimento incremental e ciclos semanais de trabalho.

O backlog será priorizado considerando o valor das funcionalidades, as dependências técnicas e o esforço estimado. Ao início de cada ciclo, serão selecionadas as tarefas prioritárias. Ao final, os resultados serão revisados e utilizados para orientar o planejamento seguinte.

O andamento será acompanhado por meio do quadro de tarefas, das entregas concluídas, dos testes realizados e dos riscos identificados.

Alterações que afetem significativamente o escopo, o prazo ou o orçamento deverão ser avaliadas pelo gerente do projeto e aprovadas pelo patrocinador antes da implementação.
