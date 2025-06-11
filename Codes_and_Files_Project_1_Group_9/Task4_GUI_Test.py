#!/usr/bin/python
# encoding=utf8
import tkinter as tk
import time
from PIL import Image, ImageTk
from llama_cpp import Llama
# Load the LLaMA model
# Need to re-locate the model, it is not included in the zip file since it is too large
llm = Llama(
    model_path="/home/idler/forclass/ee5112/models/Meta-Llama-3-8B-Instruct.Q4_0.gguf",
    chat_format="llama-3",
    verbose=False
)

print("Chatbot is ready! Type 'exit' to end the conversation.")
print("*" * 50)

# Initialize conversation with system message
messages = [{"role": "system", "content": "You are an assistant who perfectly answer the problems."}]


# 发送消息
def sendMsg():
    t1_Msg.configure(state=tk.NORMAL)
    strMsg = "Me:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
    t1_Msg.insert("end", strMsg, 'green')
    sendMsg = t2_sendMsg.get('0.0', 'end')
    t1_Msg.insert("end", sendMsg)
    t2_sendMsg.delete('0.0', "end")

    user_input = sendMsg
    # Add user message to the conversation
    messages.append({"role": "user", "content": user_input})

    # Create chat completion
    response = llm.create_chat_completion(messages=messages)
    strMsg1 = "LLaMA:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
    t1_Msg.insert("end", strMsg1, 'green')
    sendMsg1 = response['choices'][0]['message']['content'] + '\n'
    t1_Msg.insert("end", sendMsg1)
    t1_Msg.config(state=tk.DISABLED)
    # print('*'*50)
    # Print the assistant's response

    # Add assistant's response to the conversation for context
    messages.append({"role": "assistant", "content": response['choices'][0]['message']['content']})

    print(strMsg + sendMsg)
    print()
    print(f"LLaMA: {response['choices'][0]['message']['content']}")
    print()


def clearBox():
    t1_Msg.configure(state=tk.NORMAL)
    t1_Msg.delete("0.0", tk.END)
    t1_Msg.config(state=tk.DISABLED)


# 创建窗口
app = tk.Tk()
app.title('Chat with Mr.Bot')

#
w = 1500
h = 660
sw = app.winfo_screenwidth()
sh = app.winfo_screenheight()
x = 200
y = (sh - h) / 2
app.geometry("%dx%d+%d+%d" % (w, h, x, y))
app.resizable(0, 0)

bg_image = Image.open("1.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
imgLabel = tk.Label(app, image=bg_photo)
imgLabel.place(x=800, y=0)

# 聊天消息预览窗口
t1_Msg = tk.Text(width=113, height=32)
t1_Msg.tag_config('green', foreground='#008C00')  # 创建tag
t1_Msg.place(x=2, y=35)
# bg_label = tk.Label(t1_Msg, image=bg_photo)
# bg_label.place(relwidth=1, relheight=1)
# t1_Msg.config(state=tk.DISABLED)
# t1_Msg.configure(state='disabled')

# 聊天消息发送
t2_sendMsg = tk.Text(width=112, height=10)
t2_sendMsg.place(x=2, y=485)

# 发送按钮
sendMsg_btn = tk.Button(text="Send", command=sendMsg)
sendMsg_btn.place(x=665, y=628)

delet_btn = tk.Button(text="Clear", command=clearBox)  # 建一个按键
delet_btn.place(x=580, y=628)


# 主事件循环
app.mainloop()