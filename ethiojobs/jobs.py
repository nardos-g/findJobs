import scrapy

class myScrapy(scrapy.Spider):
    name = 'ethiojobs'

    start_urls = {
        'https://www.ethiojobs.net/browse-by-category/Engineering/',
        'https://www.ethiojobs.net/browse-by-category/Education/',
        'https://www.ethiojobs.net/browse-by-category/Automotive/',
        'https://www.ethiojobs.net/browse-by-category/Maintenance/',
        'https://www.ethiojobs.net/browse-by-category/Manufacturing/',
        'https://www.ethiojobs.net/browse-by-category/Science%20and%20Technology/',
        'https://www.ethiojobs.net/browse-by-category/Information%20Technology/',
        'https://www.ethiojobs.net/browse-by-category/Sales%20and%20Marketing/'
    }

    
    def parse(self, response):
            for job in response.css('.listing-section'):
                yield{
                    'Name': job.css('a::text').get(),
                    'company': job.css('.company-name::attr(title)').get(),
                    'Address': job.css('.work-palce::text').re(r'[a-zA-Z ]+\,?[a-zA-Z]+'),
                    'Level': job.css('.captions-field:nth-child(7)::text').get(),
                    'Link': job.css('.viewDetails a::attr(href)').get()
                }
        
            next = response.xpath('//div[@class="col-xs-7 no-padding-right text-right"]//i[@class="fa fa-chevron-right"]/../@href').get()
            if next is not None:
                yield response.follow(next, self.parse)
            
        
print("Nardos is not getting luck in this stages")

                