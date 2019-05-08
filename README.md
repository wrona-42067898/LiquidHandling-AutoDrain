# LiquidHandling-AutoDrain
Relatively simple python script utilising pyautogui to automatically control mouse inputs to drain the reservoirs on our Mantis Liquid Handling Robot (FORMULATRIX). Coordinates are hard-coded as per the monitor's resolution.

![Simple commandline interface with 2 options](https://i.imgur.com/n66yG7x.png)

The user is prompted to enter the number of inputs (reservoirs) to drain, and the duration to drain for (in seconds [Above]. Inputs will be systematically drained one after another, with the user able to press ctrl+c at any time to abort. The Mantis UI is pictured below; the script simply tells the mouse to where move and click based on the required inputs and time specified by the user.

![Mantis UI](https://i.imgur.com/wBRYY9T.png)
