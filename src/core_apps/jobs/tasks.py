import os
import json

import environ
import requests
from celery import shared_task
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from bs4 import BeautifulSoup

from core_apps.jobs.api.job_scraper.job_scraper.spiders.job_spider import (
    JobSpiderSpider,
)

env = environ.Env()
env.read_env(env_file="./../../.envs/.local/.django")


@shared_task
def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(JobSpiderSpider)
    process.start(stop_after_crawl=False)
    return "Job Spider has completed running."


@shared_task
def fetch_visa_jobs():
    url = "https://immi.homeaffairs.gov.au/visas/working-in-australia/skill-occupation-list"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    json_input = soup.find(
        "input", {"id": "ctl00_PlaceHolderMain_PageJSONDataHiddenField_Input"}
    )

    if not json_input:
        raise Exception("Failed to find the JSON data input with the given selector.")

    json_data = json.loads(json_input["value"])

    visa_jobs = {}
    for item in json_data:
        job_title = item["occupation"]
        visas = item["visas"].split(";")
        for visa in visas:
            visa_code = visa.split(" - ")[0].strip()
            if visa_code not in visa_jobs:
                visa_jobs[visa_code] = set()
            visa_jobs[visa_code].add(job_title)

    output_dir = "visa_jobs"
    os.makedirs(output_dir, exist_ok=True)

    for visa_code, jobs in visa_jobs.items():
        file_path = os.path.join(output_dir, f"{visa_code}.txt")
        with open(file_path, "w") as file:
            for job in jobs:
                file.write(f"{job}\n")

    return "Job titles have been categorized and written to text files."
