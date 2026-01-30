from flask import Flask, request, Response
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
    app.run(host=host, port=port)