#!/usr/bin/env python
import os
import re
import subprocess

def fix(filename):

    # convert to md
    root, ext = os.path.splitext(filename)
    mdfile = root + '.md'
    command = 'pandoc -f latex -t markdown -o {0} {1}'.format(mdfile, filename)
    proc = subprocess.Popen(command.split())
    proc.wait()
    if proc.returncode != 0:
        raise SystemExit('failed to convert {0}'.format(filename))

    lines = open(mdfile).read()

    # find all <span>**...**</span>
    regex = r'<span>\*\*(?P<n>.*?)\*\*<\/span>'
    for pat in re.findall(regex, lines):
        sub = '**{0}**'.format(pat)
        pat = regex.replace('(?P<n>.*?)', pat)
        lines = re.sub(pat, sub, lines)

    # find all <span>*...*</span>
    regex = r'<span>\*(?P<n>.*?)\*<\/span>'
    for pat in re.findall(regex, lines):
        sub = '*{0}*'.format(pat)
        pat = regex.replace('(?P<n>.*?)', pat)
        lines = re.sub(pat, sub, lines)

    # find all other <span>...</span>
    regex = r'(?m)<[\/]*span>'
    lines = re.sub(regex, '``', lines)

    lines = lines.split('\n')
    for (i, line) in enumerate(lines):
        lines[i] = lines[i].replace('\*', '*')
        lines[i] = lines[i].replace('\>', '>')
        lines[i] = lines[i].replace('\<', '<')
        if '=====' in line:
            lines[i-1] = '# ' + lines[i-1].strip()
            lines[i] = ''
            continue
        if '-----' in line:
            lines[i-1] = '## ' + lines[i-1].strip()
            lines[i] = ''
            continue
        if line.startswith(':') and lines[i-2].rstrip().endswith(':'):
            lines[i-2] = '- **{0}**'.format(lines[i-2].strip())
            lines[i] = ' ' + lines[i][1:]
            continue

    new_lines = [lines[0]]
    for (i, line) in enumerate(lines[1:]):
        if not line.split():
            new_lines.append(line)
            continue
        if re.search('(?i)[a-z\*`0-9]', line[0]):
            if not new_lines[-1].split():
                new_lines.append(line.lstrip())
            else:
                new_lines[-1] += ' ' + line
            continue
        new_lines.append(line)
    lines = '\n'.join(new_lines)

    # remove consecutive new lines
    lines = re.sub('\n{2,99}', '\n\n', lines.strip())

    with open(mdfile, 'w') as fh:
        fh.write(lines)

if __name__ == '__main__':
    fix('temp.tex')
