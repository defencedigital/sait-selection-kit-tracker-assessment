# Challenge 2. Kit Tracker

Challenge Outline. There are dozens of sensors, cameras, beacons and other pieces
of technology deployed in theatres around the world and this
is only increasing. 

You are required to create a software solution
to this problem. The tech lead has the following user requirements for the
solution:

- Must allow the user to easily create, read, update and delete equipment
entries (ideally using a GUI)

- Must include all of the equipment data in the provided kit spreadsheet.
- Must pull device data from the provided API to get updates with relevant
sensor information such as:
o Current GPS location
o Battery status
o Most recent image captured

- Should have the entries overlayed on an interactive map which updates as
new requests hit the API
- Should update the database of equipment as requests hit the API.
- Should allow user to interact with the equipment entry through the GUI.
- Should actively monitor the status of networked OpTech (using pings, routine
API calls etc) and provide an appropriate alert when connectivity is lost.
- Should provide a more urgent notification when the tamper status changes.
- Could allow easy viewing of live feeds (embedded) within your solution from
cameras which are currently streaming.

- If you are ready for viewing of a live feed within your solution, we have a live feed
camera streaming RTSP which you can use and this will
simulate a device feed, just ask when you are ready.

Instructions for participants of challenge

API and Credentials to be given in person

See example_api_get.py for an example of how to GET data from the api

See sample_data for example data
