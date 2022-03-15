import datetime

# the individual graph plts are stored in this folder
graphFolder = "graphs"

# at what time did the recording of the video file start?
videoCreationDatetime = datetime.datetime(year=2022, month=3, day=15, hour=12, minute=59, second=44)

# evaluate a video frame every <samplingIntervalInSeconds>
samplingIntervalInSeconds = 1

#  graph title
graphTitle = "Evolution of Twitter Space listeners"

# where does the time range start on the graphs?
graphStartTime = "13:00:00"

# where does the time range stop on the graphs?
graphEndTime = "14:00:00"

# what is the minimum number of listeners displayed in the graphs?
graphMinimumNumberOfListeners = 0

# what is the maximum number of listeners displayed in the graphs?
graphMaximumNumberOfListeners = 600
