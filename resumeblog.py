from pywebio import session, start_server
from pywebio.output import put_markdown


def my_resume():
    session.set_env(title='老表的简历', output_animation=False)
    with open('resumeblog/Resume.md') as md:
        md_txt = md.read()
    put_markdown(md_txt)
    put_markdown('<br>祝你求职成功，记得和老表一起学习云服务器！')

if __name__ == '__main__':
    start_server(my_resume, port=8081, auto_open_webbrowser=True)