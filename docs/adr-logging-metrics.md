# ADR: Logging Estruturado Global

## Contexto
O projeto CrewAI carecia de padronização de logs para troubleshooting e observabilidade.

## Decisão
Foi adotado logging global em formato JSON no entrypoint do pacote, facilitando integração futura com sistemas de observabilidade.

## Consequências
- Logs padronizados para todos os módulos.
- Facilidade de análise e troubleshooting.
- Não quebra retrocompatibilidade.

---
# ADR: Instrumentação de Métricas

## Contexto
Não havia métricas mínimas para monitorar tempo de execução de funções críticas.

## Decisão
Decorator `metric_time` criado para instrumentar funções e registrar tempo de execução via logging.

## Consequências
- Métricas básicas disponíveis sem dependências externas.
- Facilidade de extensão para métricas customizadas.
