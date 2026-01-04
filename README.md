# precommit

## Usage

.pre-commit-config.yaml

```yaml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
    - repo: https://github.com/qsoyq/precommit
      rev: 0.1.0
      hooks:
          - id: check-stash-override-format
            args: [--inplace]
            files: "\\.(py)$"
            always_run: true
            verbose: true
```

### Help

```bash
check-stash-override-format --help
```
