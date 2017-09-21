class ModifiedWordpress(StandardWordpress):
    def __init__(self, content):
        StandardWordpress.__init__(self,content)

    def first_bold_line(self, body):
        title = body.find(re.compile(r"^h\d$"))
        if title:
            return title.text

    def get_title(self, soup):
        entry_title = soup.find(class_='uk-article-title')
        if entry_title:
            return entry_title.text
        post_title = soup.find('div', {'class':'posttitle'})
        if post_title:
            return post_title.text
        post_title = soup.find('div', {'class':'post-headline'})
        if post_title:
            return post_title.text
        post_title = soup.find(class_='entry-header')
        if post_title:
            return post_title.text
        post_title = soup.find(class_='art-postheader')
        if post_title:
            return post_title.text
        post_title = soup.find(class_='titles')
        if post_title:
            return post_title.text
        body = soup.find('div', {'class':'post'})
        if body:
            return self.first_bold_line(body)
        body = soup.find('div', {'id':'content'})
        if body:
            return self.first_bold_line(body)
        body = soup.find('section', {'id':'content'})
        if body:
            return self.first_bold_line(body)
        else:
            return None


        entry_bold = soup.find(class_='entry-content')
        if entry_bold:
            bold = entry_bold.find('b')
            if bold:
                return bold.text



        abbr_pub = soup.find('abbr', {'class':'published'})
        if abbr_pub:
            if 'title' in abbr_pub.attrs.keys():
                return abbr_pub['title']
            else:
                return abbr_pub.text
        pub_time = soup.find('div', {'class':'post-box-meta-single'})
        if pub_time:
            spans = pub_time.find_all('span')
            if spans:
                return spans[-1].text
        pub_time = soup.find('div', {'class':'postmetadata'})
            if pub_time:
                return pub_time.text
        pub_time = soup.find('span', {'class':'author'})
        if pub_time:
            return pub_time.text
        pub_time = soup.find(class_='meta')
        if pub_time:
            li = pub_time.find('li')
            return li.text
        pub_time = soup.find('time')
        if pub_time:
            return pub_time['datetime']


        body = soup.find('section', {'class':'entry'})
        if body:
             return self.concat_body(body)
        body = soup.find('div', {'class':'entry-container'})
        if body:
             return self.concat_body(body)
        body = soup.find('div', {'class':'post-entry'})
        if body:
             return self.concat_body(body)


         <!-- Performance optimized by W3 Total Cache. Learn more: http://www.w3-edge.com/wordpress-plugins/

Minified using disk
Page Caching using disk: enhanced
Database Caching 6/21 queries in 0.081 seconds using disk
Object Caching 614/659 objects using disk

 Served from: www.coolibahconsulting.com.au @ 2016-12-01 09:08:49 by W3 Total Cache -->
