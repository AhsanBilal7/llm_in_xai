import pandas as pd


data = pd.read_csv("./dataset/dataset/survey/FlourishingScale.csv")
pre_data = data[data["type"] == "pre"]
post_data = data[data["type"] == "post"]

head_data = data.head()
print("Total number of pre susrvey entries: ",len(pre_data))
print("Total number of post susrvey entries: ",len(post_data))



# working_data = data.drop(columns=["type", "uid"])
working_data = data
# Display the column names
print("Columns in the dataset:")
print(working_data.columns.tolist())

# Calculate and print the total number of entries in each column
print("\nTotal number of entries in each column:")
final_array = []
for column in working_data.columns:
    output_data  = {}
    if True or column not in ["type", "uid"]:
        total_entries = working_data[column].count()  # Counting non-null entries in the column
        print(f"********** Processing column {column} **********")
        unique_entries = working_data[column].unique()  # Counting the number of unique entries
        # print(unique_entries)
        description = data[column].describe()
        print(f"Total Entries: {total_entries} entries")
        print(description)
        output_data["Metric"] = column
        # Extract and display values dynamically
        entries = description.index.tolist()
        values = description.values.tolist()

        # Create a dictionary to map entries to their values
        result = dict(zip(entries, values))
        print("================")
        print(result)
        print("================")
        for entry in result.items():
            output_data[entry[0]] = entry[1]

        final_array.append(output_data)

final_array_data_frame = pd.DataFrame(final_array)
# final_array_data_frame = final_array_data_frame.dropna(axis=1, how = 'any')
final_array_data_frame.to_csv('side_by_side_statistics_FlourishingScale.csv', index=False)
print("========== Final Output ==============")
print(final_array_data_frame)
print("==========  ==============")
# Additional check: total rows in the working_dataset
# total_rows = working_data.shape[0]
# print(f"\nTotal number of rows in the working_dataset: {total_rows}")