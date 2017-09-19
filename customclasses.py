class JoNova(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)

    def get_title(self, soup):
        post_title = soup.find('div', {'class':'post-headline'})
        if post_title:
            return post_title.text
        else:
            return None

    def get_author(self, soup):
        return 'Joanne Nova'

    def get_body(self, soup):
        body = soup.find('div', {'class':'post-bodycopy'})
        if body:
            return self.concat_body(body)

    def get_pubtime(self, soup):
        pub_time = soup.find('div', {'class':'post-footer'})
        if pub_time:
            pub_time = pub_time.find('b')
            if pub_time:
                return pub_time.text
