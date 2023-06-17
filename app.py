import os
from pathlib import Path
import streamlit as st
from langchain import OpenAI

from langchain.chains import AnalyzeDocumentChain
from langchain.chains.summarize import load_summarize_chain

#開発
# from dotenv import load_dotenv
# load_dotenv()

#本番
os.environ["OPENAI_API_KEY"] = st.secrets.OpenAIAPI.openai_api_key

import streamlit as st
from langchain import OpenAI
from langchain.chains import AnalyzeDocumentChain
from langchain.chains.summarize import load_summarize_chain

# Streamlit UIの設定
st.title('文書の要約')
st.write('文書を要約得意です。')

# ユーザーがテキストエリアに入力するためのUI部品
document = st.text_area("文書をこちらに入力してください:")

# 要約ボタンを押したときの処理
if st.button('要約'):

    # もし、入力があれば
    if document:
        st.write('thingking...')

        # 要約チェーンのセットアップ
        llm = OpenAI(temperature=0)
        summary_chain = load_summarize_chain(llm, chain_type="map_reduce")
        summarize_document_chain = AnalyzeDocumentChain(combine_docs_chain=summary_chain)
        
        # 文書を要約
        summary = summarize_document_chain.run(document)
        
        # 要約を表示
        st.subheader('要約:')
        st.write(summary)

    # 入力がない場合、エラーメッセージを表示
    else:
        st.write('エラー: 文書を入力してください。')


