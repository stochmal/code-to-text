import os
import sys

from pprint import pprint



def main(folder):

    print('folder:',folder)

    # create output file names all_code.txt
    output_file = 'all_code.txt'
    output_file = os.path.join(folder, output_file)
    
    # add YYYYMMDD to output file name
    output_file = output_file.replace('.txt', '_20210101.txt')

    print('output_file:',output_file)

#    assert not os.path.exists(output_file), 'Output file already exists: {}'.format(output_file)

    # write to output file
    with open(output_file, 'w', encoding="utf-8") as f:

        # list all files
        for root, dirs, files in os.walk(folder):
            for file in files:

                filename = os.path.join(root, file)

                # exclude folders
                EXCLUDE_FOLDERS = ['.git','.vs','.vscode']
                if any(folder in filename for folder in EXCLUDE_FOLDERS):
                    continue

                EXCLUDE_EXTENSIONS = ['.pfx','.wsdl']
                if any(filename.endswith(ext) for ext in EXCLUDE_EXTENSIONS):
                    continue

                if filename.startswith('.\\'):
                    filename = filename[2:]

                print(filename)

                # write filename to output file
                f.write('\nfilename: ' + filename + '\n')
                f.write('```\n')

                # read filename using readlines() and write to output file
                with open(filename, 'r', encoding="utf-8") as f2:
                    lines = f2.readlines()
                    for line in lines:
                        f.write(line)

                f.write('\n```\n')


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: python code-to-text.py <input_folder>')
        sys.exit(1)

    main(sys.argv[1])
    