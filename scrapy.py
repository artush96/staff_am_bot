import scrapy


class WorksSpider(scrapy.Spider):
    name = 'python_works'
    start_urls = ['https://staff.am/en/jobs/categories/index?JobsFilter%5Bkey_word%5D=Python']

    def parse(self, response):
        for link in response.css('a.history_block_padding'):
            print()
            yield [link.css('a ::attr(href)').get()]

        # for next_page in response.css('a.next-posts-link'):
        #     yield response.follow(next_page, self.parse)









        # company_name=response.xpath('/html/body/div[2]/div[3]/div[3]/div[2]/div/a/h1/text()').extract()
        # work_name=response.xpath('//*[@id="job-post"]/div[1]/div[1]/h2/text()').extract()
        # location=response.xpath('//*[@id="job-post"]/div[1]/div[4]/p[2]/text()').extract()
        # job_type=response.xpath('//*[@id="job-post"]/div[1]/div[4]/p[1]/text()').extract()
        # category=response.xpath('//*[@id="job-post"]/div[1]/div[3]/p[2]/text()').extract()
        # job_description=response.xpath('//*[@id="job-post"]/div[2]/p[2]/text()').extract()
        # job_responsibilities=response.xpath('//*[@id="job-post"]/div[2]/ul[1]/text()').extract()
        # required_qualifications=response.xpath('//*[@id="job-post"]/div[2]/ul[2]/text()').extract()
        # required_level=response.xpath('//*[@id="job-post"]/div[2]/h3[4]/span/text()').extract()
        # additional_information=response.xpath('//*[@id="job-post"]/div[2]/div/p/text()').extract()
        # skills=response.xpath('//*[@id="job-post"]/div[3]/div/text()').extract()
        #
        # row_data = zip(company_name,
        #                work_name,
        #                location,
        #                job_type,
        #                category,
        #                job_description,
        #                job_responsibilities,
        #                required_qualifications,
        #                required_level,
        #                additional_information,
        #                skills)
        # print('llllllllll')
        #
        #
        #
        # for item in row_data:
        #     scraped_info = {
        #         'page': response.url,
        #         'company_name': item[0],
        #         'work_name': item[1],
        #         'location': item[2],
        #         'job_type': item[3],
        #         'category': item[4],
        #         'job_description': item[5],
        #         'job_responsibilities': item[6],
        #         'required_qualifications': item[7],
        #         'required_level': item[8],
        #         'additional_information': item[9],
        #         'skills': item[10]
        #     }
        #     print('kkkkkkkkk')
        #     print(scraped_info)
        #     yield scraped_info

