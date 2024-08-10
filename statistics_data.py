import statistics

data = [142, 172, 146, 185, 163, 142, 147, 156, 176, 152]

def getStatistics(data_item):
    mean = statistics.mean(data_item)
    mode = statistics.mode(data_item)
    median = statistics.median(data_item)
    
    return {
        "mean": mean,
        "mode": mode,
        "median": median
    }
    
print(f"The mean is {getStatistics(data)["mean"]}")
print(f"The mode is {getStatistics(data)["mode"]}")
print(f"The median is {getStatistics(data)["median"]}")