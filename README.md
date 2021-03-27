# Capstone_Pneumonia
1 Introduction:
Pneumonia accounts for over 15% of all deaths of children under 5 years old
internationally. In 2015, 920,000 children under the age of 5 died from the disease. In the
United States, pneumonia accounts for over 500,000 visits to emergency departments [1]
and over 50,000 deaths in 2015 [2], keeping the ailment on the list of top 10 causes of
death in the country.


2.How existing system works:
Pneumonia is an infection of the lungs with a range of possible causes. It can be a serious
and life-threatening disease. It normally starts with a bacterial, viral, or fungal infection. The
lungs become inflamed, and the tiny air sacs, or alveoli, inside the lungs fill up with fluid.
Pneumonia can occur in young and healthy people, but it is most dangerous for older
adults, infants, people with other diseases, and those with impaired immune system.

2.1. Pneumonia identification through X-rays
In the process of taking the image, an X-ray passes through the body and reaches a
detector on the other side. Tissues with sparse material, such as lungs which are full of air,
do not absorb the X-rays and appear black in the image. Dense tissues such as bones
absorb X-rays and appear white in the image.

3. Problem Statement
Challenge is to build an algorithm to detect a visual signal for pneumonia in medical
images. Specifically, build an algorithm which needs to automatically locate lung opacities
on chest radiographs. Lung opacities are vague, fuzzy clouds of white in the darkness of the
lungs.

4.Expected Outcome :
Prediction was held on whether pneumonia exists in a given image by predicting bounding
boxes around areas of the lung. Samples without bounding boxes are negative and contain
no definitive evidence of pneumonia. Samples with bounding boxes indicate evidence of
pneumonia.
When making predictions, competitors should predict as many bounding boxes as they feel
are necessary, in the format: confidence x-min y-min width height
There should be only ONE predicted row per image. This row may include multiple
bounding boxes.
A properly formatted row may look like any of the following.
For patientIds with no predicted pneumonia / bounding boxes: 0004cfab-14fd-4e49-80ba-
63a80b6bddd6,
For patientIds with a single predicted bounding box: 0004cfab-14fd-4e49-80ba-
63a80b6bddd6,0.5 0 0 100 100
For patientIds with multiple predicted bounding boxes: 0004cfab-14fd-4e49-80ba-
63a80b6bddd6,0.5 0 0 100 100 0.5 0 0 100 100, etc.
