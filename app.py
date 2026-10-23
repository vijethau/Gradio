import gradio as gr
gr.close_all()

def details(name, age, preference, hobbies):
    return f"Name:{name}\nAge:{age}\nSubject Preference: {preference}\n Hobbies: {[h for h in hobbies]}"

demo = gr.Interface(
    fn=details,
    inputs=[gr.Textbox(label="Name:"),
            gr.Slider(label="Age:"),
            gr.Radio(label="Subject Preference: ", choices=['C','C#','Java','Python']),
            gr.Checkboxgroup(label='Hobbies:', choices=['Painting', 'Singing', 'Reading', 'Gaming'])
           ]
    outputs=[gr.Textbox()],
)

demo.launch()
