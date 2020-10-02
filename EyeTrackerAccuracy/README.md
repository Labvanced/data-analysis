# Eye tracking accuracy calculation
The given data sets and analysis provide a data-driven conclusion about how accurate the Labvanced eye tracking technology is.
> In summary Labvanced eyetracking has a **spatial accuracy** of **1.4° horizontally** and **1.3° vertically** .
To direclty see this online click on the [iPythonNotebook/ipynb file](https://github.com/Labvanced/data-analysis/blob/master/EyeTrackerAccuracy/eyetracking_accuracy.ipynb)

## Where do the provided data sets come from?
All the data sets were recorded from our [spatial accuracy test study ](https://www.labvanced.com/page/library/12990)

## Was there any special/additional hardware or software involved when the data sets were recorded?
No, all data was recorded on different but normal laptops, and standard rgb webcams over the internet.

## How did the study look like for participants.
It was a relatively simple procedure. Each point was shown for 6 seconds while the subject was instructed to fixate it. 30 points were shown in total per subject, with a short break after each 10 points. Additionally before each trial 5 points were shown for re-calibration. 

## How many subjects were analzed?
The current data set includes data from 10 participants, more will follow.

## Was the data somehow filtered/preprocessed, did we remove 'outliers'?
We included all recorded gaze positions from all subjects from second 1 to second 6 (excluding the first second) to ensure that no large saccades towards the target where included in the data set. However, micro and correction saccades were probably still made from time to time (i.e. it might be hard to fixate one point for 5-6 seconds). So removing those outliers posthHoc yields further potential to improve the accuracy. 

## How was the analysis conducted, which calculation/method was used?
To determine how precise the Labvanced eyetracking is working we calcualted the 'spatial accuracy', which can be described as the average
distance in visual degrees between the 'true' gaze position and the predicted one. We did this for each gaze point and then averaged first 
all points for 1 participant, and in a second step accross participants. A reference paper describing this method [can be found here](https://www.researchgate.net/publication/254007815_Eye_tracker_data_quality_What_it_is_and_how_to_measure_it).

## How can I test the accuracy on my own / verify this?
- Clone the repository (git clone https://github.com/Labvanced/data-analysis.git)
- Install the dependencies (pip3 install -r requirements.txt) 
- Import the [spatial accuracy test study ](https://www.labvanced.com/page/library/12990) into your Labvacned account.
- Activate data recording and record data sets locally, or publish the study and acquire data sets online.
- Select the data sets in the data-view and download both "trial data" and "timeseries data".
- Make sure to rename the trial data  to "data.csv" and the timeseries data to "timeseries.csv", and replace those files in the repository
- Run the Jupyter notebook and see the results.


## Can I contact someone if I have further questions?
Sure, please contact us at contact@labvanced.com 


