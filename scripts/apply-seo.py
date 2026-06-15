#!/usr/bin/env python3
"""Apply SEO meta tags and JSON-LD schema to all HTML pages."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
seo = json.loads((ROOT / "assets/partials/seo-pages.json").read_text())
schema = (ROOT / "assets/partials/schema.html").read_text().strip()

for filename, meta in seo.items():
    path = ROOT / filename
    text = path.read_text()
    canonical = "https://coyotelegal.com/" if filename == "index.html" else f"https://coyotelegal.com/{filename}"
    robots = meta.get("robots", "index, follow")
    head_seo = f'''  <title>{meta["title"]}</title>
  <meta name="description" content="{meta["description"]}" />
  <meta name="robots" content="{robots}" />
  <link rel="canonical" href="{canonical}" />
  <link rel="alternate" hreflang="es-MX" href="{canonical}" />
  <link rel="alternate" hreflang="es-US" href="{canonical}" />
  <link rel="alternate" hreflang="en-US" href="{canonical}" />
  <link rel="alternate" hreflang="x-default" href="{canonical}" />
  <meta name="geo.region" content="US-TX" />
  <meta name="geo.placename" content="Dallas-Fort Worth" />
  <meta name="audience" content="Mexico, United States, Hispanic immigration clients" />
  <meta property="og:type" content="{meta["og_type"]}" />
  <meta property="og:site_name" content="Coyote Legal | Margaret A. Donnelly, P.C." />
  <meta property="og:title" content="{meta["title"]}" />
  <meta property="og:description" content="{meta["description"]}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="https://coyotelegal.com/assets/images/logo.png" />
  <meta property="og:locale" content="es_MX" />
  <meta property="og:locale:alternate" content="es_US" />
  <meta property="og:locale:alternate" content="en_US" />'''

    text = re.sub(
        r"  <title>.*?</title>\s*<meta name=\"description\" content=\"[^\"]*\" />\s*<meta name=\"robots\" content=\"[^\"]*\" />\s*<link rel=\"canonical\" href=\"[^\"]*\" />(?:\s*<link rel=\"alternate\" hreflang=\"[^\"]*\" href=\"[^\"]*\" />)?(?:\s*<meta name=\"geo\.region\"[^>]*>)?(?:\s*<meta name=\"geo\.placename\"[^>]*>)?(?:\s*<meta name=\"audience\"[^>]*>)?(?:\s*<meta property=\"og:[^\"]*\"[^>]*>)*",
        head_seo,
        text,
        count=1,
        flags=re.DOTALL,
    )

    if "application/ld+json" not in text:
        text = text.replace(
            '  <link rel="stylesheet" href="assets/css/style.css" />',
            '  <link rel="stylesheet" href="assets/css/style.css" />\n' + schema,
        )
    else:
        text = re.sub(
            r'<script type="application/ld\+json">.*?</script>',
            schema,
            text,
            count=1,
            flags=re.DOTALL,
        )

    text = text.replace(
        'alt="Coyote Legal logo"',
        'alt="Coyote Legal — abogada de inmigración Dallas y Fort Worth"',
    )

    if not text.startswith('<!DOCTYPE html>\n<html lang="es">'):
        text = text.replace('<html lang="en">', '<html lang="es">', 1)

    path.write_text(text)
    print("updated", filename)
