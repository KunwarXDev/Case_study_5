import pandas as pd
import matplotlib.pyplot as plt
file_path = 'Case_Studt_5_B.xlsx' 
df = pd.read_excel(file_path)


df['Percentage'] = df['Percentage'].astype(float)


more_than_75 = df[df['Percentage'] > 75]
between_60_and_75 = df[(df['Percentage'] >= 60) & (df['Percentage'] <= 75)]
less_than_60 = df[df['Percentage'] < 60]


print("🟢 Students with more than 75%:")
print(more_than_75, end="\n\n")

print("🟡 Students with 60% to 75%:")
print(between_60_and_75, end="\n\n")

print("🔴 Students with less than 60%:")
print(less_than_60, end="\n\n")


plt.figure(figsize=(10, 6))
plt.bar(more_than_75['Percentage'], more_than_75['Name'], width=4, color='blue', edgecolor='black', label='>75%')
plt.bar(between_60_and_75['Percentage'], between_60_and_75['Name'], width=4, color='blue', edgecolor='black', label='60%-75%')
plt.bar(less_than_60['Percentage'], less_than_60['Name'], width=4, color='blue', edgecolor='black', label='<60%')

plt.xlabel("Percentage")
plt.ylabel("Name of Student")
plt.title("Histogram")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
plt.scatter(more_than_75['Name'], more_than_75['Percentage'], color='green', label='>75%')
plt.scatter(between_60_and_75['Name'], between_60_and_75['Percentage'], color='orange', label='60%-75%')
plt.scatter(less_than_60['Name'], less_than_60['Percentage'], color='red', label='<60%')

plt.xlabel("Name of Student")
plt.ylabel("Percentage")
plt.title("Scatter plot")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()
