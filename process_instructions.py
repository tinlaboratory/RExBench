import sys
from pathlib import Path

def split_markdown(file_path):
    path = Path(file_path)
    if not path.exists() or not path.suffix == ".md":
        print(f"Error: {file_path} is not a valid markdown file.")
        return

    content = path.read_text(encoding='utf-8')
    lines = content.splitlines()

    # Identify section split indices
    hints_index = next((i for i, line in enumerate(lines) if line.strip() == "### Hints"), len(lines))
    detailed_hints_index = next((i for i, line in enumerate(lines) if line.strip() == "### More detailed hints"), len(lines))

    # Create content slices
    no_hints_content = "\n".join(lines[:hints_index-1])
    hints_content = "\n".join(lines[:detailed_hints_index-1])
    detailed_hints_content = content  # All of it

    # Prepare output paths
    base = path.with_suffix("")
    no_hints_path = base.with_name(f"{base.name}-default.md")
    hints_path = base.with_name(f"{base.name}-hints.md")
    detailed_hints_path = base.with_name(f"{base.name}-more_detailed_hints.md")

    # Write the files
    no_hints_path.write_text(no_hints_content, encoding='utf-8')
    hints_path.write_text(hints_content, encoding='utf-8')
    detailed_hints_path.write_text(detailed_hints_content, encoding='utf-8')

    print("Files written:")
    print(f"  - {no_hints_path}")
    print(f"  - {hints_path}")
    print(f"  - {detailed_hints_path}")

if __name__ == "__main__":
    input_filepath = sys.argv[1]
    split_markdown(sys.argv[1])