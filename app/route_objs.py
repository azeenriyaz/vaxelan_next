from .utils import VaxelanRoute

class Routes():
    def __init__(self):
        pass

    Home = VaxelanRoute("/","Home - Vaxelan", "main/home.html")
    About = VaxelanRoute("/about/","About", "main/about.html")
    download = VaxelanRoute('/downloads/<path:filename>', "" , "")
