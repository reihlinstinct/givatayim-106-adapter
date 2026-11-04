ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim AS test
WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir '.[dev]' && python -m playwright install --with-deps chromium webkit
COPY tests ./tests
COPY scripts ./scripts
COPY repo-layout.json ./
ENV PYTHONPATH=/app/tests GIVATAYIM_SCREENSHOTS=/app/browser-evidence
RUN coverage run -m unittest discover -s tests -v && coverage run --append -m unittest discover -s tests/browser -v && coverage report && coverage json
