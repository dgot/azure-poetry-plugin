poetry run pytest test \
    --junit-xml=test-report.xml \
    --html=test-report.html --self-contained-html \
    --cov src \
    --cov-report html \
    --cov-report xml:coverage.xml \
    # --cov-fail-under=85 \
