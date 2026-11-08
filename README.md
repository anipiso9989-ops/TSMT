# The Structure of Mathematical Thought

[The Structure of Mathematical Thought](https://anipiso9989-ops.github.io/TSMT/) is a principle-based guide to rigorous, creative, independent mathematical reasoning.

The original Markdown lives in [guide/](guide/README.md). GitHub Pages serves the generated site from `main` → `/docs`.

## Update the site

With Python 3.10+ and Pandoc 3.x installed, edit the Markdown and regenerate the pages:

```sh
python3 scripts/build.py
python3 -m http.server --directory docs 8000
```

Open <http://localhost:8000> to preview. Commit the Markdown and regenerated HTML together. The published site uses static HTML, CSS, and native MathML.
