import gradio as gr
def freet(name):
 return "Hello " + name + "!"
 app=gr.Interface(fn=freet,inputs="text",outputs="text")
 if _name_ == " _main_":
   app.launch(inbrowser=True)
