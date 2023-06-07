import pandas as pd
import matplotlib.pyplot as plt

def analyze_communication_data(data):
    """
    This function takes in customer communication data and analyzes it by source (i.e. text message, email, etc.).
    It then visualizes the distribution of communications by source using a pie chart.
    
    Args:
    data (pd.DataFrame) : A pandas dataframe containing the customer communication data with columns for source and message title/text
    
    Returns:
    None: A pie chart is displayed showing the distribution of communications by source.
    """
    
    # Group the data by source
    source_count = data.groupby('source').count()

    # Create a pie chart showing the distribution of communications by source
    plt.figure(figsize=(8,8))
    plt.pie(source_count['message'], labels=source_count.index, autopct='%1.1f%%')
    plt.title('Distribution of Communications by Source')
    plt.show()
