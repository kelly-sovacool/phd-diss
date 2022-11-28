import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.customization import *
from bibtexparser.bibdatabase import BibDatabase


def main(input_filenames, output_filename):
    bib_dict = {entry['ID']: entry for filename in input_filenames for entry in parse_bibtex(filename).entries}
    print(bib_dict['allaire_rmarkdown_2020']['author'])
    db = BibDatabase()
    db.entries = list(bib_dict.values())
    writer = BibTexWriter()
    #print(db.entries)
    with open(output_filename, 'w') as outfile:
        outfile.write(writer.write(db))


def parse_bibtex(bibtex_filename):
    with open(bibtex_filename, 'r') as bibtex_file:
        parser = BibTexParser()
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
    return bib_database


if __name__ == "__main__" and 'snakemake' in locals():
    main(snakemake.input.bib, snakemake.output.bib)
