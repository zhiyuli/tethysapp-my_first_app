from tethys_apps.base import TethysAppBase, url_map_maker


class MyFirstApp(TethysAppBase):
    """
    Tethys app class for My First App.
    """

    name = 'My First App'
    index = 'my_first_app:home'
    icon = 'my_first_app/images/icon.gif'
    package = 'my_first_app'
    root_url = 'my-first-app'
    color = '#f1c40f'
        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='my-first-app',
                           controller='my_first_app.controllers.home'),
        )

        return url_maps