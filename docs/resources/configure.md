# Configure

See customization in
<https://expect-language-server.readthedocs.io/en/latest/api/expect-language-server.html#expect_language_server.server.get_document>.

## (Neo)[Vim](https://www.vim.org)

### [coc.nvim](https://github.com/neoclide/coc.nvim)

```json
{
  "languageserver": {
    "expect": {
      "command": "expect-language-server",
      "filetypes": [
        "expect"
      ],
      "initializationOptions": {
        "method": "builtin"
      }
    }
  }
}
```

### [vim-lsp](https://github.com/prabirexpectrestha/vim-lsp)

```vim
if executable('expect-language-server')
  augroup lsp
    autocmd!
    autocmd User lsp_setup call lsp#register_server({
          \ 'name': 'expect',
          \ 'cmd': {server_info->['expect-language-server']},
          \ 'whitelist': ['expect'],
          \ 'initialization_options': {
          \   'method': 'builtin',
          \ },
          \ })
  augroup END
endif
```

## [Neovim](https://neovim.io)

```lua
vim.api.nvim_create_autocmd({ "BufEnter" }, {
  pattern = { "*.exp" },
  callback = function()
    vim.lsp.start({
      name = "expect",
      cmd = { "expect-language-server" }
    })
  end,
})
```

## [Emacs](https://www.gnu.org/software/emacs)

```elisp
(make-lsp-client :new-connection
(lsp-stdio-connection
  `(,(executable-find "expect-language-server")))
  :activation-fn (lsp-activate-on "*.exp")
  :server-id "expect")))
```

## [Sublime](https://www.sublimetext.com)

```json
{
  "clients": {
    "expect": {
      "command": [
        "expect-language-server"
      ],
      "enabled": true,
      "selector": "source.expect"
    }
  }
}
```

## [Visual Studio Code](https://code.visualstudio.com/)

[An official support of generic LSP client is pending](https://github.com/microsoft/vscode/issues/137885).

### [vscode-glspc](https://gitlab.com/ruilvo/vscode-glspc)

`~/.config/Code/User/settings.json`:

```json
{
  "glspc.serverPath": "expect-language-server",
  "glspc.languageId": "expect"
}
```
