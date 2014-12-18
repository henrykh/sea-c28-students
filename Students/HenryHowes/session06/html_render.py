#!/usr/bin/env python


class Element(object):
    opening_tag = "<>"
    closing_tag = "</>"
    indent = ""

    def __init__(self, content=None):
        self.content = []
        if content is not None:
            self.content.append(content)

    def render(self, file_out, ind=""):
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
        file_out.write(("{}{}\n").format(ind, " ".join(one_line)))


class Title(OneLineTag):
    opening_tag = "<title>"
    closing_tag = "</title>"








