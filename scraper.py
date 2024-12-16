from playwright.sync_api import sync_playwright

def scrape_headings_and_paragraphs(url):
    """
    Scrapes all headings (h1, h2, h3, etc.) and their corresponding paragraphs from a webpage.
    Returns a list of tuples with heading text and the associated paragraph(s).
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the website
        page.goto(url)

        # Wait for content to load
        page.wait_for_load_state("domcontentloaded")

        # Locate all headings and paragraphs
        elements = page.locator("h1, h2, h3, h4, h5, h6, p")

        # Combine headings with their following paragraphs
        result = []
        current_heading = None
        for i in range(elements.count()):
            element = elements.nth(i)
            tag_name = element.evaluate("el => el.tagName.toLowerCase()")
            text = element.inner_text().strip()

            if tag_name.startswith("h"):  # If it's a heading
                if current_heading:  # Save the previous heading and its paragraphs
                    result.append(current_heading)
                current_heading = (text, [])
            elif tag_name == "p" and current_heading:  # If it's a paragraph
                current_heading[1].append(text)

        # Add the last heading and paragraphs if any
        if current_heading:
            result.append(current_heading)

        # Close the browser
        browser.close()

        return result
