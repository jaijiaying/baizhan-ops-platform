"""阶段09学习复现的 API 边界草稿；安装 fastapi/uvicorn 后可运行。"""
from fastapi import FastAPI
app=FastAPI(title='百战智能运营平台-学习复现')
@app.get('/health')
def health(): return {'status':'ok','pipeline':['inspiration','copy','image','publish','history']}
@app.post('/topics')
def create_topic(topic:str): return {'topic':topic,'next':'generate_titles'}
