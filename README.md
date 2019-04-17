# roi_annotation.py
Tool for annotating regions of interest (ROI's) in prostate cancer biopsy images, each ROI can be rated with a gleason score from 1-5. Pressing a numbered button will rate the currently displayed ROI with that number. The ">" button displays the next image to be rated, and the "<" button returns to the previous image. The left and right arrowkeys and numbers on the keyboard can be used to traverse and rate the images. The users' is saved to a csv.

# to start:
1. The root directory should be called "roi_annotation", inside this directory place roi_annotation.py and another directory called "public". Inside the public directory place 3 more directories: "images","js",and "css". Place images to be rated in the images directory, "style.css" in the css directory, and "keys.js" in the js directory.

2. In a terminal, from the roi_annotation directory run the command: "python roi_annotation.py"
   if successful, the output should look like:
   
   -ENGINE Listening for SIGTERM.
   
   -ENGINE Bus STARTING
   
   -ENGINE Set handler for console events.
   
   -ENGINE Started monitor thread 'Autoreloader'.
   
   -ENGINE Serving on http://127.0.0.1
   
   -ENGINE Bus STARTED
  
   and the application should be running on http://127.0.0.1
   
- Images in the "images" directory will be displayed in random order to be graded

- The users' ratings will be saved to a csv in the roi_annotation directory
