# 1) ベースイメージ
FROM python:3.12-slim

# 2) 環境変数
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3) 作業ディレクトリ
WORKDIR /app

# 4) 依存インストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5) アプリ本体をコピー
COPY . .

# 6) コンテナ外に公開するポート
EXPOSE 8000

# 7) 本番用サーバで起動
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
