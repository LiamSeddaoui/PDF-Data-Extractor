#!/usr/bin/env python3
# coding:utf8

import PyPDF2
import argparse
import re
import exifread


def get_pdf_meta(file_name):
    pdf_file = PyPDF2.PdfFileReader(open(file_name, "rb"))
    doc_info = pdf_file.getDocumentInfo()
    for data in doc_info:
        print("[+] " + data + doc_info[data])


def get_strings(file_name):
    with open(file_name, "rb") as file:
        content = file.read()
    _re = re.compile("[\S\s]{4,}")
    for match in _re.finditer(content.decode("utf8", "backslashreplace")):
        print(match.group())


def get_exif(file_name):
    with open(file_name, "rb") as file:
        exif = exifread.process_file(file)
    if not exif:
        print("No exif metadata")
    else:
        for tag in exif.keys():
            print(tag + " " + exif.get(""))


parser = argparse.ArgumentParser(
    description=" Extract metadata PDF & IMG file")
parser.add_argument("-pdf", dest="pdf_file",
                    help="PDF using for extract metadata ", required=False)
parser.add_argument("-str", dest="str", help="PDF need read content", required=False)
parser.add_argument("-exif", dest="exif", help="Image extract metadata", required=False)
args = parser.parse_args()

if args.pdf_file:
    get_pdf_meta(args.pdf_file)


if args.str:
    get_strings(args.str)


if args.exif:
    get_exif(args.exif)
