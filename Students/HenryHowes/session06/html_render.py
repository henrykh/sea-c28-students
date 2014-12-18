#!/usr/bin/env python


class Element(object):
    opening_tag = "<>"
    closing_tag = "</>"
    attributes = None
    indent = ""

    def __init__(self, content=None, **kwargs):
        self.content = []
        if kwargs:
            self.attributes = ['{}="{}"'.format(key, kwargs[key]) for key in kwargs]         
        if content is not None:
            self.content.append(content)

    def render(self, file_out, ind=""):
        if self.attributes is not None:
            opening_tag = [self.opening_tag.split('>')[0]] + self.attributes
            self.opening_tag = " ".join(opening_tag)
            self.opening_tag += ">"
        file_out.write("{}{}\n".format(ind, self.opening_tag))
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, (ind+(" "*4)))
            else:
                file_out.write("{}{}\n".format(ind+(" "*4), item))
        file_out.write("{}{}\n".format(ind, self.closing_tag))

    def append(self, additional_content):
        self.content.append(additional_content)


class Html(Element):
    opening_tag = "<html>"
    closing_tag = "</html>"

    def render(self, file_out, ind=""):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out)


class Body(Element):
    opening_tag = "<body>"
    closing_tag = "</body>"


class P(Element):
    opening_tag = "<p>"
    closing_tag = "</p>"


class Head(Element):
    opening_tag = "<head>"
    closing_tag = "</head>"


class OneLineTag(Element):
    def render(self, file_out, ind=""):
        one_line = [self.opening_tag] + self.content + [self.closing_tag]
        file_out.write(("{}{}\n").format(ind, "".join(one_line)))


class Title(OneLineTag):
    opening_tag = "<title>"
    closing_tag = "</title>"


class SelfClosingTag(Element):
    opening_tag = "< />"

    def render(self, file_out, ind=""):
        if self.attributes is not None:
            opening_tag = [self.opening_tag.split('/>')[0]] + self.attributes + ["/>"]
            self.opening_tag = "".join(opening_tag)
        file_out.write(("{}{}\n").format(ind, self.opening_tag))


class Br(SelfClosingTag):
    opening_tag = "<br />"


class Hr(SelfClosingTag):
    opening_tag = "<hr />"


class A(OneLineTag):
    opening_tag = "<a>"
    closing_tag = "</a>"

    def __init__(self, link, content):
        self.opening_tag = '<a href="{}">'.format(link)
        Element.__init__(self, content)


class Ul (Element):
    opening_tag = "<ul>"
    closing_tag = "</ul>"


class Li (Element):
    opening_tag = "<li>"
    closing_tag = "</li>"


class H(OneLineTag):

    def __init__(self, level, content):
        self.opening_tag = "<h{}>".format(level)
        self.closing_tag = "</h{}>".format(level)
        Element.__init__(self, content)


class Meta(SelfClosingTag):
    opening_tag = "<meta />"
