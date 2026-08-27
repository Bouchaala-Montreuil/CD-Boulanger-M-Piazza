#!/usr/bin/env python3
"""Build the deployable CD Boulangerie website.

The generated site is written to ../website.  Keeping the build output in a
separate directory makes it clear what can be uploaded to a host and avoids
mixing generated pages with the source files.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parent
OUTPUT = PROJECT / "website"


def main() -> None:
    staging = Path(tempfile.mkdtemp(prefix="cd-boulangerie-", dir=PROJECT))
    try:
        env = os.environ.copy()
        env.update({
            "CD_INLINE": "0",
            "CD_OUT": str(staging),
        })

        subprocess.run(
            [sys.executable, str(ROOT / "build.py")],
            cwd=ROOT,
            env=env,
            check=True,
        )

        # The generated HTML expects these shared files at the website root.
        for name in ("styles.css", "script.js"):
            shutil.copy2(ROOT / name, staging / name)
        for name in ("fonts", "images"):
            shutil.copytree(ROOT / name, staging / name, dirs_exist_ok=True)

        # Inline-sized images are useful for the old standalone preview, but
        # are not requested by the production HTML and needlessly add weight.
        inline = staging / "images" / "inline"
        if inline.exists():
            shutil.rmtree(inline)

        if OUTPUT.exists():
            shutil.rmtree(OUTPUT)
        staging.rename(OUTPUT)
        staging = None  # ownership has moved to website/
        print(f"Website generated in {OUTPUT}")
    finally:
        if staging is not None and staging.exists():
            shutil.rmtree(staging)


if __name__ == "__main__":
    main()
