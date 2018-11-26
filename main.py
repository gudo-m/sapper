import random


class Sapper:
    def __init__(self, num_cols, num_rows):
        self.devst = True
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.cols = []
        gui = self.gui = Tk()
        canv = self.canv = Canvas(gui, width=num_cols * 50, height=num_rows * 50, bg='white')
        canv.grid(row=0, column=1)
        for r in range(num_rows):
            self.cols.append([])
            canv.create_line(0, 50 * r, num_cols * 50, 50 * r)
            for c in range(num_cols):
                canv.create_line(50 * c, 0, 50 * c, num_rows * 50)
                self.cols[-1].append(None)

        self.print_cols()

        self.frame = frame = Frame(self.gui)
        self.frame.grid(row=0, column=0, sticky="n")

        self.write_run_label = Label(frame, text="Ваш ход:", font="Arial 14")
        self.write_run_label.grid(row=1, column=0)

        self.write_run_error = Label(frame, text="Введите корректные координаты!", fg='red', font="Arial 14")

        self.write_run_cols_label = Label(frame, text="Колонка (начиная с 0):", font="Arial 14")
        self.write_run_cols_label.grid(row=2, column=0)

        self.write_run_cols = Entry(frame, font="Arial 14", textvariable=write_how_many_cols_label)
        self.write_run_cols.grid(row=3, column=0)

        self.write_run_rows_label = Label(frame, text="Строка (начиная с 0):", font="Arial 14")
        self.write_run_rows_label.grid(row=4, column=0)

        self.write_run_rows = Entry(frame, font="Arial 14", textvariable=write_how_many_rows_label)
        self.write_run_rows.grid(row=5, column=0)

        self.write_run = Button(frame, text='Сходить', width=25, height=5, font='arial 14')
        self.write_run.grid(row=6, column=0)

        self.write_run.bind_class('Button', '<1>', self.check_run)

    def print_cols(self):
        for row in range(len(self.cols)):
            for col in range(len(self.cols[row])):
                if self.cols[row][col] is None:
                    self.canv.create_rectangle(col * 50, row * 50, col * 50 + 50, row * 50 + 50, fill='yellow')
                    self.canv.create_text(
                        col * 50 + 25,
                        row * 50 + 25,
                        text='({}, {})'.format(col, row)
                    )
                elif not self.cols[row][col]:
                    self.canv.create_rectangle(col * 50, row * 50, col * 50 + 50, row * 50 + 50, fill='green')

    def initialize(self):
        for i in range(int((self.num_rows + self.num_cols) * 0.9)):
            self.cols[random.randint(0, self.num_rows - 1)][random.randint(0, self.num_cols - 1)] = True

    def run(self):
        flag = True
        for row in range(len(self.cols)):
            for col in self.cols[row]:
                if col is None:
                    flag = False
                    break
        if flag:
            win = Tk()
            Label(win, text="Вы выиграли!").pack()
            self.gui.destroy()
            win.mainloop()
        if self.cols[int(self.write_run_rows.get())][int(self.write_run_cols.get())]:
            self.canv.create_rectangle(int(self.write_run_cols.get()) * 50,
                                       int(self.write_run_rows.get()) * 50,
                                       int(self.write_run_cols.get()) * 50 + 50,
                                       int(self.write_run_rows.get().isdigit()) * 50 + 50, fill='red')
            lose = Tk()
            Label(lose, text="Вы проиграли!").pack()
            self.gui.destroy()
            lose.mainloop()
        else:
            rows = int(self.write_run_rows.get())
            cols = int(self.write_run_cols.get())
            for indexes in ((0, 0), (1, 1), (-1, -1), (-2, -2), (0, -1), (-1, 0)):
                try:
                    if self.cols[rows + indexes[0]][cols + indexes[1]] is None:
                            self.cols[rows + indexes[0]][cols + indexes[1]] = False
                    if self.cols[int(self.write_run_rows.get()) - indexes[0]][cols + indexes[1]] is None:
                            self.cols[rows - indexes[0]][cols + indexes[1]] = False
                    if self.cols[int(self.write_run_rows.get()) + indexes[0]][cols - indexes[1]] is None:
                            self.cols[rows - indexes[0]][cols + indexes[1]] = False
                except IndexError:
                    continue

    def check_run(self, e):
        print(e)
        if self.write_run_rows.get().isdigit() and self.write_run_cols.get().isdigit():
            error = False
            try:
                nn = self.cols[int(self.write_run_rows.get())][int(self.write_run_cols.get())]
                del nn
            except IndexError:
                error = True
            if error:
                self.write_run_error.grid(row=1, column=0, columnspan=3)
            else:
                self.write_run_error.grid_forget()
                if self.devst:
                    self.initialize()
                    self.devst = False
                self.run()
                self.print_cols()
        else:
            self.write_run_error.grid(row=1, column=0, columnspan=3)


def check_write_how_many(e):
    print(e)
    if write_how_many_rows.get().isdigit() and write_how_many_cols.get().isdigit():
        sapper = Sapper(int(write_how_many_cols.get()), int(write_how_many_rows.get()))
        sapper.gui.mainloop()
        root.destroy()
    else:
        if not write_how_many_error.winfo_viewable():
            write_how_many_error.grid(row=1, column=0, columnspan=3)


if __name__ == '__main__':
    name = input('Ваше имя? ')
    from tkinter import *

    root = Tk()

    write_how_many_label = Label(text="Введите размеры поля:", font="Arial 14")
    write_how_many_label.grid(row=1, column=0, columnspan=3)

    write_how_many_label = Label(text="Здравствуйте, {}!".format(name), font="Arial 14")
    write_how_many_label.grid(row=0, column=0, columnspan=3)

    write_how_many_error = Label(text="Введите корректные размеры!", fg='red', font="Arial 14")

    write_how_many_cols_label = Label(text="Колонок:", font="Arial 14")
    write_how_many_cols_label.grid(row=2, column=0, columnspan=2)

    write_how_many_cols = Entry(root, font="Arial 14", textvariable=write_how_many_cols_label)
    write_how_many_cols.grid(row=2, column=2, columnspan=1)

    write_how_many_rows_label = Label(text="Строк:", font="Arial 14")
    write_how_many_rows_label.grid(row=4, column=0, columnspan=2)

    write_how_many_rows = Entry(root, font="Arial 14", textvariable=write_how_many_rows_label)
    write_how_many_rows.grid(row=4, column=2, columnspan=1)

    write_how_many = Button(root, text='Создать', width=25, height=5, font='arial 14')
    write_how_many.grid(row=6, column=0, columnspan=3)

    write_how_many.bind_class('Button', '<1>', check_write_how_many)

    root.mainloop()
