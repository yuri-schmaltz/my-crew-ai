# ADR: Integração de Monitoramento Externo CrewAI

## Contexto
Com observabilidade interna madura, o próximo passo é integrar monitoramento externo (APM, dashboards, alertas) para SLOs/SLA e incidentes.

## Decisão
Integrar CrewAI a plataformas como Datadog, Prometheus, Grafana ou New Relic, exportando métricas e traces críticos.

## Consequências
- Visibilidade operacional ponta a ponta
- Alertas proativos e resposta rápida a incidentes
- Base para SLOs/SLA e compliance
