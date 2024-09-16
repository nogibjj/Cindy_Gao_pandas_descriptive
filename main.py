import matplotlib.pyplot as plt
import pandas as pd

data = "https://raw.githubusercontent.com/anlane611/datasets/main/population.csv"


# read dataset from csv file
def load_dataset(dataset):
    df = pd.read_csv(dataset)
    return df


# calculate the mean of variable:
def get_mean(df, col):
    mean_col = df[col].mean()
    return mean_col


# calculate the median of variable:
def get_median(df, col):
    median_col = df[col].median()
    return median_col


# calculate the standard deviation of variable:
def get_std(df, col):
    std_col = df[col].std()
    return std_col


# data visualization: boxplot for variable Y
def create_boxplot(script, filename="Boxplot.png"):
    plt.boxplot(script)
    plt.xlabel("variable_Y")
    plt.ylabel("values")
    plt.title("Visualization for Boxplot of variable_Y")
    plt.savefig(filename)
    plt.show()


# create the summary markdown
def save_to_md(mean_y, median_y, std_y):
    with open("boxplot.md", "a", encoding="utf-8") as file:  # Specify encoding
        file.write("# Markdown for the boxplot of variable Y\n")
        file.write("![Figure](boxplot.png)\n")
        file.write(f"\n**Mean**: {mean_y}\n")
        file.write(f"**Median**: {median_y}\n")
        file.write(f"**Standard Deviation**: {std_y}\n")
