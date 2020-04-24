import streamlit as st
import requests as rq
import json as js

def main():
    st.title('Hello Wolrd')

    request = rq.get('https://api.thecatapi.com/v1/breeds')

    request.headers['x-api-key'] = 'a4824c2c-86fb-4ec8-8627-b5779c3bc0be'

    response_api = js.loads(request.text)

    st.markdown(response_api == request.json())

    response_api[:5]


if __name__ == '__main__':
    main()


