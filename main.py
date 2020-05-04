import streamlit as st
import requests as rq
import seaborn as sns
import altair as alt
import matplotlib.pyplot as plt
import json as js
import pandas as pd
from pandas.io.json import json_normalize
import base64

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href

def main():

    st.title('App Gatinhos')
    st.image('cat2.jpg', width=100)
    st.markdown('Essa é uma aplicação desenvolvida para por em pratica os ensinamentos do curso de Data Science do AceleraDev.\n A aplicação em questão utiliza a TheCatApi (https://thecatapi.com/) como fonte de seus dados, para realizar uma breve análise sobre as raças dos gatinhos de tal Api (https://api.thecatapi.com/v1/breeds)')

    response = rq.get('https://api.thecatapi.com/v1/breeds')

    response.headers['x-api-key'] = 'a4824c2c-86fb-4ec8-8627-b5779c3bc0be'

    jdata = js.loads(response.text)
    df = pd.DataFrame(jdata)

    st.write('Os dados disponíveis na Api foram transformados para um Dataframe com', df.shape[0], 'observações e ', df.shape[1], 'colunas.')
    #st.write(df.to_csv('gatos.csv', index=False, header=True))

    st.markdown('**Visualizando os 5 primeiros registros do Dataframe**')
    st.dataframe(df.head(5))
    #st.markdown(df.shape)

    st.markdown('**Lista de colunas**')
    st.markdown(list(df.columns))

    st.markdown('**Descrevendo os dados do Dataframe**')
    st.dataframe(df.describe())

    #st.markdown('**Tipos os dados do Dataframe**')
    #st.dataframe(df.dtypes.value_counts())
    #st.markdown('**Busca tipo**')
    #st.dataframe(df.dtype())


   # st.header('**Agora vamos responder algumas questões interessates sobre alguns atributos dos gatinhos**')
    st.header('**Respondendo algumas questões sobre os atributos dos gatos**')
   
    st.write('**Lista  das raças "raras" (rare): **')
    st.markdown(list(df['name'][df['rare'] == 1]))

    st.write('**A faixa da vida util das raças que mais se repete (life_span) é **', df['life_span'].mode().loc[0])

    st.markdown('**Lista de raças classificadas como "perna curta" (short_legs)**')
    st.markdown(list(df['name'][df['short_legs'] == 1]))
    #st.write(round(len(list(df['name'][df['short_legs'] == 1])*100)/df['short_legs'].count(), 3), '%')
    #st.write()

    st.markdown('**Gerador de relações**')
    st.write('Como a maioria dos atributos são calssificações do tipo [0 ou 1] ou [ faixa de valores de 1 a 5], o gerador de relações faz uma tabelinha entre o nome das raças e o atributo escolhido. ')
    #st.markdown(list(df['name'][df['child_friendly'] == 5]))
    list_select = list(['adaptability', 'affection_level', 'child_friendly', 'dog_friendly', 'energy_level', 'grooming', 'health_issues', 'intelligence', 'shedding_level', 'social_needs', 'stranger_friendly', 'vocalisation', 'experimental', 'hairless', 'natural', 'rare', 'rex', 'suppressed_tail', 'short_legs', 'hypoallergenic', 'cat_friendly', 'country_code', 'life_span'])
   # list_atrib = df.columns
    pic_atrib = st.selectbox("Selecione o atributo:", list_select, 0)
    st.table(df.groupby(pic_atrib)['name'].unique())

    st.markdown('**Gráfico com a relação da quantidade de raças por paises **')
    plt.figure(figsize = (8,6))
    sns.countplot(x = 'country_code', data = df)
    plt.xticks(rotation = 60)
    st.pyplot()

    st.title('Ficou curios@? Veja como são as raças ...')

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


