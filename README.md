# Galdêncio

A web scraper to get the latest memes posted on [AhNegão](https://ahnegao.com.br). It may sound silly, but they have the best memes.

Right now, it only works with videos.

Galdêncio returns the youtube link to the posted videos, so you can then use for whatever purpose you want. The reason I did this is because Joe (AhNegão's owner) posts the videos on his channel as unlisted videos, so you can't just subscribe to his channel.

Make sure to give the blog a visit, if you like good memes. Btw, Galdêncio is one of the unusual names that Joe gives to the dogs from the memes he post.

### How to use

You can simply run main.py and it will return the latest videos posted on the blog. It will then add the videos unique ID to a list, to make sure you won't get reposts.

If you want more than the first page, you can add the -p option and specify the pages ex `-p 1 2 3` to get the first 3 pages (I'll try and implement a system so you can actually just pass something like 1-3)

You can clear the cache with the `-c` option. And you can enable what I call the sentry mode with `-s`, which just keeps making requests and returns if something new is posted. You can specify how long would you like to wait till a second scan in seconds like `-s 60` for a minute. Default is 1 hour.
