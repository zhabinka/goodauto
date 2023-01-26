#!/usr/bin/env python

from parser.parser import ASSETS_CATALOG_PAGES_PATH, get_links_auto


def main():
     try:
        get_links_auto(ASSETS_CATALOG_PAGES_PATH)
        print(f'[SUCCESS] All pages processed')
     except Exception as e:
        # TODO: add logging
        print(e)


if __name__ == "__main__":
    main()
