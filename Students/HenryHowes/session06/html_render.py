#!/usr/bin/env python


class Element(object):
    opening_tag = "<>"
    closing_tag = "</>"
    indent = ""

    def __init__(self, content=None, **kwargs):
        self.content = []
        if kwargs:
            opening_tag = [self.opening_tag.split('>')[0]]
            for key in kwargs:
                opening_tag.append('{}="{}"'.format(key, kwargs[key]))
            opening_tag.append(">")
            self.opening_tag = " ".join(opening_tag)
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

#TODO - Is tag the best way to do this ?
class SelfClosingTag(Element):
    tag = "< />"

    def render(self, file_out, ind=""):
        file_out.write(("{}{}\n").format(ind, self.tag))


class Br(SelfClosingTag):
    tag = "<br />"


class Hr(SelfClosingTag):
    tag = "<hr />"


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
        self.closing_tag = "<\h{}>".format(level)
        Element.__init__(self, content)




