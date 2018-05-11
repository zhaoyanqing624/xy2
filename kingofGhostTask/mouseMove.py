import autopy3 as autopy,PIL

autopy.mouse.smooth_move(300, 300)  # 平滑移动鼠标（上面那个是瞬间的）

autopy.mouse.click()  # 单击
autopy.mouse.toggle(True)  # 按下左键
autopy.mouse.toggle(False)  # 松开左键

autopy.key.toggle('q', True, autopy.key.MOD_ALT)
autopy.key.toggle('q', False, autopy.key.MOD_ALT)