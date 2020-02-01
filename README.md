# Tools and Utils used for Machine Learning 

Various tools used in my adventures in ML. 

## partition.py

Partition image datasets into training, validation, and test for maximum ML

### TODO 
 * Make it do its thing 
   * Default will be 33%/33%/33% for T/V/T (*T*raining/*V*alidation/*T*est) or something
 * Parse a argument like: 70/15/15
 * Parse wild cards like: 70/\*/\*
   * This would parse it as: 70/15/15
 * Add a .partignore or something to ignore some files (.DS_Store, I'm looking at you)

## grabber.py

Download images from ImageNET list of URLs

### TODO
  * Add example to this README
  * Refactor the actual code
    * add main
    * move argparse setup to its own function 
    * crop / scale / nothing needs to be refactored 
  * This should run in parallel 
  * Add sweet TUI with progress bar like: 
    * [==== 34%      ] Downloading file.jpg... 
