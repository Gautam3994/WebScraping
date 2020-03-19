import scrapy
from scrapy.mail import MailSender
import os


class StackOverFlowEmailSpider(scrapy.Spider):
    name = "email_sender"
    # start_urls = ["https://stackoverflow.com/questions/60760904/add-security-header-to-a-soap-message"]
    start_urls = ["https://stackoverflow.com/questions/60555241/how-to-pipe-stdout-from-docker-run-in-dockerpy"]

    def parse(self, response):
        # answer_flag = response.css("#answers-header > div > h2::text").re(r"(\d)\s[A-Z][a-z]+")
        answer_flag = response.css('span[itemprop="answerCount"]::text').extract()
        # if not answer_flag:
        if answer_flag[0] == "0":
            self.logger.info("There are No Answers on this question yet!")
        else:
            mailer = MailSender(
                smtphost="smtp.gmail.com",
                mailfrom=os.environ.get("EMAIL"),
                smtpuser=os.environ.get("EMAIL"),
                smtppass=os.environ.get("PASSWORD"),
                smtpport=587
            )
            msg_body = "Hi There,\n\nThere are " + answer_flag[0] + " answers to your question on stackoverflow. " + "Here's the link:\n" + response.url
            # IN BELOW YOU WILL GET ERR IF YOU DONT SEND THE MAIL IN RETURN STATEMENT DUE TO TLS ISSUE
            # ALTERNATIVELY YOU COULD SEND MAILS IN PIPELINES
            return mailer.send(to=["gautam3994@gmail.com"], subject="Someone responsed to your question on stackoverflow", body=msg_body, cc=["deadpoolv907@gmail.com"])
