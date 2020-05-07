build:	verify
	python3 build.py
verify:
	mypy build.py
test:
	tsc --target es6 *.ts && node *.js && rm -rf *.js
clean:
	rm -r index.html examples
