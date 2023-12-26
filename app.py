"""
Université Virtuelle du Tchad.
Master Securité Logicielle.
LAGRE GABBA BERTRAND (https://github.com/FoubaDev/)
"""
import joblib
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu



@st.cache_resource
def load_data_csv():
   df = pd.read_csv("Canada_per_capita_income.csv")
   return df

@st.cache_resource
def load_data_sav():
   loaded_model = joblib.load(open('canada_per_capital.sav', 'rb'))
   return loaded_model


df = load_data_csv()
loaded_model = load_data_sav()


@st.cache_resource
def predict(input_data):
    
    my_array = np.array(input_data)
    input_reshaped = my_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_reshaped)
    
    st.write("The predicted income is :")
    st.write(prediction)
    st.write("income = 820.31 * year - 1616038.78")
    

# create column for dashbaord
@st.cache_resource(experimental_allow_widgets=True)
def dashboard():

    # Footer
    st.sidebar.markdown('---')
    st.sidebar.markdown('https://github.com/FoubaDev')


def main():

    with st.sidebar:
        selected = option_menu ("Income Prediction System",
                            
                            ['Home',
                             'Prediction',
                            'Dataset',
                            'Author',
                            ],
                            icons = ['house','bi bi-file-medical-fill','person','book','person'],
                            default_index=0
    
                            )
    
    if(selected == "Home") :
        st.title("Income Prediction System")
        st.title("income = 820.31 * year - 1616038.78")
        st.write("This dataset is just a sample. We have 46 rows and 2 columns. Accoriding to the size of the data, the linear regression can't give best mean square error")
        dashboard()

    if(selected == "Dataset") :
        st.write(df)
        st.write(df.shape)
    if(selected == "Prediction") :
    
       
        col1, col2 = st.columns(2)
    
        with col1:
            year = st.number_input('year', min_value=2022, step = 1, max_value = 2024) 

        CandaIncome = ''
        data = (year)   
        
        if st.button('Prediction'):
           
            result = predict(data)
        st.success(CandaIncome)
        
    if(selected == "Author") :
         
         
         st.subheader("Author : LAGRE GABBA BERTRAND")
         st.write(" Software Security Student at  Chad Virtual University. I have passion for Data Science") 
         st.write("Github link  : https://github.com/FoubaDev/TpML_UVT.git \n")

         st.write(" It is my pleasure to see you reading my work.")
         st.write(" The objective of this dataset is to  predict mean income of Canada for 2022, 2023 and 2024 year .")
        
if __name__=='__main__':
    main()