# Polling Input vs Events

* Events are "Some thing happening"
  * User typing a key (reexplain input)
  * Timer waiting out (reexplain sleep)
  * Responding to a network request (explain network requests)
  * Something happening is external to our programt that we want to respond to.
* Event systems call a function
  * Register a function with the event system
  * Different event systems for different types of events
  * UI Events
  * Network Events

## Web Frameworks
* URLs as event targets
* Web server as event dispatcher
* Respond with HTML for a file
* Moustache templating

### Exercises:
* Web Server for President's Database (Read only, links to next/last president)
* Web Server for Rug Shop, has a form to select rug details.

## UI Frameworks
* Provide common UI elements (panel, text, button, input)
* Handle the "event loop"
* Your code just responds to registered clicks
* Python, C: tkinter for UI framework
* Typescript: Angular for UI framework

### Exercises:
* UI for President's Database
* UI for Rug Shop
