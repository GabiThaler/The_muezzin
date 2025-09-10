# the muezzin


Our program is a program for saving and processing data on audio files.

## the first stage - processing_metadata


We receive the file cache, go through it one by one and get all the data on it,
such as when the weight was created, etc. and send it to the next stage.

## In The second stage - transcriber

We transcribe all files and enter each transcription into the metadata dictionary and send it to the next stage.

## In the third stage - BDS_calculator

We calculate the level of risk for each audio file.

### Explanation of calculating the risk level

We did the calculation by adding a point to each word on the dangerous list and two points to each word on the very dangerous list.
Finally, we divide the number of words in the conversation by the number of dangerous words there are. Then, the lower the final number,
the more dangerous the conversation. So with a final score of more than ten, it is not dangerous, and if it is between five and ten, it is dangerous, and below five, it is very dangerous.

## Fourth and final stage - Data_storaging

At this stage, we store all the information for the metadata information. We add a unique identifier by encrypting the path on the computer + the name of the file and enter it into a dictionary. 
Then we store the dictionary in Elasticsearch and divide the file into parts and store it in the binary method in mongoDB.



### remark

Of course, we documented the entire program with logs in three stages. 
1.INFO
2.DEBUG
3.ERROR
Currently in the program, comments are only at the level "info" You can always change the definition in the file loger_manager



### A brief explanation of the architecture structure

I was really debating whether to enter the information into databases at each stage or have a flow of data and only end up entering elastic and mongo
But I decided that I would start by streaming directly through Kafka at each stage and only end up entering elastic and mongo. 
And if there is time, we would change it, but there was no time...


Some of the considerations are that it is not good to put the information in and out of the caches because it is not the most secure and time-consuming

On the other hand, each step would not depend on the second step if we did it in a way that puts each step into elastic and mongo



##Start the program
pip install commands.bat
pip install requirements.txt
And in each folder there is a main file that needs to be run