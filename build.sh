# Generate CV sections from structured data
python3 generate-cv.py > cv-sections-generated.qmd

# Build pdf
quarto render index.qmd --to pdf
mv docs/index.pdf files/DavidMis-CV.pdf

# Build html
quarto render
cp files/googlee496e0ae7810f83e.html docs/googlee496e0ae7810f83e.html
cp files/robots.txt docs/robots.txt
cp files/sitemap.xml docs/sitemap.xml