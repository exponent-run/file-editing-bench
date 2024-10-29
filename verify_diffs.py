import difflib
import os


def generate_diff(original_file: str, modified_file: str, diff_file: str):
    with open(original_file) as f:
        original_lines = f.readlines()
    with open(modified_file) as f:
        modified_lines = f.readlines()

    diff = difflib.unified_diff(
        original_lines, modified_lines, fromfile=original_file, tofile=modified_file
    )

    with open(diff_file, "w") as f:
        f.writelines(diff)


def verify_diff(original_file: str, modified_file: str, diff_file: str) -> bool:
    with open(diff_file) as f:
        diff_content = f.read()
    print(f"\nVerifying {os.path.basename(os.path.dirname(original_file))}:")
    print(diff_content)
    return len(diff_content) > 0


# Process each benchmark
benchmarks_dir = "file_editing_bench"
for benchmark in [
    "move_function_above",
    "move_method_within_class",
    "rename_function",
    "delete_function",
    "add_logging",
]:
    base_path = os.path.join(benchmarks_dir, benchmark)
    original = os.path.join(base_path, "original_code.py")
    modified = os.path.join(base_path, "original_code.after.py")
    diff_file = os.path.join(base_path, "original_code.diff")

    generate_diff(original, modified, diff_file)
    verify_diff(original, modified, diff_file)
