import re
import sys
import tempfile
import subprocess
import io
import shutil

def run():
    if len(sys.argv) < 2:
        print("""
        Please provide tex filename
            %s [filename] other param in xelatex
        """ % sys.argv[0]);
        sys.exit()

    filename = sys.argv[1]
    with io.open(filename, 'r+', encoding='utf8') as f :
        content = f.read()
        # reg replacement
        # remove \maketitle
        content = content.replace(r'\maketitle', '')

        # replace to documentclass{ctexart}
        content = re.sub(r'\\documentclass(.*?)$', r'\documentclass{ctexart}', content, flags=re.M)

        # make tempfile
        tmpfile = tempfile.mktemp()
        tfile = io.open(tmpfile, "w", encoding='utf8')
        tfile.write(content)
        tfile.close()

    #copy back
    if tmpfile :
        shutil.copy(tmpfile, sys.argv[1]);

    # run xelatex
    cmdlist = ['/usr/bin/xelatex',] + sys.argv[1:]
    print (cmdlist);
    subprocess.call (cmdlist)
