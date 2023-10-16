# requirements-language-server

[![readthedocs](https://shields.io/readthedocs/requirements-language-server)](https://requirements-language-server.readthedocs.io)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Freed-Wu/requirements-language-server/main.svg)](https://results.pre-commit.ci/latest/github/Freed-Wu/requirements-language-server/main)
[![github/workflow](https://github.com/Freed-Wu/requirements-language-server/actions/workflows/main.yml/badge.svg)](https://github.com/Freed-Wu/requirements-language-server/actions)
[![codecov](https://codecov.io/gh/Freed-Wu/requirements-language-server/branch/main/graph/badge.svg)](https://codecov.io/gh/Freed-Wu/requirements-language-server)
[![DeepSource](https://deepsource.io/gh/Freed-Wu/requirements-language-server.svg/?show_trend=true)](https://deepsource.io/gh/Freed-Wu/requirements-language-server)

[![github/downloads](https://shields.io/github/downloads/Freed-Wu/requirements-language-server/total)](https://github.com/Freed-Wu/requirements-language-server/releases)
[![github/downloads/latest](https://shields.io/github/downloads/Freed-Wu/requirements-language-server/latest/total)](https://github.com/Freed-Wu/requirements-language-server/releases/latest)
[![github/issues](https://shields.io/github/issues/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server/discussions)
[![github/milestones](https://shields.io/github/milestones/all/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server/milestones)
[![github/forks](https://shields.io/github/forks/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server/network/members)
[![github/stars](https://shields.io/github/stars/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server/stargazers)
[![github/watchers](https://shields.io/github/watchers/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server/watchers)
[![github/contributors](https://shields.io/github/contributors/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server/commits)
[![github/release-date](https://shields.io/github/release-date/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server/releases/latest)

[![github/license](https://shields.io/github/license/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server/blob/main/LICENSE)
[![github/languages](https://shields.io/github/languages/count/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server)
[![github/languages/top](https://shields.io/github/languages/top/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server)
[![github/directory-file-count](https://shields.io/github/directory-file-count/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server)
[![github/code-size](https://shields.io/github/languages/code-size/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server)
[![github/repo-size](https://shields.io/github/repo-size/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server)
[![github/v](https://shields.io/github/v/release/Freed-Wu/requirements-language-server)](https://github.com/Freed-Wu/requirements-language-server)

[![pypi/status](https://shields.io/pypi/status/requirements-language-server)](https://pypi.org/project/requirements-language-server/#description)
[![pypi/v](https://shields.io/pypi/v/requirements-language-server)](https://pypi.org/project/requirements-language-server/#history)
[![pypi/downloads](https://shields.io/pypi/dd/requirements-language-server)](https://pypi.org/project/requirements-language-server/#files)
[![pypi/format](https://shields.io/pypi/format/requirements-language-server)](https://pypi.org/project/requirements-language-server/#files)
[![pypi/implementation](https://shields.io/pypi/implementation/requirements-language-server)](https://pypi.org/project/requirements-language-server/#files)
[![pypi/pyversions](https://shields.io/pypi/pyversions/requirements-language-server)](https://pypi.org/project/requirements-language-server/#files)

Language server for
[requirements.txt](https://pip.pypa.io/en/stable/reference/requirements-file-format).

Currently python has two requirement formats:

- [PEP508](https://peps.python.org/pep-0508): supported by:
  - [setuptools](https://setuptools.pypa.io)
- [pip](https://pip.pypa.io/en/stable/reference/requirements-file-format/#requirements-file-format):
  supported by:
  - [pip](https://pip.pypa.io)
  - [pip-compile](https://github.com/jazzband/pip-tools)

The difference is that
[PEP508 doesn't support pip's options](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html#dynamic-metadata).

- [x] diagnostic
- [x] format: sort packages
- [x] go to definition: jump to first repeated package
- [x] go to reference: jump to all other repeated packages
- [x] document link: open package's pypi homepage
- [x] document hover & completion:
  - [x] pip's options
  - [x] package: requires [pip-cache](https://github.com/brunobeltran/pip-cache).
    Must `pip-cache update` before.

Other features:

- [x] pre-commit-hooks
  - [x] linter
  - [x] formatter

## Screenshots

### Diagnostic

![diagnostic](https://github.com/Freed-Wu/requirements-language-server/assets/32936898/13aa466d-62af-423a-a141-880b495750a7)

### Document Hover

![module](https://github.com/Freed-Wu/requirements-language-server/assets/32936898/0e74a423-b07a-459a-8fb4-10789f245265)

![option](https://github.com/Freed-Wu/requirements-language-server/assets/32936898/78a7b5ec-a9dd-46c2-b22b-4dc0123b6f0e)

### Completion

![module](https://github.com/Freed-Wu/requirements-language-server/assets/32936898/d3a258ef-3d99-4666-a015-cc516bdb58fd)

![option](https://github.com/Freed-Wu/requirements-language-server/assets/32936898/1a8de48c-9138-4a0c-97a4-0c7ea3030be0)

![file](https://github.com/Freed-Wu/requirements-language-server/assets/32936898/da7e162d-fa82-461a-a8b4-09db684e766c)

Read
[![readthedocs](https://shields.io/readthedocs/requirements-language-server)](https://requirements-language-server.readthedocs.io)
to know more.

## Related Projects

- [requirements.txt.vim](https://github.com/raimon49/requirements.txt.vim):
  syntax highlight for vim
- [vim-polyglot](https://github.com/sheerun/vim-polyglot): contains above
- [bat](https://github.com/sharkdp/bat): syntax highlight for less
- [requirements-txt-fixer](https://github.com/pre-commit/pre-commit-hooks#requirements-txt-fixer):
  sort package names
