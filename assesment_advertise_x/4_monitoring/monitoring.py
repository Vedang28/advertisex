from prometheus_client import start_http_server, Gauge

g = Gauge('data_pipeline_status', 'Status of the data pipeline')

def set_status(status):
    g.set(status)

# Example usage
start_http_server(8000)
set_status(1)  # 1 for running, 0 for error
