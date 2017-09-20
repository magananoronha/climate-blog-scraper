from classTemplates import WordpressFormat, BlogspotFormat

class JoNova(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)

    def get_title(self, soup):
        title = soup.find('div', {'class':'post-headline'})
        if title:
            return title.text
        else:
            return None

    def get_body(self, soup):
        body = soup.find('div', {'class':'post-bodycopy'})
        if body:
            return self.concat_body(body)
        else:
            return None
        
    def get_pubtime(self, soup):
        pub_time = soup.find('div', {'class':'post-footer'})
        if pub_time:
            pub_time = pub_time.find('b')
            if pub_time:
                return pub_time.text
        else:
            return None
        
        
class WattsUpWithThat(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
    
    def get_author(self, soup):
        author = soup.find(class_='author')
        if author:
            return author.text
        else:
            return None
        
        
class TimWorstall(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)


        
class NoTricksZone(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
             
        
    def get_pubtime(self, soup):
        pub_time = soup.find('abbr', {'class':'published'})
        if pub_time:
            if 'title' in pub_time.attrs.keys():
                return pub_time['title']
            else:
                return pub_time.text
        else:
            return None            
            
class C3Headlines(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
    def get_pubtime(self, soup):
        pub_time = soup.find('span', {'class':'post-footers'})
        if pub_time:
            return pub_time.text
        else:
            return None

        
    def get_title(self, soup):
        title = soup.find(class_='entry-header')
        if title:
            return title.text
        else:
            return None
        
        
    def get_body(self, soup):
        body = soup.find('div', {'class':'entry-body'})
        if body:
            return self.concat_body(body)
        else:
            return None
        
    
class NotAlotOfPeopleKnowThat(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
        
    def get_body(self, soup):
        body = soup.find('div', {'class':'entry-clear'})
        if body:
             return self.concat_body(body) 
        else:
            return None    
    
    def get_title(self, soup):
        title = soup.find('div', {'class':'post-header'})
        if title:
            title_h = body.find(re.compile(r"^h\d$"))
            if title_h:
                return title_h.text
            else:
                return title.text
        else:
            return None    
        
        
class TallBloke(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
    
    def get_title(self, soup):
        title = soup.find(class_='pagetitle')
        if title:
            return title.text
    
        
        
class StevenGoddard(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
    def get_author(self, soup):
        return 'Steven Goddard'
    
    
class Heartland(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
    
    def get_author(self, soup):
        author = soup.find('a', {'class':'author-url'})
        if author:
            return author.text
        
    def get_title(self, soup):
        title = soup.find(class_='post-title')
        if title:
            title_h = body.find(re.compile(r"^h\d$"))
            if title_h:
                return title_h.text
            
    def get_body(self, soup):
        body = soup.find('div', {'class':'post-entry'})
        if body:
             return self.concat_body(body)
         
            
class AmericanElephant(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)   

    def get_title(self, soup):
        title = soup.find(class_='title')
        if title:
            return title.text.replace(' | American Elephants','')
        
         
class Chiefio(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)   

    def get_author(self, soup):
        author = soup.find('div', {'id':'author-description'})
        author = body.find(re.compile(r"^h\d$"))
        if author_h:
            return author_h.text
        
        
class SunshineHours(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)   
        

class HockeySchtick(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
    
         
            
class AntiGreen(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
        
class TomNelson(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
        
class MikeSmithEnterprisesBlog(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
class ItsFairComment(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
        
class Motls(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
         
class Cfact(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
class ClimateDepot(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
        
    def get_title(self, soup):
        title = soup.find(class_='the-title')
        if title:
            return title.text
        
    def get_author(self, soup):
        author = soup.find('a', {'rel':'author'})
        if author:
            return author.text
        
    def get_pubtime(self, soup):
        pub_time = soup.find('span', {'class':'date-meta'})
        if pub_time:
            return pub_time.text
        else:
            return None
        
class WMBriggs(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
    def get_author(self, soup):
        author = soup.find('span', {'class':'author-name'})
        if author:
            return author.text
        
class HallOfRecord(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
        
class FactsNotFantasy(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)        
        
        
class JenniferMarohasy(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
        
    def get_pubtime(self, soup):
        pub_time = soup.find('abbr', {'class':'published'})
        if pub_time:
            if 'title' in pub_time.attrs.keys():
                return pub_time['title']
            else:
                return pub_time.text
            
            
class JudithCurry(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
        
class CoyoteBlog(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
        
    def get_title(self, soup):
        title = soup.find(class_='posttitle')
        if title:
            title = title.find('a')
            if title:
                return title.text   
            
    def get_pubtime(self, soup):
        pub_time = soup.find('div', {'class':'postmetadata'})
        if pub_time:
            return pub_time.text
        
    def get_body(self, soup):
        body = soup.find('div', {'class':'postentry'})
        if body:
             return self.concat_body(body)
         
          
class ClimateAudit(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        

class AustralianClimateMadness(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content) 
        
                 
    def get_author(self, soup):
        author = soup.find('a', {'rel':'author'})
        if author:
            return author.text
        
    def get_pubtime(self, soup):
        pub_time = soup.find('abbr', {'class':'published'})
        if pub_time:
            if 'title' in pub_time.attrs.keys():
                return pub_time['title']
            else:
                return pub_time.text
            
            
class AutonomousMind(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content) 
        
        
class PielkeClimateSci(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content) 
            
        
class Heliogenic(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content) 
        
        
class NoConsensus(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content) 
        
    def get_title(self, soup):
        title = soup.find('title')
        if title:
            return title.text.replace(' « the Air Vent','')
        
    def get_body(self, soup):
        body = soup.find('div', {'class':'entrytext'})
        if body:
             return self.concat_body(body)
         
            
class Omnologos(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
        
class ScottishSceptic(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
        
class AlGoreLied(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
    def get_title(self, soup):
        title = soup.find(class_='posttitle')
        if title:
            title = title.find('a')
            if title:
                return title.text  
         
            
    def get_pubtime(self, soup):
        pub_time = soup.find('div', {'class':'date'})
        if pub_time:
            month_day = pub_time.text
        year = soup.find('div', {'class':'comment-meta'})
        if year:
            if month_day in year.text:
                pub_time = year.text
        return pub_time
            
    
class SkepticsCorner(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
        
class RogerPielkeJr(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
        
class JulesAndJames(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
        
class NewNostradamusOfTheNorth(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
class TheGWPF(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
    def get_title(self, soup):
        title = soup.find('title')
        if title:
            return title.text.replace('  |  The Global Warming Policy Forum (GWPF)','')

         
    def get_pubtime(self, soup):
        pub_time = soup.find('ul', {'class':'meta'})
        if pub_time:
            pub_time = pub_time.find('li')
            if pub_time:
                return pub_time.text
            
    def get_author(self, soup):
        author = soup.find('ul', {'class':'meta'})
        if author:
            author = author.find_all('li')
            if author:
                return author[2].text
            
            
class BobTisdale(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
        
class ClimateChangePredictions(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
        
class GlobalWarming(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
class ClimateCommonSense2(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
        
class AnHonestClimateDebate(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
    def get_title(self, soup):
        title = soup.find('title')
        if title:
            return title.text.replace(' | An Honest Climate Debate','')
        
         
            
class ClimateConversation(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
        
class WarwickHughes(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
    def get_pubtime(self, soup):
        pub_time = soup.find('span', {'class':'entry-date'})
        if pub_time:
            return pub_time.text
        
class ADogNamedKyoto(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
        
class Klimazwiebel(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
class CoolibahConsulting(WordpressFormat):

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
    def get_body(self, soup):
        post_title = soup.find(class_='art-postheader')
        if post_title:
            return post_title.text
        
    def get_author(self, soup):
        author = soup.find('a', {'rel':'author'})
        if author:
            return author.text
        
    def get_pubtime(self, soup):
        return re.findall("@ (\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d) .*$", str(soup))[0]

class NoFrakkingConsensus(WordpressFormat):        

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
class Omniclimate(WordpressFormat):        

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
    def get_title(self, soup):
        title = soup.find('title')
        if title:
            return title.text.replace(' | The Unbearable Nakedness of CLIMATE CHANGE','')
        
    def get_body(self, soup):
        body = soup.find('div', {'class':'content'})
        if body:
             return self.concat_body(body)
         
class DrRoySpencer(WordpressFormat):        

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
        
    def get_title(self, soup):
        title = soup.find('title')
        if title:
            return title.text.replace(' «  Roy Spencer, PhD','')
        
    def get_pubtime(self, soup):
        pub_time = soup.find('small')
        if pub_time:
            return pub_time.text.replace(' by Roy W. Spencer, Ph. D.','')       

class LeastThing(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
class GlobalClimateScam(BlogspotFormat):        

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
        
    def get_author(self, soup):
        author = soup.find(class_='author')
        if author:
            return author.text
        else:
            return None


class GlobalSham(BlogspotFormat):

    def __init__(self, content):
        BlogspotFormat.__init__(self,content)
        
        
class GreenHellBlog(WordpressFormat):        

    def __init__(self, content):
        WordpressFormat.__init__(self,content)
                
    def get_title(self, soup):
        title = soup.find('title')
        if title:
            return title.text.replace(' | Green Hell Blog','')
        