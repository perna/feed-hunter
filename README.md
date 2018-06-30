# Feed Hunter
> Feed Hunter is an CLI tool to crawl itunes feeds

---

### Running on docker:
 #### 1. Installing
  ```
   $ git clone git@github.com:perna/feed_hunter.git
  ```

 #### 2. Build image for running scrapy
  ```
   $ docker build -t feed_hunter/scrapy:0.1 .
  ```

 #### 3. Create the container, mapping your local project into the container
  ````
    $ docker run -it -v /Users/JohnDoe/Code/feed-hunter:/home feed_hunter/scrapy:0.1 /bin/bash
  ````

 #### 4. Install requirements
  ````
   $ pip install -r requirements.txt
  ````

 #### 5. Now just let go of the spiders 
  ````
   $ scrapy crawl itunes
  ````
