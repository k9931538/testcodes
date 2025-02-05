from openai import OpenAI
import data

client = OpenAI(api_key="sk-93b55670387f451b90df66c3578206d6", base_url="https://api.deepseek.com")
def get_response(name, query):
    names = []
    reasons = []
    dataLoad = data.DataLoad(name)
    parser = "이름과 원인을 알려줘, 그 사이는 | 문자로 구분해줘"
    order_messages = []
    order_messages.append({"role": "system", "content": f"{name}{query} {parser}"})
    for msg in dataLoad.Get_All_Message():
        if msg.creator == name and msg.user != name:
            order_messages.append({"role": "user", "content": f"작성자:{msg.user}, 제목: {msg.subject}: 내용: {msg.contents}"})
    
    response = client.chat.completions.create(
        model="deepseek-chat", 
        messages=order_messages,
        stream=False
    )
    
    result = response.choices[0].message.content
    for output in result.split('\n'):
        txt = output.split('|')
        if len(txt) == 1:
            names.append("")
            reasons.append(txt[0])
        elif len(txt) == 2:
            names.append(txt[0])
            reasons.append(txt[1])
    return names, reasons
