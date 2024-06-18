# meeting-room-booking

## DB設計
### テーブル設計
**users**
- user_id : ユーザID
- user_name : ユーザ名

**rooms**
- room_id : 会議室ID
- room_name : 会議室名
- capacity : 定員
  - 各会議室ごとに定員を定める

**bookings**
- booking_id : 予約ID
- user_id : ユーザID
  - usersテーブルと紐づけ
- room_id : 会議室ID
  - roomsテーブルと紐づけ
- reserved_num : 予約人数
  - 会議室の定員まで
- start_date_time : 開始時刻
  - 15分刻み
- end_date_time : 終了時刻
  - 15分刻み

### DB条件
- capacity（定員）以上のreserved_num（予約人数）は不可
  - capacity ≧ reserved_num
- 利用時間は9:00~20:00

### 必要な処理
**Create**
- ユーザ登録
- 会議室作成
- 予約登録
**Read**
- ユーザ情報読み込み
- 会議室情報読み込み
- 予約一覧読み込み

**Update**
- なし

**Delete**
- なし