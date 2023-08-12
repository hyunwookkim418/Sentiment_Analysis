import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

f = [f.name for f in fm.fontManager.ttflist]
print(f)

plt.rc('font', family='Malgun Gothic')

# Sample data
group1_positive = [164, 352, 305, 248, 186, 132, 339, 380, 251, 179, 240, 177, 233, 168, 134, 194, 225, 114, 276, 132, 276, 529, 888, 611, 553, 590, 518, 1244, 171, 382, 270, 443, 330, 1229]
group2_positive = [206, 328, 267, 209, 231, 165, 190, 386, 570, 465, 327, 206, 234, 218, 367, 342, 108, 270, 223, 252, 220, 248, 255, 264, 249, 311, 194, 427, 418, 293, 554, 296, 321, 0]
group1_negative = [199, 231, 246, 140, 140, 123, 201, 194, 192, 91, 136, 95, 188, 153, 112, 84, 171, 80, 117, 145, 123, 629, 879, 559, 680, 501, 382, 1391, 218, 447, 287, 393, 229, 957]
group2_negative = [184, 257, 222, 236, 282, 144, 146, 279, 627, 411, 279, 200, 270, 269, 409, 249, 106, 282, 192, 193, 181, 183, 258, 252, 251, 224, 268, 413, 400, 237, 472, 245, 276, 0]

# Combine the data
all_data = [group1_positive, group2_positive, group1_negative, group2_negative]

# Create a colorful and styled box plot
fig, ax = plt.subplots(figsize=(8, 6))
bp = ax.boxplot(all_data, labels=['긍정(1세대)', '긍정(2세대)', '부정(1세대)', '부정(2세대)'], 
                showfliers=False, patch_artist=True)

#['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon']
# Set box colors
box_colors = ['blue', 'grey', 'blue', 'grey']
for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)

# Add grid lines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Set the title and labels
#ax.set_xlabel('그룹')
ax.set_ylabel('감성 어휘 수')

# Show the plot
plt.savefig('box_plot.jpg', format='jpeg')

plt.tight_layout()
plt.show()
