from templates.classTemplates import WordpressFormat, BlogspotFormat
import re
   

class extractors(): 
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

    
        def get_title(self, soup):
            title = soup.find('div', {'class':'post-header'})
            if title:
                title_h = title.find(re.compile(r"^h\d$"))
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
            else:
                return None    
    
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
            else:
                return None            
    
        def get_title(self, soup):
            title = soup.find(class_='post-title')
            if title:
                title_h = title.find(re.compile(r"^h\d$"))
                if title_h:
                    return title_h.text
                else:
                    return None
            else:
                return None     
            
            
        def get_body(self, soup):
            body = soup.find('div', {'class':'post-entry'})
            if body:
                 return self.concat_body(body)
            else:
                return None                   
             
        def get_pubtime(self, soup):
            pub_time = soup.find('span', {'class':'date'})
            if pub_time:
                return pub_time.text
            else:
                return None    
    
    class AmericanElephant(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    class Chiefio(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_author(self, soup):
            author = soup.find('div', {'id':'author-description'})
            author_h = author.find(re.compile(r"^h\d$"))
            if author_h:
                return author_h.text
            else:
                return None   
            
            
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
            else:
                return None               
            
    
        def get_author(self, soup):
            author = soup.find('a', {'rel':'author'})
            if author:
                return author.text
            else:
                return None               
    
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
            else:
                return None               
            
    
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
            else:
                return None                   
    
    
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
            else:
                return None               
            
    
        def get_body(self, soup):
            body = soup.find('div', {'class':'postentry'})
            if body:
                 return self.concat_body(body)
            else:
                return None                   
    
    
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
            else:
                return None       
    
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
                return re.findall('(.*)«',title.text)
            else:
                return None               
            
    
        def get_body(self, soup):
            body = soup.find('div', {'class':'entrytext'})
            if body:
                 return self.concat_body(body)
            else:
                return None                   
    
    
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
                else:
                    return None   
            else:
                return None       
    
        def get_pubtime(self, soup):
            pub_time = soup.find('div', {'class':'date'})
            if pub_time:
                month_day = pub_time.text
                year = soup.find('div', {'class':'comment-meta'})
                if year:
                    if month_day in year.text:
                        pub_time = year.text
                        return pub_time
                return pub_time.text
            else:
                return None
    
    
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
    
    class TheGWPFCom(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
        def get_pubtime(self, soup):
            pub_time = soup.find('ul', {'class':'meta'})
            if pub_time:
                pub_time_li = pub_time.find('li')
                if pub_time_li:
                    return pub_time_li.text.replace('Date: ','')
                else:
                    return pub_time.text
            else:
                return None                   
    
        def get_author(self, soup):
            author = soup.find('ul', {'class':'meta'})
            if author:
                author_li = author.find_all('li')
                if author_li and len(author_li) == 3:
                    return author_li[2].text
                else:
                    return author.text
            else:
                return None       
    
    
    class BobTisdale(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    class ClimateChangePredictions(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    class GlobalWarming(WordpressFormat):
    
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
                
    
    class ClimateCommonSense2(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)
    
    
    class AnHonestClimateDebate(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
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
            else:
                return None               
    
    class ADogNamedKyoto(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)
    
    
    class Klimazwiebel(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)
    
    class CoolibahConsulting(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_title(self, soup):
            post_title = soup.find(class_='art-postheader')
            if post_title:
                return post_title.text
            else:
                return None               
    
        def get_author(self, soup):
            author = soup.find('a', {'rel':'author'})
            if author:
                return author.text
            else:
                return None   
            
            
        def get_pubtime(self, soup):
            return re.findall("@ (\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d) .*$", str(soup))[0]
        
        def get_body(self, soup):
            body = soup.find(class_='art-postcontent')
            if body:
                 return self.concat_body(body)
            else:
                return None                
                
    class NoFrakkingConsensus(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    class Omniclimate(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_body(self, soup):
            body = soup.find('div', {'class':'content'})
            if body:
                 return self.concat_body(body)
            else:
                return None   
            
            
    class DrRoySpencer(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_title(self, soup):
            title = soup.find('title')
            if title:
                return re.findall('(.*)«',title.text)[0]
            else:
                return None   
            
        def get_pubtime(self, soup):
            pub_time = soup.find('small')
            if pub_time:
                return pub_time.text.replace(' by Roy W. Spencer, Ph. D.','')
            else:
                return None   
            
            
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

    
    class DevConsultancyGroup(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)
    
    
    #this one blocked me, but basic wordpress works on what I have downloaded
    class CarbonFolly(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    class CarbonSense(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_title(self, soup):
            title = soup.find('title')
            if title:
                return title.text
            else:
                return None               
    
        def get_body(self, soup):
            body = soup.find('div', {'class':'storybody'})
            if body:
                 return self.concat_body(body)
            else:
                return None   
                
    
        def get_pubtime(self, soup):
            pub_time = soup.find(class_='postmetadata')
            if pub_time:
                return re.findall('(.*)\|',pub_time.text)[0]
            else:
                return None
    
    class Dddusmma(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_title(self, soup):
            title = soup.find('div', {'class':'post-header'})
            if title:
                title_h = title.find(re.compile(r"^h\d$"))
                if title_h:
                    return title_h.text
                else:
                    return title.text
            else:
                return None                   
    
    
    class ClimateSkeptic(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
        def get_pubtime(self, soup):
            pub_time = soup.find('time')
            if pub_time:
                if 'datetime' in pub_time.attrs.keys():
                    return pub_time['datetime']
                else:
                    return pub_time.text
            else:
                return None   
    
    
    class PolarBearScience(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    class GlobalFreeze(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)

    
        def get_body(self, soup):
            body = soup.find('div', {'class':'words'})
            if body:
                 return self.concat_body(body)
            else:
                return None       
    
    class ClimateResistance(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_title(self, soup):
            post_title = soup.find(class_='art-postheader')
            if post_title:
                return post_title.text
            else:
                return None               
    
        def get_body(self, soup):
            body = soup.find(class_='art-postcontent')
            if body:
                 return self.concat_body(body)
            else:
                return None                   
    
    class Co2Insanity(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    class TheLukewarmersWay(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    
    class NextGrandMinimum(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    class HiIzuru(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    class RClutz(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    class ClimateNonconformist(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    class HRo001(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    class Moyhu(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)
    
    
    class ThePointman(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_title(self, soup):
            title = soup.find(class_='posttitle')
            if title:
                title_h = title.find(re.compile(r"^h\d$"))
                if title_h:
                    return title_h.text
                else:
                    return title.text
            else:
                return None   
            
        def get_author(self, soup):
            author = soup.find(class_='postauthor')
            if author:
                author_a = author.find('a')
                if author_a:
                    return author_a.text
                else:
                    return author.text
            else:
                return None                   
    
    class Co2Coalition(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_body(self, soup):
            body = soup.find('div', {'class':'entry-summary'})
            if body:
                 return self.concat_body(body)
            else:
                return None                   
    
    
    class TrustYetVerify(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    class GustOfHotAir(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)
    
    
    class ClimateLessons(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)
    
    class Scientificqa(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)
    
    
    class CliveBest(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    class DiggingInTheClay(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    class Hypsithermal(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    class ClimateChangeDispatch(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_title(self, soup):
            entry_title = soup.find(class_='uk-article-title')
            if entry_title:
                return entry_title.text
    
    
        def get_body(self, soup):
            body = soup.find(class_='tm-article-content')
            if body:
                 return self.concat_body(body)
            else:
                return None                   
             
        def get_pubtime(self, soup):
            pub_time = soup.find('time')
            if pub_time:
                if 'datetime' in pub_time.attrs.keys():
                    return pub_time['datetime']
                else:
                    return pub_time.text
            else:
                return None                   
                
    
    class TheGWPFOrg(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
        def get_pubtime(self, soup):
            pub_time = soup.find('ul', {'class':'meta'})
            if pub_time:
                pub_time_li = pub_time.find('li')
                if pub_time_li:
                    return pub_time_li.text.replace('Date: ','')
                else:
                    return pub_time.text
            else:
                return None                   
                
    
        def get_author(self, soup):
            author = soup.find('ul', {'class':'meta'})
            if author:
                author_li = author.find_all('li')
                if author_li and len(author_li) == 3:
                    return author_li[2].text
                else:
                    return author.text
            else:
                return None                   
    
    class CcgiNewbery1(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
        def get_title(self, soup):
            title = soup.find(class_='posttitle')
            if title:
                title = title.find('a')
                if title:
                    return title.text
            else:
                return None                   
    
        def get_pubtime(self, soup):
            pub_time = soup.find('span', {'class':'author'})
            if pub_time:
                return pub_time.text.replace('\r\n\tPosted by TonyN on ','')
            else:
                return None       
    
    class Nigguraths(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_body(self, soup):
            body = soup.find('div', {'class':'content'})
            if body:
                 return self.concat_body(body)
            else:
                return None                   
    
    
    class AllRightAllRight(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)
    
    
    class ScienceOfDoom(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_title(self, soup):
            title = soup.find(class_='posttitle')
            if title:
                title = title.find('a')
                if title:
                    return title.text
                else:
                    return None                   
            else:
                return None                   
    
    
    class RhinoHide(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)

    
    class TheClimateBet(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_title(self, soup):
            title = soup.find('title')
            if title:
                return title.text.replace(' at The Global Warming Challenge','')
            else:
                return None               
    
        def get_body(self, soup):
            body = soup.find('div', {'class':'main'})
            if body:
                 return self.concat_body(body)
            else:
                return None                   
    
        def get_pubtime(self, soup):
            pub_time = soup.find('div', {'class':'signature'})
            if pub_time:
                pub_time_p = pub_time.find_all('p')
                if pub_time_p:
                    return pub_time_p[1].text
                else:
                    return pub_time.text
            else:
                return None                   
                
    
    class ClimateSanity(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
        def get_body(self, soup):
            body = soup.find('div', {'class':'entrytext'})
            if body:
                 return self.concat_body(body)
            else:
                return None                   
    
    
    class AGWHeretic(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)
    
    
    class GeoffChambers(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    class DefyCCC(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    class Hiizuru(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
    
    class TheClimateGateBook(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_pubtime(self, soup):
            pub_time = soup.find('span', {'class':'post-info2'})
            if pub_time:
                pub_time.a.decompose()
                return re.findall('on (.*)\|',pub_time.text)[0]
            else:
                return None               
    
        def get_title(self, soup):
            title = soup.find(class_='titles')
            if title:
                title_a = title.find('a')
                if 'title' in title_a.attrs.keys():
                    return title_a['title']
                else:
                    return title.text
            else:
                return None
    
        def get_body(self, soup):
            body = soup.find('div', {'class':'home-post-wrap'})
            if body:
                 return self.concat_body(body)
            else:
                return None                   
             
    
    class HauntingTheLibrary(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)   
            
            
    class CarlinEconomics(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)  
            
        def get_title(self, soup):
            title = soup.find('title')
            if title:
                return re.findall('» (.*)',title.text)[0]
            else:
                return None               
            
    class PetesPlace(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)   
            
            
    class PrincipiaScientific(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
    
        def get_title(self, soup):
            entry_title = soup.find(class_='uk-article-title')
            if entry_title:
                return entry_title.text
            else:
                return None               
    
    
        def get_pubtime(self, soup):
            pub_time = soup.find('time')
            if pub_time:
                if 'datetime' in pub_time.attrs.keys():
                    return pub_time['datetime']
                else:
                    return pub_time.text
            else:
                return None                   
    
        def get_body(self, soup):
            body = soup.find(class_='uk-article')
            if body:
                 return self.concat_body(body)
            else:
                return None                   
             
    class ClimateOfSophistry(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)       
            
    class Three000Quads(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content) 
            
            
    class SkepticalSwedishScientists(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content) 
            
    
    class TalkingAboutTheWeather(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
            
    class RealClimateScience(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
            
            
    class CGFI(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)       
            
            
    class ClimateEdinburgh(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content) 
            
            
    class ClimateGuy(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content) 
            
            
    class CalderUp(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
            

    class PopularTechnology(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)      
            
            
    class JunkScience(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)            
            
    class SteveMosher(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)  
            
        def get_body(self, soup):
            body = soup.find('div', {'class':'content'})
            if body:
                 return self.concat_body(body)
            else:
                return None                   
             
    class ImpactOfCC(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)   
            
            
    class TroyCA(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content) 
        
    
        def get_body(self, soup):
            body = soup.find('div', {'class':'storycontent'})
            if body:
                 return self.concat_body(body)
            else:
                return None                   
             
                
    class NoCarbonTax(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content) 
            

    class TheInconvenientSkeptic(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)             
            
            
        def get_body(self, soup):
            body = soup.find('div', {'id':'content'})
            if body:
                 return self.concat_body(body)    
            else:
                return None                   
                
             
        def get_title(self, soup):
            title = soup.find('title')
            if title:
                title_car = re.findall('»(.*)',title.text)[0]
                if title_car:
                    return title_car
                else:
                    return None
            else:
                return None                       
             
        def get_pubtime(self, soup):
            pub_time = soup.find('div', {'class':'post-details'})
            if pub_time:
                pub_time_h = pub_time.find(re.compile(r"^h\d$"))
                if pub_time_h:
                    return re.findall('inconvenientskeptic on (.*)', pub_time_h.text)[0]
            else:
                return None
            
            
    class KiwiThinker(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)   
            
            
    class ClimateSenseNorpag(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)   
            
            
    class UnsettledClimate(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)   
            
            
    class TreesForTheForest(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)   
            
            
    class ThePompousGit(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)   
            
    class FriendsOfCo2(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)  
            
    class ClimateContrarian(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)       
            
            
    class FakeGate(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content) 
            
    class EnthusiasmScepticismScience(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)  

    class StatPad(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)   
            
    class DeadmanTurner(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
            
    class IceAgeNow(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
            
            
    class PaulMacrae(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
            
        def get_pubtime(self, soup):
            pub_time = soup.find(class_='posted')
            if pub_time:
                return re.findall('on (.*)', pub_time.text)[0]
            else:
                return None               
            
            
    class TheWeatherWiz(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content) 
            
            
    class GlobalWarmingFactOrFiction(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
            
        def get_title(self, soup):
            title = soup.find('title')
            if title:
                return re.findall('» (.*)',title.text)[0]
            else:
                return None               
            
        def get_pubtime(self, soup):
            pub_time = soup.find('div', {'class':'postdate'})
            if pub_time:
                return re.findall('on (.*) by',pub_time.text)[0]
            else:
                return None               
            
            
    class PoliClimate(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)
            
        def get_body(self, soup):
            body = soup.find('div', {'class':'user-content'})
            if body:
                 return self.concat_body(body)
            else:
                return None                
                
    class Ubilibertas(WordpressFormat):
    
        def __init__(self, content):
            WordpressFormat.__init__(self,content)  
            
            
    class PerhapsAllNatural(BlogspotFormat):
    
        def __init__(self, content):
            BlogspotFormat.__init__(self,content)  