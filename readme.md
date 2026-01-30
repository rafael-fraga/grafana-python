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

<!-- from flask import Flask, request, Response
from prometheus_client import Counter, Summary, generate_latest, CONTENT_TYPE_LATEST
from os import getenv

REQUEST_COUNT = Counter(
    'app_request_count',
    'Total number of requests',
    ['method', 'endpoint', 'http_status'],
)
EXCEPTION_COUNT = Counter(
    'app_exception_count',
    'Total number of exceptions',
    ['endpoint', 'exception_type'],
)
PRINT_NUMBER = Summary('app_print_number_summary', 'Summary of numbers printed')
app = Flask(__name__)

@app.errorhandler(Exception)
def catch_all(e):
    EXCEPTION_COUNT.labels(endpoint=request.path, exception_type=type(e).__name__).inc()
    return {"error": type(e).__name__, "message": str(e)}, 500

@app.after_request
def count_request(response):
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.path,
        http_status=str(response.status_code),
    ).inc()
    return response

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/print_number')
def print_number():
    number = request.args.get('number', default=None, type=int)
    if number is None:
        return "Please provide a number parameter.", 400
    PRINT_NUMBER.observe(float(number))
    return {"printed": number}

@app.route('/crash')
def crash():
    raise KeyError("This is a simulated crash!")

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    host = getenv('HOST', '0.0.0.0')
    port = int(getenv('PORT', '3001'))
    app.run(host=host, port=port) -->

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