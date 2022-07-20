from glob import glob
from pathlib import Path
from shutil import copy2
from sys import argv

def compare_files(file_1, file_2):
    if file_2.exists() is False:
        return True

    return file_1.stat().st_mtime > file_2.stat().stmtime


def sync_file(templates_path, file, prefix):
    def __get_filename():
        return f'{prefix + "-" if prefix else ""}{file}'

    file_path = templates_path / __get_filename(file, prefix)
    if compare_files(Path(file), file_path):
        copy2(file, str(file_path))
        print(f'{file_path} updated.')


def main():
    if len(argv) == 1 or len(argv) > 3:
        print(f'Usage: python sync-templates.py [prefix] /path/to/destination')
        return

    if len(argv) == 2:
        templates_path = Path(argv[1])
        prefix = None
    else:
        templates_path = Path(argv[2])
        prefix = argv[1]

    file_list = [x for x in glob("*.xml") if x != "template.xml"]
    for file in file_list:
        sync_file(templates_path, file, prefix)

if __name__ == '__main__':
    main()