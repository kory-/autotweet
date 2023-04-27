import tweepy
import time
from dotenv import load_dotenv
import os

load_dotenv()

# Twitter APIキーとトークンを設定
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# 認証を行い、APIクライアントを初期化
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# 特定のタグを含むツイートを検索
tag_to_delete = '#tag_to_delete'
max_id = None

while True:
    # ページネーションを使用してツイートを取得
    tweets = api.user_timeline(count=200, max_id=max_id, tweet_mode='extended', include_rts=False)

    # タグが含まれているツイートを削除
    if not tweets:
        break

    for tweet in tweets:
        if tag_to_delete in tweet.full_text:
            print(f"Deleting tweet: {tweet.full_text}")
            api.destroy_status(tweet.id)
            time.sleep(1)  # APIコールの間に1秒間の待機時間を設ける

        max_id = tweet.id - 1

    # ページネーションの間に待機時間を設ける
    time.sleep(60)  # 60秒待機
