from lxml import html
import requests

import json

base_url = 'https://staff.am'
general_url = base_url + '/en/jobs/categories/index?JobsFilter%5Bkey_word%5D=Python'

get_url_list_page = requests.get(general_url, verify=False)
get_url_list_content = html.fromstring(get_url_list_page.content)
urls =[]
for href in get_url_list_content.xpath('//a[(@class="load-more btn width100 job_load_more radius_changes")]'):
    url = base_url + href.attrib['href']
    urls.append(url)

filtered_data = []
for url in urls:
    get_data_page = requests.get(url, verify=False)
    get_data_content = html.fromstring(get_data_page.content)

    company_name=get_data_content.xpath('/html/body/div[2]/div[3]/div[3]/div[2]/div/a/h1/text()')
    work_name=get_data_content.xpath('//*[@id="job-post"]/div[1]/div[1]/h2/text()')
    location=get_data_content.xpath('//*[@id="job-post"]/div[1]/div[4]/p[2]/text()')[1]
    job_type=get_data_content.xpath('//*[@id="job-post"]/div[1]/div[4]/p[1]/text()')[1]
    category=get_data_content.xpath('//*[@id="job-post"]/div[1]/div[3]/p[2]/text()')[1]
    job_description=get_data_content.xpath('//*[@id="job-post"]/div[2]/p[2]/text()')

    for li in get_data_content.xpath('//*[@id="job-post"]/div[2]/ul[1]'):
        job_responsibilities = li.xpath('li/text()')

    for li in get_data_content.xpath('//*[@id="job-post"]/div[2]/ul[2]'):
        required_qualifications = li.xpath('li/text()')

    required_level=get_data_content.xpath('//*[@id="job-post"]/div[2]/h3[4]/span/text()')

    for s in get_data_content.xpath('//*[@id="job-post"]/div[3]/div'):
        skills = s.xpath('p/span/text()')


    data = {
        'url': url,
        'company_name': str(company_name),
        'work_name': str(work_name),
        'location': str(location),
        'job_type': str(job_type),
        'category': str(category),
        'job_description': str(job_description).replace(u'\u00a0', u' '),
        'job_responsibilities': str(job_responsibilities).replace(u'\\xa0', u' '),
        'required_qualifications': str(required_qualifications).replace('\\xa0', ' '),
        'required_level': str(required_level),
        'skills': str(skills)
    }
    filtered_data.append(data)

print(json.dumps(filtered_data, indent=4))

