#!/usr/bin/env python3
"""Extract reference facts and media from the local HMG PowerPoint template."""
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = Path(r"C:\Users\JoJoonhee\Desktop\ppt\hmg-template.pptx")


def main(template_path: str | None = None) -> None:
    template = Path(template_path) if template_path else DEFAULT_TEMPLATE
    if not template.exists():
        raise SystemExit(f"Template not found: {template}")
    media_dir = ROOT / "assets" / "hmg-template-media"
    media_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(template) as z:
        names = z.namelist()
        for name in names:
            if name.startswith("ppt/media/"):
                (media_dir / Path(name).name).write_bytes(z.read(name))
        colors: set[str] = set()
        fonts: set[str] = set()
        for name in names:
            if name.endswith(".xml") and name.startswith(("ppt/theme/", "ppt/slides/", "ppt/slideLayouts/", "ppt/slideMasters/")):
                xml = z.read(name).decode("utf-8", errors="ignore")
                colors.update(re.findall(r'(?:srgbClr val|a:srgbClr val)="([0-9A-Fa-f]{6})"', xml))
                fonts.update(re.findall(r'typeface="([^"]+)"', xml))
    print(f"Extracted {len(list(media_dir.iterdir()))} media files")
    print("Colors:", ", ".join(sorted(colors)))
    print("Fonts:", ", ".join(sorted(fonts)))


if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else None)
