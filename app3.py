import streamlit as st
import pickle
import numpy as np
import pandas as pd
import helper
import gzip
# Load pickled models (example placeholders)

# Load compressed car model
with gzip.open('pipe_car.pkl.gz', 'rb') as file:
    car = pickle.load(file)

# car = pickle.load(open('pipe_car.pkl','rb'))
car_df = pickle.load(open('car_df.pkl','rb'))

laptop_df = pickle.load(open('laptopdf.pkl','rb'))
laptop = pickle.load(open('pipe.pkl','rb'))

smartphone = pickle.load(open('smpipe.pkl','rb'))
sm_df = pickle.load(open('sm_df.pkl','rb'))

# Load custom CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True) 
    
st.sidebar.image("https://raw.githubusercontent.com/Ajinkya-19/Commodity-Price-Predictor/refs/heads/main/COMMODITY-transformed.png")
#st.sidebar.title('Commodity Price Predictor')
user_menu = st.sidebar.selectbox('Choose the Commodity',['Laptop','Smartphone','Car'])

if user_menu == 'Laptop':
    st.image("https://www.bing.com/images/blob?bcid=r3zkL3mEfeUHhw")
    st.markdown("<h1 class='main-title'>Laptop Price Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Find out the estimated price of a laptop based on its specifications.</p>", unsafe_allow_html=True)

    st.sidebar.markdown('### Select The brand of Laptop')
    company = st.sidebar.selectbox('Brand',laptop_df['Company'].unique())
    avail_lap_os = helper.filter_laos(laptop_df,company)
    type = st.sidebar.selectbox('Type',laptop_df['TypeName'].unique())
    
    Ram = st.selectbox('RAM(in GB)', [2,4,6,8,12,16,24,32,64])
    weight = st.number_input('Weight of the Laptop')
    touchscreen = st.selectbox('Touchscreen',['No','Yes'])
    ips = st.selectbox('IPS',['No','Yes'])
    screen_size = st.slider('Scrensize in inches', 10.0, 18.0, 13.0)
    resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
    cpu = st.selectbox('CPU',laptop_df['Cpu brand'].unique())
    hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
    ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])
    gpu = st.selectbox('GPU',laptop_df['Gpu brand'].unique())
    os = st.selectbox('OS',avail_lap_os)
    
    if st.button('Predict Price'):
    # query
        ppi = None
        if touchscreen == 'Yes':
            touchscreen = 1
        else:
            touchscreen = 0

        if ips == 'Yes':
            ips = 1
        else:
            ips = 0

    # Predict button for laptop
        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
        query = np.array([company,type,Ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

        query = query.reshape(1,12)
        st.title("The predicted price of this configuration is " + str(int(np.exp(laptop.predict(query)[0]))))
        
    else:
        st.info("Please select a commodity to proceed.")
        
if user_menu == 'Car':
    
    st.image("https://raw.githubusercontent.com/Ajinkya-19/Commodity-Price-Predictor/refs/heads/main/car%20png.png")
    st.markdown("<h1 class='main-title'>Car Price Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Find out the estimated price of a Car based on its specifications.</p>", unsafe_allow_html=True)

    st.sidebar.markdown('### Select the car')
    car_model_name = st.sidebar.selectbox("Model Name", car_df['model'].unique())
    car_fuel_type = st.sidebar.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric","CNG","LPG"])
    car_age = st.number_input('Age of Vehical',1,30)
    seller_type = st.selectbox("Seller",['Dealer','Individual','Trustmark Dealer'])
    car_mileage = st.number_input("Mileage (in km/l)", 5, 50, step=1)
    car_driven = st.slider('Travel of Vehicle',min_value = 100,max_value = 400000)
    car_transmission = st.selectbox('transmission_type',['Manual', 'Automatic'])
    car_Engine = st.slider('Engine Power (HP)',min_value=200,max_value=10000)
    car_seats = st.number_input('Number of Seats',0,10,step = 1)
    # Predict button for car
    if st.button("Predict Price"):
        if car_transmission == 'Manual':
            car_transmission = 1
        else:
            car_transmission = 0

        if car_transmission == 'Automatic':
            car_transmission = 1
        else:
            car_transmission = 0

    # Sample input transformation
        car_features = np.array([car_model_name, car_age, car_mileage, car_fuel_type,seller_type,car_driven,car_transmission,car_Engine,car_seats])
        # Mock prediction (replace with actual model)
        query = car_features.reshape(1,9)
        
        car_price = np.exp(car.predict(query)[0])  # Get the predicted price
        car_price_six_digits = int(car_price / 10)  # Scale down to six digits

        # Display the scaled price
        st.title(f"The predicted price for the car is: ₹{car_price_six_digits:,}")
        #car_price = str(int(np.exp(car.predict(query)[0])))
        #st.title("The predicted price for the car is: ₹"+ car_price)
        
if user_menu =='Smartphone':
    st.image("https://raw.githubusercontent.com/Ajinkya-19/Commodity-Price-Predictor/refs/heads/main/android-best-phones-removebg-preview.png")
    st.markdown("<h1 class='main-title'>Smartphone Price Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Find out the estimated price of a Smartphone based on its specifications.</p>", unsafe_allow_html=True)

    brand = st.sidebar.selectbox('Select a brand',sm_df['brand_name'].unique())
    segment = st.sidebar.radio('Choose the segment',sm_df['segment'].unique())
    avail_model = helper.filter_models(sm_df,brand,segment)
    avail_pros = helper.filter_pros(sm_df,brand,segment)
    avail_os = helper.filter_OS(sm_df,brand,segment)
    avail_width = helper.filter_width(sm_df,brand,segment)
    avail_height = helper.filter_height(sm_df,brand,segment)
    model = st.sidebar.selectbox('Choose the Model',avail_model)


    connectivity = st.sidebar.selectbox('5G connectivity',['Yes','No'])
    
    rating = st.slider('select the rating',0,10)
    OS = st.selectbox('Choose the operating system',avail_os)
    processor = st.selectbox('Choose the processor',avail_pros)
    battery = st.slider('select battery capecity(MaH)',0,20000)
    fast_charging = st.selectbox('fast_charging_available',['Yes','No'])
    Ram = st.selectbox('choose Ram',sm_df['Ram'].unique())
    memory = st.selectbox('Choose memery',sm_df['internal_memory'].unique())
    extended_memory_available = st.selectbox('Expendable memory',['Yes','No'])

    screen_size = st.slider('select the Screen Size',3,10)
    refresh_rate = st.selectbox('refresh rate',sm_df['refresh_rate'].unique())
    num_cam = st.selectbox('Select the cameras',sm_df['num_rear_cameras'].unique())
    Camera = st.selectbox('Choose camera',sm_df['primary_camera_rear'].unique())
    front_cam = st.selectbox('front camera(MP)',sm_df['primary_camera_front'].unique())

    width = st.selectbox('width',avail_width)
    height = st.selectbox('height',avail_height)
    pixel_count = st.slider('Select The pixel_count',10000,4000000)
    
    
    
    if st.button ('Predict Price'):
        if connectivity =='Yes':
            connectivity = 1
        else :
            connectivity = 0
        
        if fast_charging == 'Yes':
            fast_charging = 1
        else :
            fast_charging = 0
        
        if extended_memory_available == 'Yes':
            extended_memory_available = 1
        else :
            extended_memory_available = 0
            
            # Dictionary Form for Model Input
        query = pd.DataFrame([{
        'brand_name': brand,
        'model': model,
        'os': OS,
        'avg_rating': rating,
        'processor_brand': processor,
        'Ram': Ram,
        'internal_memory': memory,
        'primary_camera_rear': Camera,
        'battery_capacity': battery,
        '5G': connectivity,
        'fast_charging_available': fast_charging,
        'pixel_count': pixel_count,
        'segment': segment,
        'screen_size': screen_size,
        'refresh_rate': refresh_rate,
        'num_rear_cameras': num_cam,
        'primary_camera_front': front_cam,
        'width': width,
        'height': height,
        'extended_memory_available': extended_memory_available
        }])
    
        st.title("The predicted price of this configuration is " + str(int(np.exp(smartphone.predict(query)[0]))))
        
    else:
        st.info("Please select a commodity to proceed.")



st.markdown("<div class='footer'>© 2024 Commodity Price Predictor | Designed by Ajinkya Chavan</div>", unsafe_allow_html=True)

    
