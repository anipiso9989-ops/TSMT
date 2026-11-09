"""Render the guide into the checked-in GitHub Pages directory."""

from dataclasses import dataclass
from html import escape, unescape
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "guide"
PUBLIC = ROOT / "docs"
SITE_TITLE = "The Structure of Mathematical Thought"
REPO = "https://github.com/anipiso9989-ops/TSMT"

PARTS = [
    ("I", "01-Part-I-Foundations.md", "Foundations"),
    ("II", "02-Part-II-Problem-Solving.md", "Problem solving"),
    ("III", "03-Part-III-Advanced.md", "Advanced thinking"),
    ("IV", "04-Part-IV-Applied.md", "Applied reasoning"),
    ("V", "05-Part-V-Research.md", "Independent research"),
]
REFERENCES = [
    ("06-AI-Tutor-Protocol.md", "tutor-protocol.html", "AI Tutor Protocol", "Practice prompts, hints, and mastery criteria."),
    ("07-Principle-Map.md", "principle-map.html", "Principle Map", "Ways to choose a method and find what to review."),
    ("08-Glossary.md", "glossary.html", "Glossary", "Working definitions and the chapters behind them."),
    ("09-Sources-and-Synthesis.md", "sources.html", "Sources and Synthesis", "The source texts and the ideas developed from them."),
]
SOURCE_PAGES = {"README.md": "orientation.html"}
SOURCE_PAGES.update({filename: f"part-{number.lower()}.html" for number, filename, _ in PARTS})
SOURCE_PAGES.update({filename: url for filename, url, _, _ in REFERENCES})
CHAPTER_HEADING = re.compile(r"^# Chapter (\d+) — (.+)$", re.MULTILINE)
SECTION_HEADING = re.compile(r'<h2 id="([^"]+)">(.*?)</h2>', re.DOTALL)
PROTECTED_HTML = re.compile(r"(<(?P<tag>math|pre|a)\b[^>]*>.*?</(?P=tag)>|<code>[^<]*</code>|<[^>]*>)", re.DOTALL)
CHAPTER_REFERENCE = re.compile(r"\b(Chs?\.|Chapters?)( [1-9]\d?(?:\s*[,–]\s*[1-9]\d?)*(?!\d))")


@dataclass
class Chapter:
    number: int
    title: str
    text: str

    @property
    def url(self):
        return chapter_url(self.number)


@dataclass
class Part:
    roman: str
    short: str
    title: str
    intro: str
    checkpoint: str
    chapters: list[Chapter]

    @property
    def url(self):
        return f"part-{self.roman.lower()}.html"

    @property
    def span(self):
        return f"{self.chapters[0].number:02}–{self.chapters[-1].number:02}"


def chapter_url(number):
    return f"chapter-{number:02}.html"


def read_document(filename):
    heading, _, body = (SOURCE / filename).read_text(encoding="utf-8").partition("\n")
    return heading.removeprefix("# "), body.strip()


def strip_divider(text):
    return re.sub(r"\n---\s*$", "", text).strip()


def read_part(roman, filename, short):
    heading, body = read_document(filename)
    pieces = CHAPTER_HEADING.split(body)
    chapters = [
        Chapter(int(number), title, content.strip())
        for number, title, content in zip(pieces[1::3], pieces[2::3], pieces[3::3])
    ]
    checkpoint_heading = f"## Part {roman} checkpoint"
    last_text, marker, checkpoint = chapters[-1].text.partition(checkpoint_heading)
    if not marker:
        raise ValueError(f"Missing {checkpoint_heading!r} in {filename}")
    chapters[-1].text = last_text
    for chapter in chapters:
        chapter.text = strip_divider(chapter.text)
    return Part(roman, short, heading.split(" — ", 1)[1], strip_divider(pieces[0]),
                strip_divider(marker + checkpoint), chapters)


def link_references(fragment):
    def chapter_reference(match):
        label, numbers = match.groups()

        def number_link(number_match):
            number = int(number_match[0])
            if number > 35:
                return number_match[0]
            return f'<a href="{chapter_url(number)}">{number_match[0]}</a>'

        return label + re.sub(r"\d+", number_link, numbers)

    def link_piece(piece):
        if piece.startswith("<code>"):
            filename = unescape(piece.removeprefix("<code>").removesuffix("</code>"))
            if filename in SOURCE_PAGES:
                return f'<a href="{SOURCE_PAGES[filename]}">{piece}</a>'
        if piece.startswith("<"):
            return piece
        return CHAPTER_REFERENCE.sub(chapter_reference, piece)

    # Keep code blocks, TeX annotations, and existing links intact.
    pieces = []
    offset = 0
    for match in PROTECTED_HTML.finditer(fragment):
        pieces.extend((link_piece(fragment[offset:match.start()]), link_piece(match[0])))
        offset = match.end()
    pieces.append(link_piece(fragment[offset:]))
    return "".join(pieces)


def render(markdown):
    # Pandoc's TeX delimiter expects a closing dollar immediately after the formula.
    markdown = markdown.replace('$Q(n) = $', '$Q(n) =$')
    result = subprocess.run(
        ["pandoc", "--from=gfm+tex_math_dollars-raw_html", "--to=html5", "--mathml", "--wrap=none"],
        input=markdown, text=True, capture_output=True, check=True, encoding="utf-8",
    )
    if result.stderr:
        raise ValueError(result.stderr.strip())
    linked = link_references(result.stdout)
    linked = re.sub(r'<math\b[^>]* display="block".*?</math>',
                    lambda match: f'<span class="display-math">{match[0]}</span>',
                    linked, flags=re.DOTALL)
    return re.sub(r"<table>.*?</table>",
                  lambda match: '<div class="table-scroll" tabindex="0" role="region" '
                  f'aria-label="Table with horizontal scrolling">{match[0]}</div>',
                  linked, flags=re.DOTALL)


def page(title, description, main, *, home=False):
    page_title = SITE_TITLE if home else f"{title} · {SITE_TITLE}"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description)}">
  <title>{escape(page_title)}</title>
  <link rel="icon" href="assets/mark.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/site.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="shell bar">
      <a class="brand" href="index.html" aria-label="{SITE_TITLE} home"><img src="assets/mark.svg" width="26" height="26" alt="">{SITE_TITLE}</a>
      <nav aria-label="Main navigation">
        <a href="index.html#contents">Contents</a>
        <a href="index.html#reference">Reference</a>
      </nav>
    </div>
  </header>
{main}
  <footer class="site-footer">
    <div class="shell bar">
      <span>{SITE_TITLE}</span>
      <a href="{REPO}">View source <span aria-hidden="true">↗</span></a>
    </div>
  </footer>
</body>
</html>
"""


def write(filename, html):
    (PUBLIC / filename).write_text(html, encoding="utf-8")


def landing(parts):
    sequence = "\n".join(
        f'<li><a href="#part-{part.roman.lower()}"><span>{part.roman}</span>'
        f'<strong>{part.short}</strong><span>{part.span}</span></a></li>'
        for part in parts
    )
    contents = []
    for part in parts:
        rows = chapter_list(part)
        contents.append(f"""
      <section class="part-block" id="part-{part.roman.lower()}">
        <div class="part-label">
          <p class="eyebrow">Part {part.roman} <span aria-hidden="true">/</span> {part.span}</p>
          <h3><a href="{part.url}">{escape(part.title)}</a></h3>
          <a class="text-link" href="{part.url}">Overview and checkpoint <span aria-hidden="true">↗</span></a>
        </div>
        {rows}
      </section>""")
    reference_rows = "\n".join(
        f'<li><a href="{url}"><strong>{label}</strong><span>{description}</span>'
        '<span aria-hidden="true">↗</span></a></li>'
        for _, url, label, description in REFERENCES
    )
    main = f"""
  <main class="shell" id="main">
    <section class="hero" aria-labelledby="guide-title">
      <div>
        <p class="eyebrow">A field guide to reasoning</p>
        <h1 id="guide-title">The Structure of<br class="title-break"> Mathematical<br class="title-break"> Thought</h1>
        <p class="lede">Start with small examples. Learn to write proofs, solve unfamiliar problems, and investigate questions of your own.</p>
        <div class="hero-links">
          <a class="button" href="chapter-01.html">Start reading <span aria-hidden="true">→</span></a>
          <a class="text-link" href="orientation.html">How to use the guide <span aria-hidden="true">↗</span></a>
        </div>
      </div>
      <nav class="sequence" aria-label="Reading sequence">
        <p class="eyebrow">Reading sequence</p>
        <ol>{sequence}</ol>
        <p class="sequence-note">5 parts <span aria-hidden="true">/</span> 35 chapters</p>
      </nav>
    </section>
    <section class="home-section" id="contents" aria-labelledby="contents-title">
      <div class="section-heading">
        <p class="eyebrow">The guide</p>
        <h2 id="contents-title">Contents</h2>
      </div>
{"".join(contents)}
    </section>
    <section class="home-section" id="reference" aria-labelledby="reference-title">
      <div class="section-heading">
        <p class="eyebrow">Companion materials</p>
        <h2 id="reference-title">Reference</h2>
      </div>
      <ul class="reference-list">{reference_rows}</ul>
    </section>
  </main>"""
    write("index.html", page(SITE_TITLE, "A beginner-friendly guide to proofs, problem solving, applied reasoning, and independent mathematical research.", main, home=True))


def chapter_list(part):
    links = "\n".join(
        f'<li><a href="{chapter.url}"><span class="entry-number" aria-hidden="true">{chapter.number:02}</span>'
        f'<span>{escape(chapter.title)}</span><span class="entry-arrow" aria-hidden="true">→</span></a></li>'
        for chapter in part.chapters
    )
    return f'<ol class="chapter-list" start="{part.chapters[0].number}">{links}</ol>'


def step(url, label, title):
    return (f'<a href="{url}"><span class="eyebrow">{escape(label)}</span>'
            f'<span>{escape(title)}</span></a>')


def article(title, label, breadcrumb, body, previous="", following=""):
    sections = SECTION_HEADING.findall(body)
    links = "\n".join(
        f'<li><a href="#{anchor}">{re.sub(r"<[^>]+>", "", text)}</a></li>' for anchor, text in sections
    )
    outline = f'<nav class="outline" aria-label="On this page"><p class="eyebrow">On this page</p><ul>{links}</ul></nav>' if links else ""
    pagination = f'<nav class="pagination" aria-label="Reading order">{previous or "<span></span>"}{following}</nav>' if previous or following else ""
    return f"""
  <main class="shell reader" id="main">
    <nav class="breadcrumbs" aria-label="Breadcrumb">
      <a href="index.html">Guide</a><span aria-hidden="true">/</span>{breadcrumb}
    </nav>
    <header class="reader-header">
      <p class="eyebrow">{escape(label)}</p>
      <h1>{escape(title)}</h1>
    </header>
    <div class="reading-layout">
{outline}
      <div class="reading-column">
        <article class="prose">{body}</article>
{pagination}
      </div>
    </div>
  </main>"""


def main():
    parts = [read_part(*data) for data in PARTS]
    chapters = [chapter for part in parts for chapter in part.chapters]
    if [chapter.number for chapter in chapters] != list(range(1, 36)):
        raise ValueError("Expected chapters 1–35 in order")

    landing(parts)
    title, markdown = read_document("README.md")
    orientation = article(title, "Orientation", '<span aria-current="page">Orientation</span>', render(markdown),
                          following=step(chapter_url(1), "Start reading →", chapters[0].title))
    write("orientation.html", page("Orientation", "How to study and practice with the guide.", orientation))

    for part_index, part in enumerate(parts):
        intro = re.sub(r"\*\*Chapters in this part\*\*\n\n(?:\d+\. [^\n]+\n)+", "", part.intro, count=1)
        body = (render(intro) + '<h2 id="chapters">Chapters in this part</h2>' + chapter_list(part)
                + render(part.checkpoint).replace(f'id="part-{part.roman.lower()}-checkpoint"', 'id="checkpoint"'))
        following = ""
        if part_index + 1 < len(parts):
            next_part = parts[part_index + 1]
            following = step(next_part.url, f"Part {next_part.roman} →", next_part.title)
        part_page = article(part.title, f"Part {part.roman} / Chapters {part.span}",
                            f'<span aria-current="page">Part {part.roman}</span>', body,
                            step(part.chapters[0].url, "First chapter", part.chapters[0].title), following)
        write(part.url, page(f"Part {part.roman} · {part.title}", f"Overview and checkpoint for Part {part.roman}.", part_page))

        for chapter in part.chapters:
            number = chapter.number
            previous = step(chapters[number - 2].url, f"← Chapter {number - 1:02}", chapters[number - 2].title) if number > 1 else step("orientation.html", "← Orientation", "How to use the guide")
            if number == part.chapters[-1].number:
                following = step(f"{part.url}#checkpoint", f"Part {part.roman} checkpoint →", "Check your mastery")
            else:
                following = step(chapters[number].url, f"Chapter {number + 1:02} →", chapters[number].title)
            breadcrumb = (f'<a href="{part.url}">Part {part.roman}</a><span aria-hidden="true">/</span>'
                          f'<span aria-current="page">Chapter {number:02}</span>')
            chapter_page = article(chapter.title, f"Chapter {number:02} / Part {part.roman}",
                                   breadcrumb, render(chapter.text), previous, following)
            write(chapter.url, page(f"Chapter {number:02} · {chapter.title}",
                                    f"Chapter {number} of {SITE_TITLE}. {chapter.title}.", chapter_page))

    for filename, url, label, description in REFERENCES:
        title, markdown = read_document(filename)
        breadcrumb = (f'<a href="index.html#reference">Reference</a><span aria-hidden="true">/</span>'
                      f'<span aria-current="page">{escape(label)}</span>')
        reference = article(title, "Reference", breadcrumb, render(markdown))
        write(url, page(label, description, reference))


if __name__ == "__main__":
    main()
