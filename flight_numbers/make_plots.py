import seaborn as sns
import matplotlib.pyplot as plt


def make_pair_plot(df):

    pairplot = sns.pairplot(
        df[
            [
                "speed",
                "glide",
                "turn",
                "fade",
                "diameter_(cm)",
                "height_(cm)",
                "rim_depth_(cm)",
                "inside_rim_diameter_(cm)",
                "rim_thickness_(cm)",
            ]
        ]
    )

    return pairplot


def make_flight_number_hist(df, flight_number: str):

    plt.title(f"Distribution of discs by {flight_number.title()}", loc="left")

    sns.despine()

    return sns.countplot(df, x=flight_number)


def make_scatterplot(df, x, y):

    plt.title(f"{x.title()} vs. {y}", loc="left")

    sns.despine()

    return sns.regplot(data=df, x=x, y=y)


def make_stripplot(df, x, y):

    plt.title(f"{x.title()} vs. {y}", loc="left")

    sns.despine()

    return sns.regplot(data=df, x=x, y=y, x_jitter=True, y_jitter=True)


def make_correlation_matrix(df):

    corr_matrix = df.select_dtypes(include=["int64", "float64"]).corr()

    return corr_matrix.iloc[4:, :4].transform(lambda x: x * 100)


def make_correlation_plot(corr_matrix):

    plt.title("Flight Numbers and their Physical Characteristics", loc="left")

    sns.despine()

    return sns.heatmap(
        data=corr_matrix,
        annot=True,
        center=0,
        cmap="coolwarm",
    )
