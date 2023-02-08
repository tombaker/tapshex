rm -v *.py
rsync -avzu --delete --progress -h ~/github/tap/dctap-python/tests/test_* ~/github/tap/dctap-python/tests/__init__.py .
