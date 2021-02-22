# Gov API

About: This was a quick little learning experiment on collecting all data on the US Governors, and then building an API to serve it using Django. <br />


Retrieving the data: search.py utilized Selenium, BeautifulSoup, and Requests to completely scrape the https://www.nga.org/governors/ website and parse the data that I was looking for. 
Once everything was obtained I appended all data to a Pandas dataframe which was then exported as a .csv. <br />

Building the API: For building the API I used Django as I had experimented with making a web application with it before. 
It was a pretty straight-forward process of hosting it just temporarily on my computer and then accessing it via a browser through localhost:8000. 
The only thing that caused me some issues was implementing the import resource onto the Django Admin page, 
but after much debugging I resolved it by adjusting my return statement on the model I had created. <br />

Final Thoughts & Future Add Ons: Overall I think that this was a good project to continue to learn about the Django web framework, 
and get my hands dirty with building an API to work with GET / POST / etc. 
In the future I would like to adjust the API, so users are unable to POST to the database and they can only GET data. 
I think it would also be cool to actually make it available to the public and find a more permenant hosting solution via: my own homeserver or something like Heroku and Rapid API. <br />

Screenshots: I've added screenshots of the API in action below.... <br />

![ScreenShot](govapi-screenshot-1.png)
![ScreenShot](govapi-screenshot-2.png)
![ScreenShot](govapi-screenshot-3.png)
![ScreenShot](govapi-screenshot-4.png)
![ScreenShot](govapi-screenshot-5.png)
![ScreenShot](govapi-screenshot-6.png)
