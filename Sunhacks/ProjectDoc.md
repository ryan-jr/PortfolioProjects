# Project requirements doc

### User Stories

```
As a user I want ot be able to find my city/location
	- This will be done automatically upon coming onto the page(Get the code from the slack)

As a user I want to have the app play artists that will be near me(use the songkick API)
	- within a one month time period

As a user I want to be take to a ticket page if I like an artis and move on if I don't like an artist

```

### Tech stack

* Backend: Flask

* Frontend/processing: JS/jQuery

* UI/design: Use the stuff from the hackathon


### User flow diagram

1.  Landing page
	- The page shows something static to start out with
	- Upon recipt of geolocation coordinates transfer to a loading screen

2.  Loading/finding artists near user


	-------EVENTS API------
	- Make call to EVENTS API
	- Pull full list of artists from that city/nearest city

	-------Spotify API------
	- Search for each of those artists in the Spotify API
	- Get each of those artists spotify ID
	- Get a track list/a track(and their/its ID(s))
	- Use those track ID(s) to make a call to the preview API

3.  Play Music
	- Upon recepit from the preview API

4.  User interaction:
	- Like: Generate a link/selected information about the artist for tickets
	- Dislike: Move on to the next artist

	-Case(s) to deal with:
		A.  User goes trhough all artists near them
		B.  No artists near user
		C.  User listens to 30 second clip w/ no interaction, just move on?
			- How will we detect when the clip is done/over(have a timer?)



### Useful links/information


* Jquery API Calls:


```

https://stackoverflow.com/questions/9235237/jquery-how-to-use-multiple-ajax-calls-one-after-the-end-of-the-other

https://stackoverflow.com/questions/32564971/architecture-for-multiple-api-calls-using-jquery-and-javascript

```


* SeatGeek/Eventful API Docs:

```
Songkick makes you wait 7 days before granting an API key

http://platform.seatgeek.com/#events
http://api.eventful.com/docs/events/search(returns an XML)


XML Parsing:
https://stackoverflow.com/questions/25280911/how-to-read-xml-server-response-in-javascript

https://www.w3schools.com/xml/xml_parser.asp


```



* Spotify API Docs:

```

Overall API Docs: https://beta.developer.spotify.com/documentation/web-api/
API Code/examples: https://developer.spotify.com/web-api/code-examples/
SPotify Terminoligy and difference between URIs and IDs: https://developer.spotify.com/web-api/user-guide/#spotify-uris-and-ids


General Tracks API Endpoint Docs: https://beta.developer.spotify.com/console/tracks/
Artists Top Tracks: https://beta.developer.spotify.com/console/get-artist-top-tracks/?id=5l8lZmnKzCAUKKtNZMzbVO&country=US


Get Several Tracks: https://developer.spotify.com/web-api/get-several-tracks/
```




