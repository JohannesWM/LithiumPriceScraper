from Scrape_Testing import scrape_funs
from Lithium_Mail import *
import datetime


if __name__ == "__main__":
    try:
        current_date = datetime.date.today()

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

        if current_date.weekday() == 4:
            print("sending email, its friday!")
            lithium_mail(receiver_email, "Lithium Price History", f"Here is the lithium price history as of "
                                                                  f"{str(current_date)}", error=False)
            lithium_mail(developer_email, "Lithium Sent", f"Lithium price history sent for {current_date}",
                         error=False)

    except Exception as e:
        print("An Error has Occurred")
        lithium_mail(developer_email, "An Error Occurred during \'Lithium Price Scraping\'", f"{str(e)}"
                     , error=True)
