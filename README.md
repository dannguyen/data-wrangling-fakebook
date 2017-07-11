# Sphinx Documentation Hot Tips!





`TKchange` is added to `conf.py` and elsewhere to indicate changes from defaults.

## Steps to build

```sh
$ cd docs
$ make html
```

To rebuild HTML from scratch (i.e. not just from un-modified files)

```sh
$ make html SPHINXOPTS='-E'
```




## Steps to create from scratch

1. Create project directory and change into it
2. Run `sphinx-quickstart`
3. Add `_build/` to .gitignore




