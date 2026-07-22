import sys
import argparse
from pathlib import Path
from smart_organizer.worker import organize_files_in_parallel

def parse_arguments():

    parser = argparse.ArgumentParser(
        description = "Organize files in a directory concurrently based on file extensions."
 )
    
    parser.add_argument(
        "target_dir",
        type=str,
        nargs="?",
        default=".",
        help="Path to the directory to organize (default: current directory)"

    )

    parser.add_argument(
        #-
        "-w",
        "--workers",
        type=int,
        default=4,
        help="Number of parallel worker threads to use(default=4)"
    )

    return parser.parse_args()

def scan_directory(target_path: Path) -> list[Path]:
    """Scans the directory and returns a list of files to move (skipping directories)."""
    if not target_path.exists():
        print(f" Error: Path '{target_path}' does not exist.")
        sys.exit(1)

    if not target_path.is_dir():
        print(f" Error: '{target_path}' is not a valid directory.")
        sys.exit(1)

    return [item for item in target_path.iterdir() if item.is_file()]


def main():
    args = parse_arguments()
    base_dir = Path(args.target_dir).resolve()

    print(f"\n Scanning directory: {base_dir}")
    files_to_move = scan_directory(base_dir)

    if not files_to_move:
        print("No files found to organize!")
        return

    print(f"Found {len(files_to_move)} file(s). Starting organization with {args.workers} threads...\n")

    # Pass the list of files off to worker.py
    results = organize_files_in_parallel(
        files_to_move=files_to_move, 
        base_dir=base_dir, 
        max_workers=args.workers
    )

    # Format and display the results
    print("=" * 60)
    print("                   ORGANIZATION REPORT                    ")
    print("=" * 60)

    success_count = 0
    failure_count = 0

    for original, destination, success, error in results:
        if success:
            success_count += 1
            print(f"Moved: {original.name:<25} ──> {destination.relative_to(base_dir)}")
        else:
            failure_count += 1
            print(f"Failed: {original.name:<25} ──> Error: {error}")

    print("=" * 60)
    print(f"Summary: {success_count} succeeded, {failure_count} failed out of {len(results)} total files.\n")


if __name__ == "__main__":
    main()