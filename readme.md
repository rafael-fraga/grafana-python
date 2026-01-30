# grafana-python

## 1. Instrodução
Este projeto demonstra como integrar uma aplicação Flask com Prometheus para monitoramento de métricas e Grafana para visualização dessas métricas.

## 2. Requisitos
- Python 3.x
- Flask
- Prometheus Client
- Docker e Docker Compose
- Grafana

## 3. Configuração do Ambiente e Utilização
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/grafana-python.git
    cd grafana-python
    ```
2. Inicialize o docker-compose:
   ```bash
   docker-compose up --build
   ```
3. Acesse a aplicação Flask em `http://localhost:3001`.
4. Acesse o Grafana em `http://localhost:3000` (usuário: `admin`, senha: `admin`).
5. Configure o Prometheus como fonte de dados no Grafana e importe o dashboard desejado.

## 4. Endpoints da Aplicação
Esses endpoints podem ser encontrados no http://localhost:3001:
- `/hello`: Retorna uma mensagem de saudação.
- `/print_number?number=<int>`: Recebe um número como parâmetro e registra uma métrica de resumo.
- `/crash`: Simula uma exceção para testar o monitoramento de erros.
- `/metrics`: Endpoint para o Prometheus coletar as métricas da aplicação.

## 5. Métricas Monitoradas
- `app_request_count`: Contador de requisições, rotulado por método HTTP, endpoint e status HTTP.
- `app_exception_count`: Contador de exceções, rotulado por endpoint e tipo de exceção.
- `app_print_number_summary`: Resumo dos números enviados ao endpoint `/print_number`.
