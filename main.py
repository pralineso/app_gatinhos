import streamlit as st
import requests as rq
import seaborn as sns
import matplotlib.pyplot as plt
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

    st.markdown('**Quantidade de raças "raras" (rare): **')
   # st.table(df[df['rare']=='1'].count())

    st.write('**Faixa média da vida util das raças que mais se repete (life_span): **', df['life_span'].mode().loc[0])

    st.markdown('**% de raças que classificadas como "perna curta" (short_legs)**')
    #st.markdown(df['short_legs'].mean()/df['short_legs'].count())

    st.markdown('**Quais são as raças consideradas mais amigaveis com crianças (child_friendly)**')
    #st.markdown(df['name']df['child_friendly']=='1')

    st.markdown('**Quais são as raças consideradas mais adaptáveis (adaptability)**')
    #st.markdown(list(df['adaptability']=='5'))

    st.markdown('**Gráfico com a relação da origen (paises) das raças de gatinhos com a quantidade**')

    #st.write(sns.countplot(x = 'origin', data = df))

    st.subheader('Ficou curios@? Veja a carinha dos bixanos ...')

   # st.table(df[['id','name']])

    #id_list = map(df[['id','name']])
   # print(id_list)
    #st.markdown(id_list)
   # https://api.thecatapi.com/v1/images/search?breed_id=id_list[0]'
    list_select = list(df['name'])
    #lit_name.append(df['name'])
    pic_name = st.selectbox("Selecione a raça do gato:", list_select, 0)

    #pega o id da raça selecionada
    id_breed = df['id'][df['name'] == pic_name]
    #origem =  df['origin'][df['name'] == pic_name]
    #temperamento = df['temperament'][df['name'] == pic_name]
    #descricao = df['description'][df['name'] == pic_name]

    #Configurações para puxar a url da imagem da raça selecionada
    payload = {'breed_id': id_breed}   
    response_img = rq.get('https://api.thecatapi.com/v1/images/search', params=payload)
    response_img.headers['x-api-key'] = 'a4824c2c-86fb-4ec8-8627-b5779c3bc0be'
    jimg = js.loads(response_img.text)
    image_url = jimg[0]["url"]

    #Exibindo a imagem e as demais informações
    st.image(image_url, use_column_width=True, caption=('Fonte: ' + image_url))
    st.write('**Name:** ', pic_name)
    st.write('**Origin:** ', df['origin'][df['name'] == pic_name].iloc[0]  )
    st.write('**Temperament:** ',  df['temperament'][df['name'] == pic_name].iloc[0])
    st.write('**Description:** ', df['description'][df['name'] == pic_name].iloc[0]) 
    
    


if __name__ == '__main__':
    main()


