# Visa Job Scraper

This project scrapes job titles related to various visa codes from the Australian immigration website and categorizes them into separate text files.

## Prerequisites

- Docker
- Docker Compose
- Make (optional, for using the Makefile)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Amirbapiri/direction_int_task.git
    cd direction_int_task
    ```

## Makefile Commands

The `Makefile` provides convenient commands for common tasks:

- Build Docker containers:
    ```bash
    make build
    ```

- Build and run Docker containers in the foreground:
    ```bash
    make vbuild
    ```

- Start Docker containers:
    ```bash
    make up
    ```

- Start Docker containers in the foreground:
    ```bash
    make vup
    ```

- Stop Docker containers:
    ```bash
    make down
    ```

- Stop and remove Docker containers, networks, volumes, and images:
    ```bash
    make down-v
    ```

## Endpoints

### Job Fetch API

- **URL:** `http://localhost:8080/api/v1/jobs/fetch/`
- **Method:** `POST`
- **Description:** Fetches and categorizes job titles related to various visa codes.

## Running the Project

1. Build and start the Docker containers:
    ```bash
    make vbuild
    ```

2. To fetch and categorize job titles, send a POST request to the `/api/v1/jobs/fetch/` endpoint:
    ```bash
    curl -X POST http://localhost:8080/api/v1/jobs/fetch/
    ```

## Scrapy Job Spider

The job can also be run using Scrapy, though it faced integration issues with Celery:

1. To run the Scrapy job spider, use the following command:
    ```bash
    scrapy crawl job_spider
    ```

This will scrape job titles from the specified URL and categorize them into text files as defined in the `job_spider.py`.

## Directory Structure

- `.envs/.local/.django`: Environment variables for the Django application.
- `Makefile`: Contains commands to manage Docker containers.
- `job_spider.py`: Scrapy spider for scraping job titles.
- `tasks.py`: Celery task for fetching and categorizing job titles using BeautifulSoup.
- `docker-compose.dev.yml`: Docker Compose configuration for development.

## Notes

- Ensure that the Docker containers are up and running before making API requests.
- The `Scrapy` implementation was initially used but faced issues with integration into `Celery`. The current implementation uses `BeautifulSoup` for scraping.

