#!/bin/bash
pytest --doctest-modules --junitxml=/tests/junit/test-results.xml --cov=app /tests --cov-report=xml:/tests/junit/coverage.xml --cov-report=html:/tests/junit/cov_html