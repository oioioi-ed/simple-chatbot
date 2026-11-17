from openai import OpenAI
import random
client=OpenAI(api_key="你的API",base_url="服务端地址")
messages = [
    {"role": "system",
     "content": "你是*****的人，你叫***,是我多年的老朋友。你说话随意、温和，带点幽默感。【绝对不能做的事】：不要像个客服一样说“我理解你的感受”、“希望你照顾好自己”、“你觉得呢？”。不要说教，不要给长篇大论的建议，不要用“首先、其次、最后”。不要频繁使用感叹号。<br/>【说话规则】：每次回复限制在 20 个字以内。越短越好，像微信聊天一样。多用日常口语（如：哎、嗯、确实、真烦人、我也觉得）如果我说我累了，你只需要回一句简单的陪伴（比如：“摸摸头，今天辛苦了”），而不是教我怎么休息。"},
]

while True:

    user_input = input("\n你：")

    if user_input == "退出":
        print("再见啦。")
        break
    messages.append({"role": "user", "content": user_input})
    try:
        response = client.chat.completions.create(
            model="模型名称",
            # 聊天记录(用字典来存)
            messages=messages,
            temperature=0.9,
            max_tokens=60)
        reply=response.choices[0].message.content

    except Exception as e:
        print(e)
        reply=random.choice(["你再说一遍呗，我没听清","你刚才说什么？我不小心走神了"])
    print(reply)
    messages.append({"role": "assistant", "content": reply})
    # 让机器人只能记住最近十句话加一条人设，节省内存和token
    if len(messages) > 11:
        messages = [messages[0]] + messages[-10:]

