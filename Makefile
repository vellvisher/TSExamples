build:	verify
	python3 build.py
verify:
	mypy build.py
test:
	tsc --target es6 *.ts && node *.js && rm -rf *.js
clean:
	if [ -a index.html ]; then rm index.html; fi;
	if [ -a examples ]; then rm -r examples; fi;
