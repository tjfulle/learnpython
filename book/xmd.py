#!/usr/bin/env python
import os
import re
import glob
import subprocess

def find_and_fix():
    to_fix = []
    lines = open('book.mytex').readlines()
    all_gloss = {}
    for line in lines:
        match = re.search(r'\\chapter{(?P<ch>.*)}', line)
        if match:
            if to_fix:
                f = open(chap + '.tex', 'w')
                f.write(''.join(to_fix))
                f.close()
                all_gloss.update(fix_one_chapter(chap + '.tex'))

            x = '_'.join(match.group('ch').split())
            x = x.replace(':', '').replace(',', '')
            if 'case_study' in x.lower():
                continue
            chap = x
            to_fix = [line]
            continue

        if not to_fix:
            continue

        to_fix.append(line)

        if 'end{document}' in line:
            f = open(chap + '.tex', 'w')
            f.write('\n'.join(to_fix))
            f.close()
            all_gloss.update(fix_one_chapter(chap + '.tex'))
            break

    the_gloss = ''
    for key in sorted(all_gloss):
        lines = all_gloss[key]['lines']
        the_gloss = the_gloss + key.strip() + '\n   ' + lines + '\n\n'
    with open('glossary.md', 'w') as fh:
        fh.write(''.join(the_gloss))


def fix_one_chapter(filename):

    # convert to md
    root, ext = os.path.splitext(filename)
    mdfile = root + '.md'
    command = 'pandoc -f latex -t markdown -o {0} {1}'.format(mdfile, filename)
    try:
        proc = subprocess.Popen(command.split())
        proc.wait()
        if proc.returncode != 0:
            raise SystemExit('failed to convert {0}'.format(filename))
    except:
        return {}

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
            title = lines[i-1].strip()
            if '{' in title:
                title, other = title.split('{', 1)
                other = '_'.join(other.replace('#', '').replace('}', '').split())
                lines[i-1] = "<a name='{0}'></a>".format(other)
                lines[i] = '# ' + title
            else:
                lines[i-1] = '# ' + title
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

    # join lines
    lines = join_sentences(lines)

    # find the glossary
    glossary = None
    for (i, line) in enumerate(lines):
        line = ' '.join(line.split())
        if not line.split():
            continue
        if '## glossary' in line.lower():
            glossary = {}
            continue
        if glossary is None:
            continue
        if '## exercise' in line.lower():
            break
        if line.strip().startswith('- **'):
            key = line.strip()[1:].replace('*', '').replace(':', '').strip()
            glossary[key] = []
            continue
        glossary[key].append(line)

    glossary = glossary or {}
    the_gloss = {}
    for (key, item) in glossary.items():
        a = '_'.join(key.replace('*', '').replace('-', '').split())
        a = a.rstrip('s')
        a = a.replace('`', '')
        key = key.replace('`', '')
        key = "- <a name='{0}'>{1}</a>".format(a, key)
        the_gloss[key] = {'lines': ' '.join(' '.join(x.split()) for x in item),
                          'key': a}

    for (i, line) in enumerate(lines):
        line = line.replace('    >>> ', '')
        line = re.sub(r'{#.*}', '', line)
        for k in the_gloss:
            key = the_gloss[k]['key']
            regex = re.compile(r'(?i)\*\*{0}[s]?\*\*'.format(key.replace('_', ' ')))
            match = regex.search(line)
            if match:
                name = re.sub(r'\*', '', match.group()).strip()
                a = "[{1}](glossary.ipynb#{0})".format(key, name)
                line = regex.sub(a, line)
        fig = re.search('figs\/.*\.pdf', line)
        if fig:
            f = fig.group()
            line = "<img src='{0}'/>".format(f.replace('.pdf', '.png'))
        lines[i] = line

    # remove consecutive new lines
    lines = '\n'.join(lines)
    lines = re.sub('\n{2,99}', '\n\n', lines.strip())
    lines, glossary = get_glossary(lines)

    with open(mdfile, 'w') as fh:
        fh.write(lines)

    return the_gloss

def join_sentences(lines):
    sentences = [lines[0]]
    for (i, line) in enumerate(lines[1:]):
        if not line.split():
            sentences.append(line)
            continue
        if re.search('(?i)[a-z\*`0-9]', line[0]):
            if not sentences[-1].split():
                sentences.append(line.lstrip())
            else:
                sentences[-1] += ' ' + line
            continue
        sentences.append(line)
    return sentences

def get_glossary(lines):
    wo_glossary, glossary = [], None
    for line in lines.split('\n'):
        if '## glossary' in ' '.join(line.split()).lower():
            glossary = {}
            continue
        if '## exercise' in ' '.join(line.split()).lower():
            break
        if glossary is not None:
            if not line.split():
                continue
            if line.startswith('-'):
                key = line.replace(':**', '**')
                glossary[key] = []
                continue
            glossary[key].append(line)
        else:
            wo_glossary.append(line)
    glossary = glossary or {}
    return '\n'.join(wo_glossary), glossary

if __name__ == '__main__':
    find_and_fix()
