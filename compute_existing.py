import os
import re
from pathlib import Path

SEGMENT_PATTERN = re.compile(
    r"{%\s*if\s*segment:(\d+)\s*%}(.*?){%\s*endif\s*%}", re.DOTALL
)


def extract_segments(content):
    """Find all unique segment conditions in the content."""
    return {segment for segment, _ in SEGMENT_PATTERN.findall(content)}


def process_segments(content, active_segment=None):
    """Keep only the active segment and remove all others."""

    def replace_match(match):
        segment_id, segment_content = match.groups()
        return (
            segment_content
            if active_segment is None or segment_id == active_segment
            else ""
        )

    return SEGMENT_PATTERN.sub(replace_match, content)


def process_newsletters(input_dir, output_dir):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for file in input_path.glob("*.html"):
        with file.open("r", encoding="utf-8") as f:
            content = f.read()

        segments = extract_segments(content)

        # Generate a default file without any segments (removing all conditions)
        default_content = process_segments(content, None)
        output_file = output_path / f"{file.stem}.html"
        with output_file.open("w", encoding="utf-8") as f:
            f.write(default_content)

        # Generate a file for each individual segment
        for segment_id in segments:
            new_content = process_segments(content, segment_id)
            output_file = output_path / f"{file.stem}-{segment_id}.html"

            with output_file.open("w", encoding="utf-8") as f:
                f.write(new_content)


if __name__ == "__main__":
    process_newsletters("existing", "computed")
