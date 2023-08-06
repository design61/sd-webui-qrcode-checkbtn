import gradio as gr
from modules import scripts


class Script(scripts.Script):
    def title(self):
        return "QR checkBTN"

    def after_component(self, component,**kwargs):
        if kwargs.get("elem_id")=="extras_tab":
            basic_send_button=gr.Button("检查二维码可否识别")
            basic_send_button.click(None,[],None,_js="()=>qrCheckImage(this)")
