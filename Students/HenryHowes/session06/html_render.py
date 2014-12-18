#!/usr/bin/env python


class Element(object):
    opening_tag = "<>"
    closing_tag = "</>"

    def __init__(self, content=None):
        self.content = [self.opening_tag]
        if content is not None:
            self.content.append(content)

    def render(self, file_out, ind=""):
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, (ind+(" "*4)))
            else:
                file_out.write("{}{}\n".format(ind+(" "*4), item))
        file_out.write("{}{}\n".format(ind+(" "*4), self.closing_tag))

    def append(self, additional_content):
        self.content.append(additional_content)


class Html(Element):
    opening_tag = "<html>"
    closing_tag = "</html>"
    indent = ""


class Body(Element):
    opening_tag = "<body>"
    closing_tag = "</body>"


class P(Element):
    opening_tag = "<p>"
    closing_tag = "</p>"
