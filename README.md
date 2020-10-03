# fk-bot-3
## 目的
FKを利用したトレードを完全自動化すること

## 言語
Python

## データベース
Firebase（候補）

## ハードウェア
raspberry pi4
- カメラモジュール
- サーボモータ
- リレータッチボード
  - またはタッチペン（トリプルタップで画面を拡大する必要がないなら）

クレーン装置
- XYZ軸に移動可能

## Webアプリ
未定

## 処理の大まかな流れ
- タブレットの画面撮影
  - モータでカメラとリレータッチボードの座標を移動
  - リレータッチボードで画面タップ
  - カメラで撮影
- 画像処理
  - OCRを用いた画像認識 
  - 始値と（できれば）時刻の抽出
- FKルールと照合
  - FKのルールに則りFKステータスを更新する
  - サインを判定＆Slackに送信
- 売買操作
  - リレータッチボード or seleniumを利用したブラウザ操作
  - 証券アプリを起動
  - パスワードの入力
  - 売買の操作をタップして行う
    -「売り」「買い」の選択
    - 建玉の枚数
    - 成行きの選択など

- Webアプリ
  - カギ足のグラフ表示
  - 入力フォーム
  - 送信、削除
  
  
