"""スマホのボタン側のプログラム

© 2024 Swimmy石神井公園校
"""

import js

import btncon

# ボタンのコントローラーを発動
btn = btncon.ButtonController()

# 準備OKでないなら、ボタンを失敗マークにする
if not btn.is_ready():
    js.btn_failure()


# ボタン発動時
async def btn_click(event) -> None:
    await btn.send_trigger()

    # 信号の送信に失敗した場合はボタンを失敗マークにする
    if not btn.is_send_ok():
        js.btn_failure()
        return

    # IoT側が動作完了するまで10秒ごとに確認する
    while not await btn.is_done():
        await btn.sleep(10)

    js.btn_success()
