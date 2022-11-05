"""
找寻文件模板界面，用于找寻各类文件的模板
继承于content page
框架主要包括顶部标签用框架、内容框架、提示框架、返回框架
重写了内容框架里的功能（func_in_content_frame）
重写了跳转框架里的功能（jump_button_in_under_frame），添加了返回按钮
@ author: Kumarinko
@ version: 1.0.0
@ date: 2022-11-04
"""
from tkinter import *
from src.object_page import content_page
from src.menu_page import menu_page


class FindPage(content_page.ContentPage):
    # 类的属性
    title = "找寻文件模板"
    tips_txt = "找寻文件模板"
    __return_button_txt = "返回主菜单"

    # 类的方法
    # 初始化框架
    def __init__(self, master: Tk):
        super().__init__(master)
        self.master = master
        self.return_button = Button(self.under_frame, text=self.__return_button_txt, width=10, height=2,
                                    font=("微软雅黑", 12), bg="#89CFF0", command=self.__return_menu)

    # 对内容框架的方法重写
    def func_in_content_frame(self):
        pass

    # 对跳转框架的方法重写
    def jump_button_in_under_frame(self):
        # 找寻文档模板中只有返回主菜单按钮
        self.return_button.place(x=40, y=15)

    # 子类重写返回主菜单
    def __return_menu(self):
        self.destroy_content_page()
        menu_p = menu_page.MenuPage(self.master)
        menu_p.button_in_button_frame()
        menu_p.tips_label_in_tips_frame()


if __name__ == '__main__':
    root = Tk()
    root.title("找寻文件模板页测试")
    # 设置窗口大小
    width = 800
    height = 450
    scree_center_width = int((root.winfo_screenwidth() - width) / 2)
    scree_center_height = int((root.winfo_screenheight() - height) / 2)
    root.geometry(f"{width}x{height}+{scree_center_width}+{scree_center_height}")

    # 设置背景为颜色
    root.config(background="white")

    # 窗口不可放大
    root.resizable(False, False)
    find_page = FindPage(root)
    find_page.func_in_content_frame()
    find_page.jump_button_in_under_frame()
    root.mainloop()
