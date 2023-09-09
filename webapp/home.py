import justpy as jp

class Home:
    """represents home page"""

    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view='hHh lpR fFf')
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode='left', bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes='fit')
        q_list = jp.QList(a=scroller)
        a_classes = 'p-2 m-2 text-lg text-blue-400 hover:text-blue-700'
        jp.A(a=q_list, text='Home', href='/', classes=a_classes)
        jp.Br(a=q_list)
        jp.A(a=q_list, text='Dictionary', href='/dictionary', classes=a_classes)
        jp.Br(a=q_list)
        jp.A(a=q_list, text='About', href='/about', classes=a_classes)
        jp.Br(a=q_list)
        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon='menu', click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text='Instant Dictionary')
        container = jp.QPageContainer(a=layout, )

        div = jp.Div(a=container, classes='bg-gray-200 h-screen p-2')
        jp.Div(a=div, text='Home page', classes='text-4xl m-2')
        jp.Div(a=div,
               text="""Welcome to Instant Dictionary – the fastest and easiest way to look up words and definitions! 
           With our app, you can quickly search for words and get accurate definitions in a matter of seconds. 
           Whether you're studying for a test or just curious about the meaning of a word, 
           Instant Dictionary has you covered. 
           Use our app now and get instant access to the world's most comprehensive dictionary!""",
               classes='text-lg')
        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True

