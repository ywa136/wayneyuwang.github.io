#!/usr/bin/env python

# # Publications markdown generator for academicpages
# 
# Take a .bib file and parse each item and write into appropriate .md file for use 

import bibtexparser

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }


def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


def parse_author(a, keyfirst="Yu", keylast="Wang"):
    """Parses author name in the format of `Last, First Middle` where
    the middle name is sometimes there and sometimes not (and could just be an initial)
    
    Returns: author name as `F. M. Last`
    """
    
    a = a.split(', ')
    last = a[0].strip()
    fm = a[1].split(' ')
    first = fm[0][0] + '.'
    
    if len(fm) > 1:
        middle = fm[1][0] + '.'
    else:
        middle = ''
    
    if last == keylast and fm[0] == keyfirst:
        if not middle == '':
            return '<b><i>' + first + ' ' + middle + ' ' + last + '</i></b>'
        else:
            return '<b><i>' + first + ' ' + last + '</i></b>'
    else:
        if not middle == '':
            return first + ' ' + middle + ' ' + last
        else:
            return first + ' ' + last


# ## Creating the markdown files
# 
import os
from datetime import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

parser = bibtexparser.bparser.BibTexParser(common_strings=True, ignore_nonstandard_types=False)
with open("../../cv-academic/cv.bib") as bibtex_file:
    publications = bibtexparser.load(bibtex_file, parser=parser)

for item in publications.entries:
    
    item = bibtexparser.customization.add_plaintext_fields(item)
    year = item['plain_year'] if 'plain_year' in item else item['plain_date'].split('-')[0]
    key = item['plain_ID']

    md_filename = key + ".md"
    html_filename = key

    ## YAML variables

    md = "---\ntitle: \""   + item['plain_title'] + '"\n'

    md += """collection: publications"""

    md += """\npermalink: /publication/""" + html_filename

    month = datetime.strptime(item['plain_month'],"%B").month if 'plain_month' in item else 6
    day = item['plain_day'] if 'plain_day' in item else 15
    date = datetime(int(year), int(month), int(day)).isoformat() + "00:00:00 + 0500"

    #     if not 'plain_date' in item:
    #         raise Exception(item)
    #     date = item['plain_date']
    #     if len(date) == 4:
    #         date += "-06-15 00:00:00 +0500"
    #     elif len(date) == 7:
    #         date += "-15 00:00:00 +0500"
    #     elif len(date) == 10:
    #         date += " 00:00:00 +0500"
    #     else:
    #         print(date)
    #         break

    md += "\ndate: " + date

    if 'plain_journal' in item:
        venue = item['plain_journal']
    elif 'plain_eventtitle' in item:
        venue = item['plain_eventtitle']
    elif 'plain_booktitle' in item:
        venue = item['plain_booktitle']
    elif 'plain_journaltitle' in item:
        venue = item['plain_journaltitle']
    elif 'plain_school' in item:
        venue = item['plain_institution']
    else:
        venue = False

    if 'plain_note' in item:
        note = item['plain_note']
        venue += " (<b><i>" + note + "</i></b>)"

    if venue:
        md += "\nvenue: '" + html_escape(venue) + "'"

    if 'plain_url' in item:
        md += "\npaperurl: '" + item['plain_url'] + "'"

    if 'plain_doi' in item:
        md += "\ndoi: '" + item['plain_doi'] + "'"

    #     pubtypes = {"inproceedings": "conference",
    #                 "article": "journal",
    #                 "thesis": "academic"}

    md += "\npubtype: '" + item['plain_keywords'] + "'"

    authors = ', '.join([parse_author(a) for a in item['plain_author'].split(' and ')])
    md += "\nauthors: '" + authors + "'"

    md += "\nexcerpt_separator: \"\""

    md += "\n---"

    ## Markdown description for individual page

    if 'plain_abstract' in item:
        md += "\n" + html_escape(item['plain_abstract']) + "\n"

    # if 'plain_url' in item:
    #     md += "\n[Download paper here](" + item['plain_url'] + ")"

    # if 'plain_doi' in item:
    #     md += "\n[DOI](" + item['plain_doi'] + ")"

    md_filename = os.path.basename(md_filename)

    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)
