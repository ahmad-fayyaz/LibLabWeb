# documentation/markdown_extensions.py
import markdown
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import re

class ContainerPreprocessor(Preprocessor):
    RE = re.compile(r':::\s*(tip|warning|info|note)\n(.*?)\n:::', re.DOTALL)

    def run(self, lines):
        text = "\n".join(lines)
        def repl(m):
            css_class = m.group(1)
            content = m.group(2)
            return f'<div class="{css_class}">{markdown.markdown(content)}</div>'
        text = self.RE.sub(repl, text)
        return text.split("\n")

class ContainerExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(ContainerPreprocessor(md), 'container', 25)

def makeExtension(**kwargs):
    return ContainerExtension(**kwargs)
