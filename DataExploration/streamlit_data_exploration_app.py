import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Housing_Price_Data.csv')

# Introduction Section
st.title('Housing Price Data Exploration App')
st.header('Introduction')
st.write('This app explores a dataset of housing prices. The dataset contains details about houses including price, area, bedrooms, bathrooms, stories, and various other features.')

# Show dataset overview
st.subheader('Dataset Overview')
st.write(df.head())  # Display first few rows of the dataset

# Visualization Section with Interactive Options
st.header('Visualizations')

# Interactive Dropdown to select numerical columns for histograms
st.subheader('Select a variable for the histogram')
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
selected_column = st.selectbox('Choose a column', numerical_columns)

# Histogram section
if selected_column:
    st.subheader(f'Distribution of {selected_column}')
    fig, ax = plt.subplots()
    ax.hist(df[selected_column], bins=20, color='skyblue', edgecolor='black')
    ax.set_title(f'Distribution of {selected_column}')
    ax.set_xlabel(selected_column)
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    # Display statistics for the selected column
    mean_value = df[selected_column].mean()
    median_value = df[selected_column].median()
    mode_value = df[selected_column].mode()[0]
    std_value = df[selected_column].std()

    st.write(f"**Statistics for {selected_column}:**")
    st.write(f"Mean: {mean_value}")
    st.write(f"Median: {median_value}")
    st.write(f"Mode: {mode_value}")
    st.write(f"Standard Deviation: {std_value}")

    # Provide dynamic descriptions based on the selected variable
    if selected_column == 'price':
        st.write("""
        **Description**: Price represents the cost of houses in the dataset. It is one of the most important variables in this dataset, and its distribution is essential to understand how prices are spread. A skewed distribution could indicate a few high-value or low-value properties influencing the overall trend.
        """)
    elif selected_column == 'area':
        st.write("""
        **Description**: Area refers to the size of the houses, usually measured in square feet. Larger areas generally correlate with higher prices, though other factors like location and house features also play significant roles. Understanding the distribution of area helps identify the most common house sizes.
        """)
    elif selected_column == 'bedrooms':
        st.write("""
        **Description**: The number of bedrooms is a categorical variable, and it helps in segmenting the types of houses based on their capacity. Most houses tend to have 2-4 bedrooms, and this distribution provides insight into the prevalent house size in the dataset.
        """)
    elif selected_column == 'bathrooms':
        st.write("""
        **Description**: Bathrooms, like bedrooms, are a vital feature in housing data. The number of bathrooms can affect the house's price and desirability. A higher frequency of houses with more bathrooms can indicate luxury homes.
        """)
    elif selected_column == 'stories':
        st.write("""
        **Description**: Stories indicate the number of floors in a house. This variable can affect the house's price, with multi-story homes potentially offering more living space. A balanced distribution suggests that there are various housing styles in the dataset.
        """)
    else:
        st.write(f"**Description**: {selected_column.capitalize()} is a numerical feature in this dataset. Its distribution helps identify patterns or outliers that may affect the overall analysis.")


# 2. Area vs. Price scatter plot
st.subheader('Area vs. Price')
fig, ax = plt.subplots()
ax.scatter(df['area'], df['price'], color='green')
ax.set_title('Area vs. Price')
ax.set_xlabel('Area (sq. ft.)')
ax.set_ylabel('Price')
st.pyplot(fig)

# Description of the Area vs. Price relationship
st.write("""
**Description**: This scatter plot illustrates the relationship between the size of the house (area in square feet) and its price. Generally, a larger area tends to correspond to a higher price, though there can be exceptions due to factors like location, design, and amenities. By examining this plot, we can assess whether there is a clear positive correlation between house size and price. Outliers in the plot may represent unusually expensive small houses or large houses with lower-than-expected prices, which could indicate special conditions or market anomalies.
""")


# 3. Box plot of Price vs. Bedrooms (with option to choose another category)
st.subheader('Select a categorical variable for the box plot')
categorical_columns = df.select_dtypes(include=['object']).columns
selected_category = st.selectbox('Choose a category for box plot', ['bedrooms'] + list(categorical_columns))

if selected_category:
    fig, ax = plt.subplots()
    df.boxplot(column='price', by=selected_category, ax=ax, grid=False)
    ax.set_title(f'Price by {selected_category.capitalize()}')
    ax.set_xlabel(selected_category.capitalize())
    ax.set_ylabel('Price')
    st.pyplot(fig)

    # Provide dynamic descriptions based on the selected category
    if selected_category == 'bedrooms':
        st.write("""
        **Description**: This box plot shows the distribution of house prices based on the number of bedrooms. Houses with more bedrooms generally tend to be more expensive, but the distribution may reveal that there are outliers (such as smaller houses priced higher due to location or other features). The plot allows us to see the spread of prices for each bedroom count and helps identify whether more bedrooms always correlate with higher prices.
        """)
    elif selected_category == 'bathrooms':
        st.write("""
        **Description**: The number of bathrooms is an important factor in house pricing. This box plot illustrates how price varies with the number of bathrooms. Luxury homes with more bathrooms often have higher prices, but this isn't always the case, as other factors can contribute to pricing as well. By examining this plot, you can analyze the price distribution for different numbers of bathrooms.
        """)
    elif selected_category == 'stories':
        st.write("""
        **Description**: Stories refer to the number of floors in a house. This box plot shows the price variation according to the number of stories. Multi-story houses are often perceived as more valuable, but this can depend on the size and design of the house. The plot gives insight into how prices fluctuate across different types of houses, particularly whether single-story homes are valued differently from multi-story homes.
        """)
    elif selected_category == 'driveway':
        st.write("""
        **Description**: This box plot examines the relationship between having a driveway and the price of houses. A driveway can be a significant selling point, especially in areas where parking is scarce. Houses with driveways may generally be priced higher due to this feature, but the plot will reveal how much impact it has on pricing.
        """)
    elif selected_category == 'air_conditioning':
        st.write("""
        **Description**: The presence of air conditioning can significantly affect house pricing, particularly in warmer climates. This box plot explores how air conditioning influences house prices. Homes with air conditioning may command higher prices, but the extent of the price difference varies depending on other factors like the house's size, location, and design.
        """)
    else:
        st.write(f"""
        **Description**: This box plot shows the distribution of house prices across the chosen category: {selected_category.capitalize()}. By comparing how prices vary based on different {selected_category}, we can assess which features contribute more to house value and whether certain categories drive up or lower house prices.
        """)


# Conclusion Section with more elaborative conclusions
st.header('Conclusion')
st.write("""
From the visualizations, we can gather important insights:

1. **Distribution Insights**: The histograms provide a clear view of how each variable is distributed across the dataset. Skewed distributions or outliers can be quickly identified.
   
2. **Statistical Measures**: Central tendency measures like the mean and median allow us to understand the typical value for a variable, while the standard deviation indicates how much the data deviates from the average. These are important when deciding how to preprocess data for machine learning, as heavily skewed data may require transformations.
   
3. **Scatter Plot Analysis**: The scatter plot between area and price reveals trends in pricing. Larger houses generally cost more, but there may be areas where smaller houses command higher prices, indicating premium locations or features.

4. **Box Plot Insights**: The box plots help to compare price distributions across categorical variables like bedrooms, showing how different features influence pricing. Outliers in these plots might signify high-end or undervalued properties.
   
Overall, visualizing the data provides critical insights into the dataset's structure, aiding in data-driven decisions and further analysis.
""")
