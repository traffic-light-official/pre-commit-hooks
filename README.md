# pre-commit-hooks

Some hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit

## Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/traffic-light-official/pre-commit-hooks
    rev: v1.1.0  # Use the ref you want to point at
    hooks:
    -   id: detect-fuzzy-translations
        files: /LC_MESSAGES/.+\.po$
    # -   id: ...
```

### Hooks available

#### `detect-fuzzy-translations`
Prevent translation files (*.po, gettext) with fuzzy messages from being committed.

## Development
```shell
python3 -m venv venv
source ./venv/bin/activate
pip install -r ./requirements_dev.txt
pre-commit install
```
