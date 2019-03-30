# gleason
Tool for annotating regions of interest (ROI's) in prostate cancer biopsies, each ROI can be rated with a gleason score from 1-5. Pressing a numbered button will rate the currently displayed ROI with that number. The "<-back" button erases the score of the last seen image and displays the image again to be re-rated. The "save" button writes all the scored images to a csv called "Scores.csv", which holds (image filename, gleason rating) pairs. The scores will also automatically be written to the file after the user has rated all picures in the "./images" directory.

# to start:
1. Make sure roi_annotation.py is is in the same directory as the "./images" directory (not inside the "./images" directory!)
2. In a terminal, in the directory of roi_annotation.py run the command: "python roi_annotation.py"
   if successful, the output should look like:
      [30/Mar/2019:18:45:27] ENGINE Listening for SIGTERM.
      [30/Mar/2019:18:45:27] ENGINE Bus STARTING
      [30/Mar/2019:18:45:27] ENGINE Set handler for console events.
      [30/Mar/2019:18:45:27] ENGINE Started monitor thread 'Autoreloader'.
      [30/Mar/2019:18:45:27] ENGINE Serving on http://127.0.0.1
      [30/Mar/2019:18:45:27] ENGINE Bus STARTED
   and the application should be running on http://127.0.0.1
- Images in the "./images" directory will be displayed in random order to be graded until all have been graded and the webpage displays "No more images"
- The "scores.csv" file will be created in the same directory as the roi_annotation.py file
