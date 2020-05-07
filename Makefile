build:verify
	python3 build.py
verify:
	mypy build.py
clean:
	rm -r index.html examples
