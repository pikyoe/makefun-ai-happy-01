"""ai-happy-01 entry: copy the bundled image to the output directory.

The entry image lives beside this file as entry.png. The program copies
it byte for byte to $MAKEFUN_OUTPUT_DIR/entry.png (default /output),
so both runs of the program produce identical output.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"bundled image not found: {source}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    # Verify the copy so a truncated write can never pass silently.
    if destination.stat().st_size != source.stat().st_size:
        raise IOError(f"copy incomplete: {destination}")


if __name__ == "__main__":
    main()
