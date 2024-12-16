from scraper import scrape_headings_and_paragraphs
from poster import create_post

if __name__ == "__main__":
    # URL to scrape
    scrape_url = "http://webserver"

    # Scrape the content
    headings_and_paragraphs = scrape_headings_and_paragraphs(scrape_url)

    # Create a WordPress post for each heading and its paragraphs
    for heading, paragraphs in headings_and_paragraphs:
        # Combine paragraphs into a single content string
        content = "\n".join([f"<p>{paragraph}</p>" for paragraph in paragraphs])

        # Create the post with the heading as the title and paragraphs as content
        create_post(heading, content)
