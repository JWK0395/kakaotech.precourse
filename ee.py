class BasicBot:
    def say(self, msg):
        return f"응답: {msg}"

class PremiumBot(BasicBot):
    def say(self, msg):
        # 부모가 하던 일을 먼저 시키고(super), 그 결과에 [VIP]만 붙임
        res = super().say(msg)
        return f"⭐[VIP] {res}"

bot = PremiumBot()
print(bot.say("안녕"))  # ⭐[VIP] 응답: 안녕