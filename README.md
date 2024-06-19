# Install and run

    mkdir otel-getting-started
    cd otel-getting-started
    python3 -m venv venv
    source ./venv/bin/activate
    pip install -r requirements.txt
    opentelemetry-bootstrap -a install
    export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
    opentelemetry-instrument --logs_exporter otlp flask run -p 8080

    docker run -p 4317:4317 \
        -v /tmp/otel-collector-config.yaml:/etc/otel-collector-config.yaml \
        otel/opentelemetry-collector:latest \
        --config=/etc/otel-collector-config.yaml
