% Payload Manual
% Arcola Energy
%

# Payload Manual

## Pre-flight check

* Check that the system starts up as expected (see Startup section below)
* Ensure the photos have been removed from the SD card.
* Check the Pi -> projector works
* Fill a balloon for fuel cell demo and to start the Pi

## Hydrogen Filling

Fill the small balloon with enough hydrogen to blow it up fully. Low pressure results in unreliable performance.

## Startup

\ ![Payload top](payload_top.png)

\ ![Payload front](payload_front.png)

* Attach the fuel cell's wires, ensure positive and negative are correct.
* Attach the fuel cell's purge outlet to the silicone tube.
* Attach the fuel cell to the chassis with an elastic band.
* Connect the balloon to the fuel cell inlet.
* Check the Raspberry Pi switch is off.
* Unclip the gas clip.
* Press the purge valve momentarily.
* At this point you should see the red fuel cell status LED begin flashing once per second. If not then try:
    * check the gas clip,
    * try another purge,
    * replace the fuel cell.
* Wait until the status LED starts flashing once per 2 seconds.
* Turn on the Raspberry Pi with the power switch.
* The blue front panel status LED should turn on and start flickering, followed by the Pi's yellow ACT LED.
* After the Pi has booted, the blue LED will flash rapidly 3 times and turn off. This means the Pi has started successfully and will now load the camera software. While the Pi is running its yellow ACT LED should flash in a heartbeat pattern.
* After a few seconds, the blue LED will come on, followed by the red camera LED. Then both will switch off. This indicates a photo has been taken.

## Shutdown

* Press the reset button. The blue LED should flash rapidly 3 times. Wait until the blue status LED and the Pi's ACT LED are off.
* Turn off the Pi's power switch
* Disconnect the balloon and empty it.
* Remove the fuel cell and place in its air tight bag.

## Copying and Removing Photos

Photos should be copied for safe keeping and given to the teacher.

The photos need to be removed from the SD card as there is only space for about 30 minutes worth of material.

\ ![Removing Photos](remove_photos_labels.png)

* Connect a screen to the Pi and start up. 
* Connect USB hub to Pi with mouse and USB attached.
* Power up the Pi.
* Scratch will start automatically, close this down.
* Start the file browser (see image).
* Navigate to /home/pi/photos
* Select all the photos, press the right mouse button and select `copy`.
* Navigate to the USB stick and right click `paste`
* Wait for the copy to end, then eject and remove USB key.
* Navigate back to /home/pi/photos
* Select all photos, right click `delete` to remove.
* Use the shutdown button (see image) to shut the Pi down.

## Problems

### The Pi starts up, the heartbeat is flashing on the ACT LED, but no photos are taken.

This is probably because the SD card is out of space. Delete the photos from the /home/pi/photos directory and try again.
