from flask import Flask, jsonify
from prometheus_client import make_wsgi_app
from prometheus_flask_exporter import PrometheusMetrics
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# Create my app
app = Flask(__name__)

# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

metrics = PrometheusMetrics(app)


@app.route('/')
def root_path():
    return jsonify({
        'service': 'ok'
    })


@app.route('/status/<int:status>')
@metrics.do_not_track()
@metrics.summary('request_by_status', 'Request latencies by status', labels={'status': lambda r: r.status_code})
def echo_status(status):
    a = []
    print(a['abc'])
    return jsonify({
        'Status': status
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
