import os


def extension(dir, first_level=False):
    files = os.listdir(dir)
    for filename in files:
        path = os.path.join(dir, filename)
        if os.path.isfile(path):
            ext = filename.split(".")[-1]
            if ext not in extensions:
                extensions[ext] = []

            extensions[ext].append(filename)

        elif os.path.isdir(path) and not first_level:
            extension(path,first_level=True)


directory = input()

extensions = {}

extension(directory)

sorted_extensions = sorted(extensions.keys())

report_file = os.path.join(directory, 'report.txt')
with open(report_file, 'w') as report:
    for extension in sorted_extensions:
        report.write(f'.{extension}\n')
        files = extensions[extension]
        sorted_files = sorted(files)
        for file in sorted_files:
            report.write(f'- - - {file}\n')
