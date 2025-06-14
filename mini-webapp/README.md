# Mini Calculator Web App – Flask × Docker

この内容は、Flask を用いて作成した四則演算電卓アプリを Docker コンテナで動作させる構成になっている。  
ユーザーが 2 つの数値と演算子（+ - × ÷）を入力し、「計算する」ボタンで結果を表示するという内容になっている。

## ディレクトリ構成
mini-webapp/  
├── app.py # Flask アプリ本体  
├── requirements.txt # 必要なライブラリ一覧  
├── Dockerfile # Docker イメージビルド用設定  
└── templates/  
└── WebApp.html # HTML テンプレート（四則演算フォーム）  

## 使用技術

・Python 3.12
・Flask 3.0.3
・Gunicorn 22.0.0
・Docker Desktop（WSL2）

## 構築手順（Docker 利用）

### 1. ビルド
まずは、windowspowershellでmini-webappの内容が入っているパスまで行く
cd C:\Users\suzua\Docker\mini-webapp
次にビルドする
docker build --no-cache -t mini-webapp .

### 2.起動のためのdockerコマンド
docker run -d --name mini-webapp -p 8000:8000 mini-webapp
### 3.動作確認
http://localhost:8000 をブラウザ上で起動する
