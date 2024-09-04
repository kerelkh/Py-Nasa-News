import requests
import dotenv
import os
import streamlit as st

dotenv.load_dotenv()

api = os.getenv('API_KEY')

query = f"https://api.nasa.gov/planetary/apod?api_key={api}"

request = requests.get(query)

data = request.json()

if data:
    st.subheader(data['title'])
    st.write(f"By {data['copyright']} / {data['date']}")

    response = requests.get(data["url"])

    with open("image.jpg", "wb") as f:
        f.write(response.content)

    st.image("image.jpg")
    st.link_button(label="See HD Image", url=data['hdurl'])
    st.write(data["explanation"])
