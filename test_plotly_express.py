'''
    Tests the plotly.express library with the iris -dataset.
    Contains bar plot, multiple scatter plots, density plot,
    pie plot and multiple figures generation.
    Runs all tests in this file. Opens the figures in an active window
    and saves the figures data to a file specified by the current date
    and the amount of tests done on the date.

    Testing functions take in the iris dataset -frame, and the figure target file.
    Functions do not return anything and currently the validation of the figures is done manually.
    Files can be compared with filecmp.cmp to see if the currently generated output file is the same as some previous one.

    Tested functions: data.iris(), bar(), scatter(), density_contour(), pie(), scatter_3D()
    Tested other features: color assignment by category, title generation, violin- and box deviation graphs,
    ols trendline generation, facet plots with facet_col argument
'''

import plotly.express as px
from datetime import datetime
import os.path as opath


# Creates a bar plot
def test_bar(iris, file):
    fig = px.bar(iris, x="sepal_width", y="petal_width", title="Bar plot", barmode="group")
    file.write("test_bar:\n")
    file.write(str(fig))
    file.write("\n")
    fig.show()


# Creates a scatter plot with different colors for different species
def test_scatter(iris, file):
    fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species", title="Scatter plot")
    file.write("test_scatter:\n")
    file.write(str(fig))
    file.write("\n")
    fig.show()


# Creates a scatter plot with trendline for different species sepal_length as a function of sepal_width
# with graphic deviation measures next to the scatter-trendline plot
def test_scatter_with_trendline_and_boxes(iris, file):
    fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
                     marginal_x="box", trendline="ols", title="Scatter plot with trendline and boxes")
    file.write("test_scatter_with_trendline_and_boxes:\n")
    file.write(str(fig))
    file.write("\n")
    fig.show()


# Creates a density plot for all species based on their sepal measures
def test_density_plot(iris, file):
    fig = px.density_contour(iris, x="sepal_length", y="sepal_width", color="species", title="Density plot")
    file.write("test_density_plot:\n")
    file.write(str(fig))
    file.write("\n")
    fig.show()


# Creates a pie chart with the sum of sepal lengths of species
def test_pie(iris, file):
    fig = px.pie(
        iris, values="sepal_length", names="species", title="Pie Chart",
    )
    file.write("test_pie:\n")
    file.write(str(fig))
    file.write("\n")
    fig.show()


# creates a 3D scatter plot
def test_3D_plot(iris, file):
    fig = px.scatter_3d(iris, x='sepal_length', y='sepal_width', z='petal_width', color='species', title="3D plot")
    file.write("test_3D_plot:\n")
    file.write(str(fig))
    file.write("\n")
    fig.show()


# Creates a graph for each species with a scatter and trendline
def test_multiple_charts(iris, file):
    fig = px.scatter(
        iris,
        x="sepal_width",
        y="sepal_length",
        color="species",
        facet_col="species",
        trendline="ols",
        title="Multiple charts")
    file.write("test_multiple_charts:\n")
    file.write(str(fig))
    file.write("\n")
    fig.show()


# returns file name to be tested
def gen_file_name(time_str, num):
    return ("run_tests_" + time_str + "_" + str(num) + ".txt")


def run_tests():
    iris = px.data.iris()
    time_now = datetime.now()
    time_str = time_now.strftime("%d%b%Y")
    num = 0
    filename = gen_file_name(time_str, num)

    # Tests filenames for as long as an unused name is found.
    while opath.exists(filename):
        num += 1
        filename = gen_file_name(time_str, num)

    file = open(filename, "w")

    test_bar(iris, file)
    test_scatter(iris, file)
    test_scatter_with_trendline_and_boxes(iris, file)
    test_density_plot(iris, file)
    test_pie(iris, file)
    test_3D_plot(iris, file)
    test_multiple_charts(iris, file)

    file.close()


if __name__ == "__main__":
    run_tests()

