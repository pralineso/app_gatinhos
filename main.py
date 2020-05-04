import streamlit as st
import requests as rq
import json as js
import pandas as pd
from pandas.io.json import json_normalize

def main():
    st.title('App Gatinhos')
    st.image('cat2.jpg', width=100)
    st.markdown('Essa é uma aplicação desenvolvida para por em pratica os ensinamentos do curso de Data Science do AceleraDev.\n A aplicação em questão utiliza a TheCatApi (https://thecatapi.com/) como fonte de seus dados, para realizar uma breve análise sobre as raças dos gatinhos de tal Api (https://api.thecatapi.com/v1/breeds)')

    response = rq.get('https://api.thecatapi.com/v1/breeds')

    response.headers['x-api-key'] = 'a4824c2c-86fb-4ec8-8627-b5779c3bc0be'

    #names = response_api["name"][2]
    #names
    #response_api[0]["name"]

    jdata = js.loads(response.text)
    df = pd.DataFrame(jdata)
    #print (df.head(5))

    st.write('Os dados disponíveis na Api foram transformados para um Dataframe com', df.shape[0], 'observações e ', df.shape[1], 'colunas.')


    st.markdown('**Visualizando os 5 primeiros registros do Dataframe**')
    st.dataframe(df.head(5))
    st.markdown(df.shape)

    st.markdown('**Lista de colunas**')
    st.markdown(list(df.columns))

    st.markdown('**Descrevendo os dados do Dataframe**')
    st.dataframe(df.describe())

    st.subheader('Agora vamos responder algumas questões interessates sobre alguns atributos dos gatinhos')

    st.markdown('**Quantidade de raças "raras" (rare)**')

    st.markdown('**Média da idade das raças ()**')

    st.markdown('**% de raças que classificadas como "perna curta" (short_legs)**')

    st.markdown('**Quais são as raças consideradas mais amigaveis com crianças (child_friendly)**')

    st.markdown('**Quais são as raças consideradas mais adaptáveis (adaptability)**')

    st.markdown('**Gráfico com a relação da origen (paises) das raças de gatinhos com a quantidade**')

    st.subheader('Ficou curios@? Veja a carinha dos bixanos ...')

    pics = {
    "Cat": "https://cdn.pixabay.com/photo/2016/09/24/22/20/cat-1692702_960_720.jpg",
    "Puppy": "https://cdn.pixabay.com/photo/2019/03/15/19/19/puppy-4057786_960_720.jpg",
    "Sci-fi city": "https://storage.needpix.com/rsynced_images/science-fiction-2971848_1280.jpg"
    }
    pic = st.selectbox("Picture choices", list(pics.keys()), 0)
    st.image(pics[pic], use_column_width=True, caption=pics[pic])

    st.markdown('**Nome:**')
    st.markdown('**Origem:**')
    st.markdown('**Código do país:**')
    st.markdown('**Temperamento:**')
    st.markdown('**Descrição:**')
    
    


if __name__ == '__main__':
    main()


