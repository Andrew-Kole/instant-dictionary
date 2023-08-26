import justpy as jp


class About:

    path = '/about'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='About page', classes='text-4xl m-2')
        jp.Div(a=div,
               text="""Welcome to the Instant Dictionary App! 
        This app is designed to make it easier for you to look up words and find their definitions quickly and easily. 
        We understand how frustrating it can be to search through a dictionary for the definition of a word, 
        so we made the Instant Dictionary App to make it easier for you. 
        With our app, you can look up any word and get its definition in seconds. 
        We are constantly working to improve our app and make it the best dictionary app on the market. 
        We are constantly adding new words and definitions to our database, 
        so you can always trust that you are getting the most up-to-date and accurate information. 
        We hope that you enjoy using our Instant Dictionary App and find it helpful in your search for word definitions. 
        If you have any questions or feedback, please let us know.""",
               classes='text-lg')
        return wp


jp.Route(About.path, About.serve)
jp.justpy(port=8001)
        

