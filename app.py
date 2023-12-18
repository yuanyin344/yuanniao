import gradio as gr
def freet(name):
 return "Hello " + name + "!"
app=gr.Interface(fn=freet,inputs="text",outputs="text")
if __name__ == "__main__":
   app.launch(inbrowser=True,share=True)
