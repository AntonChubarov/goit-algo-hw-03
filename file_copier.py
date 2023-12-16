import os
import shutil
import argparse


def list_files(directory):
    files = []
    try:
        dir_contents = os.listdir(directory)
    except FileNotFoundError:
        print(f"Error: Source directory '{directory}' not found.")
        raise

    for entry in dir_contents:
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            files.extend(list_files(full_path))
        else:
            files.append(full_path)

    return files


def sort_and_copy(files, destination_dir):
    for file_path in files:
        _, file_extension = os.path.splitext(file_path)
        file_extension = file_extension[1:]

        if file_extension == '':
            destination_folder = os.path.join(destination_dir, 'other')
        else:
            destination_folder = os.path.join(destination_dir, file_extension)

        try:
            os.makedirs(destination_folder, exist_ok=True)
        except OSError as e:
            print(f"Error creating directory '{destination_folder}': {e}")
            raise

        try:
            shutil.copy(file_path, destination_folder)
        except OSError as e:
            print(f"Error copying '{file_path}' to '{destination_folder}': {e}")
            raise


def main():
    parser = argparse.ArgumentParser(description='Recursive copy and sort files by extension')
    parser.add_argument('-s', '--src', help='Source directory path')
    parser.add_argument('-d', '--dst', nargs='?', default='dest', help='Destination directory path (default: dest)')
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print(f"Error: {e}")
        parser.print_help()
        return

    source_dir = os.path.abspath(args.src)
    destination_dir = os.path.abspath(args.dst)

    print(f"Copying files from {source_dir} to {destination_dir}")

    files = list_files(source_dir)

    try:
        sort_and_copy(files, destination_dir)
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    print("Copy and sort completed")


if __name__ == "__main__":
    main()
