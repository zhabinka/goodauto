## Car auction aggregation

### Requirements

- python >= 3.10
- poetry
- chrome webdriver (os suitable)

### Specification

[Архитектура](https://drive.google.com/file/d/18bDCfywXauErEwW-5tOPRF-NVY6L8Y-h/view?usp=sharing) реализована по мотивам System Design Алекса Сюя.

[Database schema](https://app.dynobird.com/?action=open&id=89e59edb-4bf1-49b6-8353-21d2bcb14dff)

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

# load brands
poetry run python manage.py load_brands
```
