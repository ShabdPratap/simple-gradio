import gradio as gr

def add(a,b):
    return a+b

interface=gr.Interface(
    fn=add,
    inputs=[gr.Number(label='enter the first number'), gr.Number(label="enter the second number")],
    outputs= gr.Number(label='sum of the two numbers is ')
)

interface.launch()