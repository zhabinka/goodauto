#!/usr/bin/env python

from parser.parser import SOURCE_URL, CATALOG_PATH, collect_catalog_page_sources


def main():
     try:
        collect_catalog_page_sources(
            SOURCE_URL + CATALOG_PATH,
            pages_count=10,
        )
        print(f'[INFO] Collected catalog pages successfully!')
     except Exception as e:
        # TODO: add logging
        print(e)


if __name__ == "__main__":
    main()
