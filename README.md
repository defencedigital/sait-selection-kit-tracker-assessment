# sait-selection-kit-tracker-assessment

The challenge is to create an 'Op Tech kit tracker'. It should show the location and status of various pieces of simulated optech kit on a nice GUI.

The kit will be simulated via two scripts- rx.py and tx.py. They will both push kit status data to challenge participants IP's and provide an API interface to be queried ad-hoc by any particpant on the LAN. Kit status data is stored within a default and current state .json, which can be loaded by either program upon request transmit/ recieve.

API:  kit-tracker.peacemosquitto.workers.dev

Credentials to be given in person
