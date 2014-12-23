#!/usr/bin/env python


class Element(object):
    tag = ""
    attributes = ""
    indent = ""

    def __init__(self, content=None, **kwargs):
        self.content = []
        if kwargs:
            self.attributes = [' {}="{}"'.format(
                key, kwargs[key]) for key in kwargs]
        if content is not None:
            self.content.append(content)

    def render(self, file_out, ind=""):
        file_out.write("\n{}<{tag}{attr}>".format(
            ind, tag=self.tag, attr="".join(self.attributes)))

        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, (ind+(" "*4)))
            else:
                file_out.write("\n{}{}".format(ind+(" "*4), item))
        file_out.write("\n{}</{}>".format(ind, self.tag))

    def append(self, additional_content):
        self.content.append(additional_content)


class Html(Element):
    tag = "html"

    def render(self, file_out, ind=""):
        file_out.write("<!DOCTYPE html>")
        Element.render(self, file_out)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    def render(self, file_out, ind=""):
        file_out.write(("\n{}<{tag}{attr}>{cont}</{tag}>").format(
            ind, tag=self.tag, attr="".join(self.attributes),
            cont="".join(self.content)))


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):

    def render(self, file_out, ind=""):
        file_out.write("\n{}<{tag}{attr} />".format(
            ind, tag=self.tag, attr="".join(self.attributes)))


class Br(SelfClosingTag):
    tag = "br"


class Hr(SelfClosingTag):
    tag = "hr"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content, **kwargs):
        super(A, self).__init__(content, href="{}".format(link), **kwargs)


class Ul (Element):
    tag = "ul"


class Li (Element):
    tag = "li"


class H(OneLineTag):

    def __init__(self, level, content, **kwargs):
        self.tag = "h{}".format(level)
        super(H, self).__init__(content, **kwargs)


class Meta(SelfClosingTag):
    tag = "meta"
