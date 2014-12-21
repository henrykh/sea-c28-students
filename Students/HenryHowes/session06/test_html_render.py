#!/usr/bin/env python


import codecs
import cStringIO
import os

import html_render as hr


def render(page, filename):
    """
    render the tree of elements

    This uses cSstringIO to renderto memory, then dump to console and
    write to file -- very handy!
    """

    f = cStringIO.StringIO()
    page.render(f)

    f.reset()

    print f.read()

    f.reset()
    codecs.open(filename, 'w', encoding="utf-8").write(f.read())


def test_step_1():
    page = hr.Element()
    page.append(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text")
    page.append(u"And here is another piece of text -- you should be able to add any number")
    render(page, u"test_1.txt")
    test_output = open('test_1.txt', 'r')
    test_example = open('html_test/test_html_output1.html')
    assert test_output.read() == test_example.read()
    os.remove('test_1.txt')
    test_example.close()


def test_step_2():
    page = hr.Html()
    body = hr.Body()
    body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))
    body.append(hr.P(u"And here is another piece of text -- you should be able to add any number"))
    page.append(body)
    render(page, u"test_2.txt")
    test_output2 = open('test_2.txt', 'r')
    test_example2 = open('html_test/test_html_output2.html')
    assert test_output2.read() == test_example2.read()
    os.remove('test_2.txt')
    test_example2.close()

 
def test_step_3():
    page = hr.Html()

    head = hr.Head()
    head.append(hr.Title(u"PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))
    body.append(hr.P(u"And here is another piece of text -- you should be able to add any number"))

    page.append(body)

    render(page, u"test_3.txt")
    test_output3 = open('test_3.txt', 'r')
    test_example3 = open('html_test/test_html_output3.html')
    assert test_output3.read() == test_example3.read()
    os.remove('test_3.txt')
    test_example3.close()


def test_step_4():  
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title(u"PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                    style=u"text-align: center; font-style: oblique;"))
    page.append(body)
    render(page, u"test_4.txt")
    test_output4 = open('test_4.txt', 'r')
    test_example4 = open('html_test/test_html_output4.html')
    assert test_output4.read() == test_example4.read()
    os.remove('test_4.txt')
    test_example4.close()


def test_step_5():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title(u"PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                  style=u"text-align: center; font-style: oblique;"))

    body.append(hr.Hr())
    page.append(body)
    render(page, u"test_5.txt")

    test_output5 = open('test_5.txt', 'r')
    test_example5 = open('html_test/test_html_output5.html')
    assert test_output5.read() == test_example5.read()
    os.remove('test_5.txt')
    test_example5.close()


def test_step_6():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title(u"PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                  style=u"text-align: center; font-style: oblique;"))

    body.append(hr.Hr())

    body.append(u"And this is a ")
    body.append( hr.A(u"http://google.com", "link") )
    body.append(u"to google")

    page.append(body)

    render(page, u"test_6.txt")
    test_output6 = open('test_6.txt', 'r')
    test_example6 = open('html_test/test_html_output6.html')
    assert test_output6.read() == test_example6.read()
    os.remove('test_6.txt')
    test_example6.close()


def test_step_7():
    page = hr.Html()

    head = hr.Head()
    head.append(hr.Title(u"PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append( hr.H(2, u"PythonClass - Class 6 example") )

    body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                  style=u"text-align: center; font-style: oblique;"))

    body.append(hr.Hr())

    list = hr.Ul(id=u"TheList", style=u"line-height:200%")

    list.append( hr.Li(u"The first item in a list") )
    list.append( hr.Li(u"This is the second item", style="color: red") )

    item = hr.Li()
    item.append(u"And this is a ")
    item.append( hr.A(u"http://google.com", u"link") )
    item.append(u"to google")

    list.append(item)

    body.append(list)

    page.append(body)

    render(page, u"test_7.txt")
    test_output7 = open('test_7.txt', 'r')
    test_example7 = open('html_test/test_html_output7.html')
    assert test_output7.read() == test_example7.read()
    os.remove('test_7.txt')
    test_example7.close()


def test_step_8():

    page = hr.Html()


    head = hr.Head()
    head.append( hr.Meta(charset=u"UTF-8") )
    head.append(hr.Title(u"PythonClass = Revision 1087:"))

    page.append(head)

    body = hr.Body()

    body.append( hr.H(2, u"PythonClass - Class 6 example") )

    body.append(hr.P(u"Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                  style=u"text-align: center; font-style: oblique;"))

    body.append(hr.Hr())

    list = hr.Ul(id=u"TheList", style=u"line-height:200%")

    list.append( hr.Li(u"The first item in a list") )
    list.append( hr.Li(u"This is the second item", style="color: red") )

    item = hr.Li()
    item.append(u"And this is a ")
    item.append( hr.A(u"http://google.com", "link") )
    item.append(u"to google")

    list.append(item)

    body.append(list)

    page.append(body)

    render(page, u"test_8.txt")
    test_output8 = open('test_8.txt', 'r')
    test_example8 = open('html_test/test_html_output8.html')
    assert test_output8.read() == test_example8.read()
    os.remove('test_8.txt')
    test_example8.close()

    
