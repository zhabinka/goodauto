#!/usr/bin/env python

from parser.parser import ASSETS_CAR_LINKS_PATH, collect_page_car_sources


def main():
     try:
        collect_page_car_sources(ASSETS_CAR_LINKS_PATH)
        print(f'[SUCCESS] All cars processed!')
     except Exception as e:
        # TODO: add logging
        print(e)


if __name__ == "__main__":
    main()
