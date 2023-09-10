import justpy as jp
import layout

class Home:
    """represents home page"""

    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

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
