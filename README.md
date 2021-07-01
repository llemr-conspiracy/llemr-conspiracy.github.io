# LLEMR Conspiracy Blog

## Running locally

Install prerequisites.

1. Create a virtual environment and install pelican.

	```bash
	pip install -r requirements.txt
	```

2. Build the documentation:

	```bash
	pelican content -s pelicanconf.py
	```

	and serve the documentation:

	```bash
	pelican --listen
	```

	Optionally, you can build the documentation every two seconds with:

	```bash
	watch pelican content -s pelicanconf.py
	```

## Deploying changes

Use pelican to build the html pages locally, then use `ghp-import` to move the html only to the `gh-pages` branch, then push that branch up to github.

```bash
$ pelican content -o output -s pelicanconf.py
$ ghp-import output -b gh-pages
$ git push origin gh-pages
```