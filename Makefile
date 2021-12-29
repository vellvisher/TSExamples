build:	verify
	python3 build.py
	# Workaround due to relative path of site.css.
	cp site.css examples/site.css
verify:
	mypy build.py
test:
	tsc --target es6 *.ts && node *.js && rm -rf *.js
clean:
	if [ -a index.html ]; then rm index.html; fi;
	if [ -a examples ]; then rm -r examples; fi;
