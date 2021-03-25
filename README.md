# TwitterCVEGrabber
 A website to grab some information about CVE discussed every day/week on Twitter
 The aim of this project is to have a global view of the different CVEs discussed every day on Twitter. This allows you to discover new trends and to keep up to date with the latest news.
 
## How does it work ?

Using the Tweepy library, it is possible to perform various queries on Twitter. We get a list of tweets, and, using a regular expression, sort them so as to keep only the CVE numbers. These CVE numbers are then stored in a database to count the number of times they appeared that week or day. We also generate a link to the NIST website for information on CVEs.
Finally, we repeat this operation every 6 hours (due to twitter restrictions) using the apscheduler library.
We have also created an API system where we can retrieve the data stored in the database to populate our tables and charts.



### Requirements 
- Have a developper account on Twitter
- Python3.X
- Edit the .env_sample to .env and fill with all the following information provided by Twitter & Django: 
  - Access Token
  - Access Token Secret
  - Api Key
  - Api Key Secret 
  - Secret Key
 - Run `pip install requirements.txt ` to install dependencies

### WIP
- [x] Populate home page
- [x] Add tabs besides graph for listing each CVE
- [x] Improve the way to display graph
- [ ] Adding more complex CSS
