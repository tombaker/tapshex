rm -v *.py
rsync -avzu --delete --progress -h ~/github/tap/dctap-python/tests/test_* .
