# scrapy shell -s USER_AGENT="""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36""" "https://stackoverflow.com/questions?sort=featured"
# response.css("h3 > a.question-hyperlink::text").extract()
# scrapy shell -s USER_AGENT="""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36""" "https://stackoverflow.com/questions/60760904/add-security-header-to-a-soap-message"
# scrapy shell -s USER_AGENT="""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36""" "https://stackoverflow.com/questions/60555241/how-to-pipe-stdout-from-docker-run-in-dockerpy"
# response.css("#answers-header > div > h2::text").re(r"(\d)\s[A-Z][a-z]+"
# response.css('span[itemprop="answerCount"]::text').extract()
