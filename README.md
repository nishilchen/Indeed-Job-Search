# Indeed Job Search
As an international student, keywords like "US citizen required" or "Security Clearance" are the most unwanted words in the requirement. This project aims at filtering jobs with these keywords.

[Indeed](https://www.indeed.com/)

Here's the demo:
```
what, where = 'Statistics','Arlington, VA'
num_pages = 3

url = jobapp.IndeedSearch(what, where)
joblist = jobapp.Indeedjoblistpage(url)
urllist = joblist.geturls(num_pages)
```

```
unwanted = ['US citizen', "TS", "SCI", "DoD", "TOP SECRET", "Top secret"]
urlresult = jobapp.CheckWordsIn(unwanted,urllist)
urlresult
```
