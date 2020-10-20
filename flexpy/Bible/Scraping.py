import os
import requests
from bs4 import BeautifulSoup

LANI_DOMAIN = "https://live.bible.is/bible/DNWOWM/"
ENGLISH_DOMAIN = "https://live.bible.is/bible/ENGESV/"
KALAM_DOMAIN = "https://live.bible.is/bible/AA1WBT/"
# example url of matthew 1: "https://live.bible.is/bible/DNWOWM/MAT/1"
# content is in a long <body> tag at the very bottom, after the script


def get_book_info():
    fp = "BibleChapterNumbers.txt"
    with open(fp) as f:
        lines = f.readlines()
    res = []
    for line in lines:
        eng_name, abbrev, chapters = line.strip().split(",")
        res.append([abbrev, int(chapters)])
    return res


def dump_html_to_files(lang_iso_code):
    book_info = get_book_info()
    for lang_iso in [lang_iso_code]:  # used to do English every time, but now already have the html, so call again if need to re-scrape it
        for book_abbrev, n_chaps in book_info:
            for chap_num in range(1, n_chaps+1):
                print("getting html from {} {} {}".format(lang_iso, book_abbrev, chap_num))
                dump_one_book_html_to_file(lang_iso, book_abbrev, chap_num)


def dump_one_book_html_to_file(lang_iso, book_abbrev, chap_num):
    print("dumping {} {} {}".format(lang_iso, book_abbrev, chap_num))
    lang_iso = lang_iso.lower()
    domain = {"dnw": LANI_DOMAIN, "eng": ENGLISH_DOMAIN, "kmh": KALAM_DOMAIN}[lang_iso]
    book_url_piece = book_abbrev + "/" + str(chap_num)
    url = domain + book_url_piece
    response = requests.get(url)
    text = response.text
    output_fp = "texts/{lang_iso}/{lang_iso}_html/{lang_iso}-{book_abbrev}-{chap_num}.html".format(**locals())
    if os.path.exists(output_fp):
        print("Warning! would overwrite file {}\npress enter to continue or Ctrl-C to exit".format(output_fp))
        input()
    with open(output_fp, "w") as f:
        f.write(text)


def get_verse_dict(lang_iso, book_abbrev, chap_num):
    spans = get_spans(lang_iso, book_abbrev, chap_num)
    spans_with_verse_text = [x for x in spans if not x.has_attr("class") and x.has_attr("data-verseid")]
    d = {}
    for x in spans_with_verse_text:
        assert x.has_attr("data-verseid")
        assert "data-verseid" in x.attrs
        k = x.attrs["data-verseid"]
        k = int(k)
        v = x.text
        d[k] = v
    return d


def get_spans(lang_iso, book_abbrev, chap_num):
    # file should have been dumped directly from server response, make sure you don't scrape the site too much
    html_fp = "texts/{lang_iso}/{lang_iso}_html/{lang_iso}-{book_abbrev}-{chap_num}.html".format(**locals())
    with open(html_fp) as f:
        text = f.read()
    html_soup = BeautifulSoup(text, "html.parser")
    return html_soup.find_all("span")


if __name__ == "__main__":
    dump_html_to_files("kmh")

    # book_info = get_book_info()
    # for abbrev, n_chaps in book_info:
    #     for chap in range(1, n_chaps+1):
    #         verse_dict = get_verse_dict(domain, abbrev, chap)
    #         for v, text in sorted(verse_dict.items()):
    #             assert type(v) is int
    #             print("{} {}:{} = {}".format(abbrev, chap, v, text))
