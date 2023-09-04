r"""Api
=======
"""
import os
import re
from gzip import decompress

from markdown_it import MarkdownIt
from platformdirs import site_data_dir
from pypandoc import convert_text


def init_document() -> dict[str, str]:
    r"""Init document.

    :rtype: dict[str, str]
    """
    with open(
        os.path.join(
            os.path.join(site_data_dir("man"), "man1"), "expect.1.gz"
        ),
        "rb",
    ) as f:
        text = decompress(f.read()).decode()
    text = convert_text(text, "markdown", "man")
    md = MarkdownIt("commonmark", {})
    tokens = md.parse(text)
    indices = []
    end_index = len(tokens)
    for i, token in enumerate(tokens):
        if token.content == "LIBRARIES":
            end_index = i
            break
        if (
            token.type == "inline"
            and token.content.islower()
            and token.content.startswith("**")
            and token.content.endswith("*")
        ):
            indices += [i]
    items = {}
    for i, index in enumerate(indices):
        if len(indices) - 1 == i:
            index2 = end_index
        else:
            index2 = indices[i + 1]
        keyword = tokens[index].content.split()[0].strip("*")
        items[keyword] = tokens[index].content + "\n"
        for token in tokens[index + 1 : index2]:
            if token.content.startswith(":"):
                items[keyword] += re.sub(r"\n\s*", " ", token.content) + "\n"
            elif token.content != "" and not token.content.startswith("<!--"):
                items[keyword] += re.sub(r"\n\s*", " ", token.content)

    return items
