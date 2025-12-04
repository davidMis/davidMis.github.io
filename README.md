# CV Data Management System

This project uses a data-driven approach to manage CV content, allowing you to maintain your CV data in one place (`cv-data.yml`) and automatically generate format-specific renderings for both HTML and PDF.

## Files

- **`cv-data.yml`** - Single source of truth for all CV content (education, publications, talks, experience)
- **`generate-cv.py`** - Python script that reads YAML and generates Quarto-compatible markdown
- **`cv-sections-generated.qmd`** - Auto-generated file (don't edit directly!)
- **`index.qmd`** - Main document that includes the generated content
- **`template.tex`** - LaTeX template for professional PDF formatting
- **`build.sh`** - Build script that regenerates everything

## How It Works

1. **Edit cv-data.yml** - All your CV data is stored here in structured YAML format
2. **Run build.sh** - Automatically:
   - Runs `generate-cv.py` to create format-specific renderings
   - Renders PDF
   - Renders HTML website
   - Copies files to docs/

## Editing Your CV

To add or update content:

1. Edit `cv-data.yml` (add a publication, talk, job, etc.)
2. Run `sh build.sh`
3. Done! Both HTML and PDF are updated

## Example: Adding a New Publication

```yaml
publications:
  conference:
    - title: "Your Paper Title"
      authors: [SD Mis, Coauthor Name]
      venue: "Conference Name 2026"
      date: Jun 2026
      location: "City, Country"
      links:
        pdf: "https://example.com/paper.pdf"
        arxiv: "https://arxiv.org/abs/2345.67890"
```

Then run `sh build.sh` and both your website and PDF CV are updated!
