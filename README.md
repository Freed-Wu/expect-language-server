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

- [x] document hover: requires [pip](https://github.com/pypa/pip).
- [x] completion: requires [pip-cache](https://github.com/brunobeltran/pip-cache).
  Must `pip-cache update` before.
- [ ] linter: requires [pip-compile](https://github.com/jazzband/pip-tools).
  See [coc-diagnostic](https://github.com/iamcco/coc-diagnostic).

![document hover](https://github.com/Freed-Wu/mirrors-astyle/assets/32936898/4bdcb620-6482-4bb5-a038-6fcb9577a2e3)

![completion](https://user-images.githubusercontent.com/32936898/195017430-8de7b0f4-e976-485f-9a53-8c66b85f296c.png)

![pypi](https://user-images.githubusercontent.com/32936898/195017436-d4dd4ad5-bd8f-4791-95be-7490299b33e6.png)

![linter](https://user-images.githubusercontent.com/32936898/194537147-bf4b4528-2594-46df-b05c-56c38c419920.png)

## Usage

### vim

Install [coc.nvim](https://github.com/neoclide/coc.nvim):

```json
{
  "languageserver": {
    "requirements": {
      "command": "requirements-language-server",
      "filetypes": [
        "requirements"
      ]
    }
  }
}
```

### neovim

Install [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig):

```vim
if executable('requirements-language-server')
  augroup lsp
    autocmd!
    autocmd User lsp_setup call lsp#register_server({
          \ 'name': 'requirements',
          \ 'cmd': {server_info->['requirements-language-server']},
          \ 'whitelist': ['requirements'],
          \ })
  augroup END
endif
```

## Customization

You can customize the document hover template. A default template is
[here](https://github.com/Freed-Wu/requirements-language-server/tree/main/src/requirements_language_server/assets/jinja2/template.md.j2).
The syntax rule is [jinja](https://docs.jinkan.org/docs/jinja2/templates.html).
The template path is decided by your OS:

```shell
$ requirements-language-server --print-config template
/home/wzy/.config/requirements/template.md.j2
```

## Similar Projects

- [requirements.txt.vim](https://github.com/raimon49/requirements.txt.vim):
  syntax highlight for vim
- [vim-polyglot](https://github.com/sheerun/vim-polyglot): contains above
- [bat](https://github.com/sharkdp/bat): syntax highlight for less
