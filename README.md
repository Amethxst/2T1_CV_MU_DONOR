# 2T1 CV MU DONOR
CV script for the DONOR (6MLN LOOP) version of Master Unlocker (2T1).

MU offers a PREMIUM version for its LOOP 6MLN (w/Special Cargo). This script facilitates the execution of the 6MLN loop by enabling restock after the warehouse runs out of stock.  

# IMPORTANT INFO
This is a CV (Computer Vision) script, meaning that the script will always have to 'use' screen and keyboard. You can't run the script in background, but useful for staying literally AFK.  

This script is based on these settings:
- 1920x1080 screen size
- GTAV languages = ENG
- Extreme version of loop
- Use of numpad
 
In case you play at different resolution/language/method, you will have to download the source code and modify it.
- Redo the img's as you find them in the folder you download (use my UI file and name the img's 1.png / 2.png).
- For normal loop:
  - Download Source code, "macro1" and remove one set of "num8" (line 67/70)
  - Download Source code, "macro2" and add one set of "num8" (line 94/97) & "num2" (line 121/124)
- If you do not have the numpad, you must also edit the keys.py file by looking online for direct keyboard inputs (remember, **direct inputs**). ChatGPT is your friend.
- If it fails to restock in time, edit line 109 by increasing the time.  
# TUTORIAL
To run the script correctly, follow these steps:  

1. Add the path to the images to the .json file.
    - 1.png = 6MLN SCREEN
    - 2.png = Warehouse empty.  
    (use // for paths)

2. Download my 2T1 UI settings and load it:
    - Only things changed:
      - Settings -> Menu UI -> Menu Colors -> 'Background Alpha' (255)
      - Settings -> Menu UI -> Menu Colors -> 'Selected BG Alpha' (255)
3. Enable MU
4. Selected the warehouse and do restock
    - As soon as it's done, disable it
5. Position to "Special Cargo"
    - Local -> Script Features -> MU -> VIP/CEO/MC -> Special Cargo (**MUST REMAIN SELECTED**)
6. Start script  
(A console pops up with a text in Italian that means "Image not found. Try again in 5 seconds." Every 5s the script will search for one of the two images, which is the time to enter the game)
8. Enter in "Special Cargo" section  
The script will do the rest :)
