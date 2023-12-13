import gradio as gr

def greet(name):
  return "Hello " + name + "!"

with gr.Blocks() as demo:
  name = gr.Textbox(label="Name")
  output = gr.Textbox(label="Output Box")
  greet_btn = gr.Button("Greet")
  greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

demo.launch(server_name = "0.0.0.0", server_port=143)
