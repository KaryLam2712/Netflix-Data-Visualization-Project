import matplotlib.pyplot as plt

# Data for the bars
movies = 70
tv_shows = 30

# Creating the stacked bar chart
fig, ax = plt.subplots()
bar_width = 0.5

# Plot bars
ax.barh("Movies", movies, bar_width, label='Movies', color='blue')
ax.barh("TV Shows", tv_shows, bar_width, left=movies, label='TV Shows', color='green')

# Adding labels, title, and legend
ax.set_xlabel('Percentage')
ax.set_ylabel('Type')
ax.set_title('Distribution of Movies and TV Shows')
ax.legend()

plt.show()

# country = netflix['country'].explode()
# country_counts = country.value_counts().head(20)
# count_values = [str(count) for count in country_counts]
# fig = px.funnel(x=country_counts, y=country_counts.index, text= country_counts, labels={'x': 'Number of Content'})
# fig.update_traces(marker_color = '#b20710')
# fig.show()