"""Write a single 100-word villain monologue to /output/entry.txt.

Fully deterministic: the text is a fixed constant, with no randomness,
no clock, no network access, and no reads outside this repository.
"""

import os
from pathlib import Path

MONOLOGUE = """Hero. Sit. No— not the throne. That chair. The one with the cushion.

I am Kevin, Lord of Ashenmoor, breaker of three kings, keeper of the Eclipse Bell. Tonight it rings, and every candle in the valley gutters out, and every locked door... opens. You came to stop me. Of course. Swords, speeches, destiny.

Look. The bell needs one last pull. The rope is right there. My hands—

Well. They have done enough pulling.

Pour the tea first. Two sugars. Then we will talk about surrender. Yours, obviously. Mine can wait. It has already waited... three hundred years."""


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(MONOLOGUE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
