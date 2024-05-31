import os
import scrapy
from scrapy_splash import SplashRequest


class JobSpiderSpider(scrapy.Spider):
    name = "job_spider"
    start_urls = [
        "https://immi.homeaffairs.gov.au/visas/working-in-australia/skill-occupation-list"
    ]

    def start_requests(self):
        print("----start requests-------------------")
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={"wait": 20})

    def parse(self, response):
        visa_jobs = {}

        rows = response.xpath('//*[@id="table-to-label-0"]/table/tbody/tr')
        for job in rows:
            job_title = " ".join(job.xpath("td[1]//text()").extract()).strip()
            visa_categories = job.xpath("td[3]//li/text()").extract()

            for visa_category in visa_categories:
                visa_code = visa_category.split(" - ")[0].strip()
                if visa_code not in visa_jobs:
                    visa_jobs[visa_code] = []
                visa_jobs[visa_code].append(job_title)

        output_dir = "visa_jobs"
        os.makedirs(output_dir, exist_ok=True)

        for visa_code, jobs in visa_jobs.items():
            with open(os.path.join(output_dir, f"{visa_code}.txt"), "w") as file:
                for job in jobs:
                    file.write(f"{job}\n")

        self.log("Job titles have been categorized and written to text files.")
