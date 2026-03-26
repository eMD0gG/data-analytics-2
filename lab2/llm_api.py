from gigachat import GigaChat
import json
import config

def call_llm(video_title, comment_text):
    prompt = config.PROMPT.format(
        video_title=video_title,
        comment_text=comment_text
    )

    with GigaChat(credentials=config.GIGACHAT_CREDENTIALS, verify_ssl_certs=False) as giga:
        response = giga.chat(prompt)
        print(response)
        content = response.choices[0].message.content
        print(content)
    try:
        result = json.loads(content)
    except json.JSONDecodeError:
        result = {"sentiment": None, "emotion": None, "intensity": None, "aspects": [], "recommendation": None}
    return result