# Skating Overlay

This is a single HTML file, intended for use in a "Browser" source of an OBS Studio stream. It will fetch information at a configurable period from a specified URL via HTTP GET requests, then this will be displayed. The final race results window will pop up if either the race ID changes or on the rising edge of the `all_finished` property.

## HTML Configuration

The top of the HTML file contains some values for configuration. The following is a summary of all configuration
fields:

`colors_url`: A string determining to which URL the HTTP GET request for the JSON colours document will be made.

`current_race_url`: A string determining to which URL the HTTP GET request for the JSON current race document will be made.

`pollingPeriodMilliseconds`: An integer representing after how long, in milliseconds, the overlay will fetch the JSON
document from the server.

`popupActiveMilliseconds`: An integer representing for how long, in milliseconds, the results popup will be visible.

`alignRight`: A boolean value. If true, the skaters' names will be aligned with the right edge of the screen, otherwise
they will be aligned with the left edge.

`alignTop`: A boolean value. If true, the skaters' names will be aligned with the top edge of the screen, otherwise they
will be aligned with the bottom edge.

## CORS

Cross-origin requests are necessary in order for the functionality of this overlay, because this client would request
the JSON file from the server which is at a separate origin. Thus, it is necessary that the server response includes the
correct CORS headers, or the request will fail. The Python server file in this repository provides an example for the
headers. In my experience, it is better to run a local web server then point the OBS Browser source to `localhost` rather than 
use the "Local File" option in OBS Studio. More information relating to CORS can be
found [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS).
