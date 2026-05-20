# davidmis.github.io

Static personal website for GitHub Pages.

## Editing

The published site lives in `docs/`:

- `docs/index.html` - home page
- `docs/news.html` - news archive
- `docs/styles.css` - shared styles
- `docs/files/DavidMis-CV.pdf` - PDF CV
- `docs/files/` - site images and static assets

There is no required build step for the website. Edit the HTML and CSS files directly, then commit and push.

## CV updates

The website and CV are intentionally maintained separately. When the CV changes:

1. Replace `docs/files/DavidMis-CV.pdf`.
2. Update the selected publications, talks, awards, or background text in `docs/index.html` if needed.
3. Add any news item to `docs/news.html` and link to it from the homepage when it should be featured.

## Legacy Quarto files

The old Quarto/YAML CV workflow files are still present for reference. The live site no longer depends on them.
