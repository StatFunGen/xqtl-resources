# Site layouts

The files here override the hugo-book theme. `scripts/hugo_generator.py` copies this folder into `website/` before Hugo runs, so authors keep editing Markdown in `content/` only.

| Path | What it does |
|---|---|
| `layouts/baseof.html` | Page shell: header with search and theme toggle, left menu, content, "On this page" |
| `layouts/home.html` | Home page. Counts are computed from the dataset pages; the Markdown in `content/README.md` is shown under it |
| `layouts/catalog.html`, `assets/xqtl/catalog.js` | Data catalog: cohort x modality matrix, facets and table. Every row is in the HTML, so it works without JavaScript. Filters are kept in the URL, for example `?kind=qtl&cohort=ROSMAP&family=Expression` |
| `layouts/page.html`, `layouts/_partials/ds/page.html` | Dataset page: summary card and access table from the metadata header, then the page's Markdown, then Analyses and Related datasets |
| `layouts/section.html` | Folder pages (eQTL, Expression ...): a table of the datasets in the folder |
| `layouts/inventory.html`, `layouts/coverage.html` | Dataset inventory and analysis coverage grid |
| `layouts/_partials/ds/info.html` | Works out a page's kind, modality label, colour, status and access in one place |
| `data/xqtl.yaml` | Shared vocabulary: modality colours and labels, cohorts, status and access wording, Synapse folders, home page participant count |
| `data/next_phase.yaml` | Datasets being curated that do not have a page yet |
| `assets/xqtl/site.css` | All styles. Colour tokens at the top, light and dark |

Page metadata lives in each page's header; see `template/metadata_header.md`.

To preview locally: install Hugo extended (0.158 or newer) and PyYAML, clone hugo-book into `website/themes/hugo-book`, then run `python scripts/hugo_generator.py --no-theme-download --no-readme --serve`.
