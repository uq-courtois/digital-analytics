# You can add this code in between defining your plot
# And saving it...

# Gets rid of scientific notation
plt.ticklabel_format(style='plain')
# Rotates labels vertically
plt.xticks(rotation='vertical')
# Forces tidy plot lay-out
plt.tight_layout()
