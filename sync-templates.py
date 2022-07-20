from glob import glob
from pathlib import Path
from shutil import copy2
from sys import argv

def compare_files(origin, mirror):
    if mirror.exists() is False:
        return True
    
    return int(origin.stat().st_mtime) > int(mirror.stat().st_mtime)


def sync_file(origin, mirror):
    if compare_files(Path(origin), mirror):
        copy2(origin, str(mirror))
        print(f'{mirror} updated.')


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
    for origin in file_list:
        mirror = templates_path / f'{prefix + "-" if prefix else ""}{origin}'
        sync_file(origin, mirror)

if __name__ == '__main__':
    main()