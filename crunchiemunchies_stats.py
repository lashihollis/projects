calorie_stats = [70, 120, 70, 50, 110 , 110, 110, 130, 90, 90, 120, 110, 120, 110, 
                 110, 110, 100, 110, 110, 110, 100, 110, 100, 100, 110, 110, 100, 120,
                 120, 110, 100, 110, 100, 110, 120, 120, 110, 110, 110, 140, 110, 100, 
                 110, 100, 150, 150, 160, 100, 120, 140, 90, 130, 120, 100, 50, 50, 100, 
                 100, 120, 100, 90, 110, 110, 80, 90, 90, 110, 110, 90, 110, 140, 100, 110, 110, 100, 100, 110]

average_calories = np.mean(calorie_stats)
print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

median_calories = np.median(calorie_stats_sorted)
print(median_calories)

for p in range(1, 101):
    if np.percentile(calorie_stats_sorted, p) > 60:
        nth_percentile = np.percentile(calorie_stats_sorted, p)
        break
print(nth_percentile)

#percentage of values in data set that have more than 60 calories
more_calories = np.mean(calorie_stats > 60)
print(more_calories)


calorie_std = np.std(calorie_stats_sorted)
print(calorie_std)

#Based on the analysis, the average calorie count of the cereals in the dataset is approximately 107 calories, with a median of 110 calories, suggesting a fairly symmetrical distribution. Most cereals fall within the 100–120 calorie range, 
#and about 96% of them have more than 60 calories per serving. The standard deviation is relatively low, indicating that calorie counts don’t vary much across products. For Yummy Corp, this is an advantage when marketing CrunchieMunchies. 
#If CrunchieMunchies falls at or slightly below the average calorie count (while still being tasty), 
#Yummy Corp can promote it as a delicious, better-for-you option that aligns with what customers are already choosing — potentially even highlighting it as a smart pick for calorie-conscious consumers.
