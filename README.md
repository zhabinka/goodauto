## Car auction aggregation

### Requirements

- python >= 3.10
- poetry
- chrome webdriver (os suitable)

### Usage

```bash
# setup
make install

# download catalog pages
poetry run catalog-loader

# get car links
poetry run catalog-handler

# collect car sources
poetry run car-loader
```
