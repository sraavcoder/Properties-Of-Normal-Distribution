import pandas as pd
import statistics
import csv
df = pd.read_csv(
    "C:/Users/sraav_1jk4baa/OneDrive/Desktop/WhitehatJr Python/Projects/Properties of ND/Data.csv")

ReadingScoreData = df["reading score"].to_list()

ReadingScore_Mean = statistics.mean(ReadingScoreData)
ReadingScore_Median = statistics.median(ReadingScoreData)
ReadingScore_Mode = statistics.mode(ReadingScoreData)

ReadingScore_SD = statistics.stdev(ReadingScoreData)

print("Mean of this Data is ", ReadingScore_Mean)
print("Median of this Data is ", ReadingScore_Median)
print("Mode of this Data is ", ReadingScore_Mode)
print("Standard Deviation of this Data is ", ReadingScore_SD)


ReadingScore_first_std_deviation_start, ReadingScore_first_std_deviation_end = ReadingScore_Mean - \
    ReadingScore_SD, ReadingScore_Mean+ReadingScore_SD
ReadingScore_second_std_deviation_start, ReadingScore_second_std_deviation_end = ReadingScore_Mean - \
    (2*ReadingScore_SD), ReadingScore_Mean+(2*ReadingScore_SD)
ReadingScore_third_std_deviation_start, ReadingScore_third_std_deviation_end = ReadingScore_Mean - \
    (3*ReadingScore_SD), ReadingScore_Mean+(3*ReadingScore_SD)

ReadingScoreData_of_data_within_1_std_deviation = [
    result for result in ReadingScoreData if result > ReadingScore_first_std_deviation_start and result < ReadingScore_first_std_deviation_end]
ReadingScoreData_of_data_within_2_std_deviation = [result for result in ReadingScoreData if result >
                                                   ReadingScore_second_std_deviation_start and result < ReadingScore_second_std_deviation_end]
ReadingScoreData_of_data_within_3_std_deviation = [
    result for result in ReadingScoreData if result > ReadingScore_third_std_deviation_start and result < ReadingScore_third_std_deviation_end]

print("{}% of data for weight lies within 1 standard deviation".format(
    len(ReadingScoreData_of_data_within_1_std_deviation)*100.0/len(ReadingScoreData)))
print("{}% of data for weight lies within 2 standard deviations".format(
    len(ReadingScoreData_of_data_within_2_std_deviation)*100.0/len(ReadingScoreData)))
print("{}% of data for weight lies within 3 standard deviations".format(
    len(ReadingScoreData_of_data_within_3_std_deviation)*100.0/len(ReadingScoreData)))
