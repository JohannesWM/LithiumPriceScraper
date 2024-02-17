from Scrape_Testing import scrape_funs


if __name__ == "__main__":
    print("Scraping...")
    page_html = scrape_funs.request_to_site(scrape_funs.Link)
    print("Dumping html...")
    scrape_funs.dump_html(page_html, "scrape_test.html")
    print("Scraping html...")
    GFEXdata = scrape_funs.GFEX_scrape(page_html)
    LithiumDataList = scrape_funs.soup_scrape(page_html)
    print("Dumping data...")
    scrape_funs.dump_xlsx(LithiumDataList)
    scrape_funs.dump_xlsx(GFEXdata, GFEX=True)
    print("Done.")

