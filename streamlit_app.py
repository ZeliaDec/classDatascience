{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import plotly.express as px\n",
        "\n",
        "url = 'https://raw.githubusercontent.com/michalis0/MGT-502-Data-Science-and-Machine-Learning/main/data/yield_df.csv'\n",
        "df_yield= pd.read_csv(url)\n",
        "\n",
        "# Assuming df_yield is your DataFrame\n",
        "data = df_yield['Item'].value_counts().reset_index()\n",
        "data.columns = ['Item', 'count']  # Rename columns for clarity\n",
        "\n",
        "# Streamlit app\n",
        "st.title('Shares of crops')\n",
        "\n",
        "# Create a pie chart using Plotly Express\n",
        "fig = px.pie(data, names='Item', values='count', title='Shares of crops')\n",
        "\n",
        "# Display the pie chart using Streamlit\n",
        "st.plotly_chart(fig)"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "authorship_tag": "ABX9TyOAjWLZl8+Dz0ZCqejjWoRz",
      "include_colab_link": true,
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.9.6"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
