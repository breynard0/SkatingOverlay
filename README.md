# Skating Overlay

This is a single HTML file, intended for use in a "Browser" source of an OBS Studio stream. It will fetch information at
a configurable period from a specified URL via HTTP GET request, then this will be displayed. The request should return
a JSON string that follows the specified format, and an example can be found in this repository's `sample.json`. The
same JSON document can be returned multiple times, and the overlay will only update when the document is different from
the current one saved. The results will pop up as soon as a new race ID is detected.

## Video Demo
![](SkaterOverlayShowcase.mp4)

## JSON Format

`currentRaceCode` (String): This represents the alphanumeric code for the current race, such as `36A`.

`currentRaceName` (String): This represents the name shown in the current race's titlebar.

`currentRaceId` (Integer): This is a unique integer identifying this race. There are no restrictions on what this number
can be, other that it must be different for every race and it cannot be equal to `-1`. It does not have to list them
sequentially, it can be random digits so long as they are unique.

`currentRaceSkaters` (Array): An array listing all skaters in the current race. They will be displayed and numbered in
the same order as they are passed in through this array, with the zeroth array element being mapped to the first skater.
This ordering may be used for either lane number or place number. The format for each array element is as
follows:

- `skaterName` (String): A string that contains the name of the skater.
- `skaterClub` (String): A string that contains an identifier to the skater's club. This will not be show directly,
  rather it will be matched with the configuration in the HTML to colour the skater's box.
- `skaterMostRecentLap` (Float, String): A floating point number or string that represents the most recent skater lap
  time to be shown. This is permitted to be `null` if no such time is available. A string may be better since a float
  would lose trailing zeros (e.g. 12.50 → 12.5).

`pastRaceCode`, `pastRaceName`, `pastRaceId`, `pastRaceSkaters`: These fields are identical to their `currentRace`
counterparts, and they will be used in the popup summary of race results. Here are a few notes:

- `skaterMostRecentLap` should probably be used for a skater's final time.
- `pastRaceId` must also be unique

## HTML Configuration

The top of the HTML file contains some values for configuration. The following is a summary of all configuration
fields:

`url`: A string determinining to which URL the HTTP GET request for the JSON document will be made.

`pollingPeriodMilliseconds`: An integer representing after how long, in milliseconds, the overlay will fetch the JSON
document from the server.

`popupActiveMilliseconds`: An integer representing for how long, in milliseconds, the results popup will be visible.

`alignRight`: A boolean value. If true, the skaters' names will be aligned with the right edge of the screen, otherwise
they will be aligned with the left edge.

`alignTop`: A boolean value. If true, the skaters' names will be aligned with the top edge of the screen, otherwise they
will be aligned with the bottom edge.

`skaterColours`: An array of two-value subarrays determining which colour will be linked with a given club code. For
each of the subarrays within this large array, the first element is a string that will be matched by the JSON's
`skaterClub` value, while the second one is a string hex value of the colour to display.

## CORS

Cross-origin requests are necessary in order for the functionality of this overlay, because this client would request
the JSON file from the server which is at a separate origin. Thus, it is necessary that the server response includes the
correct CORS headers, or the request will fail. The Python server file in this repository provides an example for the
headers. More information relating to CORS can be
found [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS).