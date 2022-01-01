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
$ ghp-import output -b gh-pages --cname=llemrconspiracy.org
$ git push origin gh-pages
```

## Making new content

Pelican has two kinds of content: "articles" and "pages". *Articles* are usually chronological content, like our blog posts, and thus associated with a date. In contrast, *pages* are not temporal and are used for content that does not change very often--for example, our "Contact" page.

To make a new Page, simply add a new markdown document to `content/pages/`. To make a new article, simply add it to `content`. Pelican should automatically identify the new markdown document, build it, and add it in the appropriate places!

See the [pertinent pelican documentation](https://docs.getpelican.com/en/latest/content.html#articles-and-pages) for all the things you can do with your content.

## Changing templates

Every page has a template, located in `themes/bootstrap/templates/`. These templates are used to add styling and HTML structure to the Markdown documents found in `content`.

See the [pertinent Pelican documentation](https://docs.getpelican.com/en/latest/themes.html) for how themes/templates work.
