# Pendências e Decisões do Projeto

- **Versão**: 0.3
- **Produto**: Syllabum - Tutor Educacional Inteligente
- **Data de Elaboração**: 23/10/2026
- **Última Atualização**: 26/10/2026

## Como usar

1. Toda dúvida ou decisão adiada entra como uma linha em **Pendências Abertas**, com um ID sequencial (P-01, P-02...).
2. Cada pendência diz **o que precisa ser decidido**, **onde afeta** (documento e seção) e **até quando** (marco ou sprint).
3. Ao decidir, a linha sai de Abertas e vai para **Decisões Tomadas**, com data e motivo. Depois, ajuste os documentos afetados.
4. Nenhuma decisão é deletada. O log serve para lembrar _por que_ algo foi escolhido.

**Legenda de prioridade**: Alta (bloqueia implementação), Média (afeta qualidade ou escopo), Baixa (acabamento).

---

## Pendências:

| ID   | Prioridade | Pendência (o que decidir)                                                                                                                  | Onde afeta                                                                   | Decidir até   | Status  |
| ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | ------------- | ------- |
| P-01 | Alta       | Stack tecnológica: provedor/modelo de LLM, backend, banco e modo de execução (local ou hospedado).                                         | EAP (seção Fundação Técnica), TAP (E7, M5)                                   | M2            | Aberta  |
| P-02 | Alta       | Debugger: nunca entrega a correção, ou entrega após N tentativas / a pedido do aluno? É uma bifurcação do Modo Tutor ou Workspace próprio? | MVP (Critério de Aceitação 3), TAP (E5), User Stories (US-11), EAP 3.1 e 3.2 | M2            | Fechada |
| P-03 | Alta       | Tutor: pode exibir exemplos livremente, mas como trata atividades geradas (gabarito)? Reescrever RN-04 e Critério 2.                       | MVP (RN-04, Critério 2), User Stories (US-07), EAP 2.3                       | M2            | Fechada |
| P-04 | Média      | Contexto entre tópicos: resumo estruturado ao concluir o tópico, ou só ementa? Manter RN-01 para mensagens brutas.                         | MVP (RN-01), EAP 2.5, User Stories (CA-05.1)                                 | M2            | Fechada |
| P-05 | Média      | Critérios de sucesso mensuráveis sem usuários-piloto (cenários roteirizados: X de Y).                                                      | TAP (critérios de sucesso, M5), MVP (objetivo)                               | M2            | Aberta  |
| P-06 | Média      | Teto de custos (API de LLM, hospedagem, e-mail) ou declaração de custo zero.                                                               | TAP (orçamento, critério 5)                                                  | M2            | Aberta  |
| P-07 | Média      | Definir "duplicado" e "fora da área de TI" para cursos, roteiros e atividades (objetivo específico do TAP).                                | TAP (objetivo 7), MVP (nova RN), EAP                                         | M3            | Aberta  |
| P-08 | Média      | Definir métricas dos dashboards: como medir tempo de estudo, streak e média semanal.                                                       | EAP 4.1/4.2, CA-09.1, CA-10.1                                                | M3            | Aberta  |
| P-09 | Baixa      | Itens mínimos de LGPD: consentimento, política de privacidade, exclusão de conta.                                                          | TAP (restrições), EAP 5                                                      | M3            | Aberta  |
| P-10 | Baixa      | Glossário único (curso/trilha, escopo preliminar, tutor, workspace, perfil, avaliação).                                                    | Todos os documentos                                                          | Revisão final | Aberta  |
| P-11 | Média      | Definição de estrutura de Payload de comunicação entre o Modo Debugger e o Modo Tutor                                                      | TutorFlow                                                                    | M3            | Aberta  |
| P-12 | Média      | Definição de orçamento máximo de tokens para o Modo Debugger e Modo Tutor                                                                  | TutorFlow (C-02)                                                             | M3            | Aberta  |
| P-13 | Alta       | Atividades: As atividades geradas devem permitir múltiplas tentativas? Como medir a nota de múltiplas tentativas (média, maior nota)?      | MVP, EAP, User Stories                                                       | M2            | Aberta  |

---

## Decisões Tomadas

| ID   | Decisão                                                                                                                                                                                                                                                                       | Data                                         | Motivo                                                                                    | Documentos ajustados                      |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------- |
| D-01 | Importação e Exportação de Arquivos passa a Won't Have; citada só nas exclusões do TAP.                                                                                                                                                                                       | 23/10/2026                                   | Fora do que um MVP precisa para validar a proposta.                                       | MVP, TAP                                  |
| D-02 | EAP mantida orientada a funcionalidades; infraestrutura em artefato próprio.                                                                                                                                                                                                  | 23/10/2026                                   | Padrão que já funcionou em outros projetos; stack no M2.                                  | EAP                                       |
| D-03 | Sem usuários-piloto; objetivo do MVP passa a ser viabilidade técnica e pedagógica.                                                                                                                                                                                            | 23/10/2026                                   | Não há usuários disponíveis; retenção/autonomia ficam pós-MVP.                            | MVP, TAP                                  |
| D-04 | A ação de ajuda e apresentação real da solução deve ser escalonada em níveis (perguntas abertas que redirecionam atenção, dicas que apontam a região ou conceito, exemplo análogo resolvido, só então a resolução real do problema, acompanhada de uma explicação do porquê). | 24/10/2026                                   | Limitações do uso de conceitos puros de Intercepção Socrática podem frustrar usuários.    | MVP, TAP, User Stories e EAP              |
| D-05 | O Modo Debugger deve ser tratado como uma bifurcação especializada do Workspace do Modo Tutor, tendo características próprias.                                                                                                                                                | 24/10/2026                                   | Melhor definição e mapeamento para o Modo Debugger em relação ao Workspace de Aprendizado | MVP e TAP                                 |
| D-06 | O Modo Tutor, no que tanger atividades geradas, apenas fornece um gabarito quando o usuário finalizar sua primeira tentativa, estando a disposição apenas para sanar possíveis dúvidas e relembrar conceitos que ajudem o estudante a resolver o problema independentemente.  | 26/10/2026                                   | Melhor definição das capacidades do Modo Tutor diante de Atividades Geradas.              | MVP (RN-04, Critério 2), US-07, EAP (2.3) |
| D-07 | A contextualização entre tópicos é dado por compartilhamento de resumos estruturados abstraídos de tópicos anteriores, escolhidos e analisados mediante decisão do modelo.                                                                                                    | 26/10/2026 | Melhor definição da relação entre tópicos de trilhas de aprendizado e compartilhamento de contexto. |MVP (RN-01), EAP 2.5, User Stories (CA-05.1) |

---
