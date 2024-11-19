import os
from datetime import datetime

from CTkMessagebox import CTkMessagebox
from customtkinter import CTk, CTkButton, CTkLabel, StringVar, filedialog

from lib.logic import generate_csv, generate_data


class Application(CTk):
    def __init__(self):
        super().__init__()
        self.title('Receiving Barcode Generator')
        self.iconbitmap('resources/icon.ico')
        self.geometry("500x300")
        self.out_path = StringVar(value='Select Folder')
        self.file_path = StringVar(value='Select File')

        # Configure grid
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=2)

        self.out_path_label = CTkLabel(self,
                                       textvariable=self.out_path,
                                       wraplength=200
                                       )
        self.out_path_button = CTkButton(self,
                                         command=self._set_out_dir,
                                         text='Select Output Folder'
                                         )
        self.out_path_label.grid(column=1, row=0, sticky='ew', padx=(10, 10))
        self.out_path_button.grid(column=0, row=0, sticky='ew', padx=(10, 10))

        self.file_path_button = CTkButton(self,
                                          command=self._get_file_path,
                                          text='Select Receiving CSV'
                                          )
        self.file_path_label = CTkLabel(self,
                                        textvariable=self.file_path,
                                        text='Select File',
                                        wraplength=200
                                        )
        self.file_path_button.grid(column=0, row=1, sticky='ew', padx=(10, 10))
        self.file_path_label.grid(column=1, row=1, sticky='ew', padx=(10, 10))

        self.generate_button = CTkButton(self,
                                         command=self._generate_csv,
                                         text='Generate CSV',
                                         fg_color='grey',
                                         hover=False
                                         )
        self.generate_button.grid(
            row=2,
            columnspan=2,
            sticky='ew',
            padx=(10, 10)
        )

    def _generate_csv(self):
        try:
            res_path = os.path.join(
                self.out_path.get(),
                f'receiving_{datetime.now().strftime('%d-%m-%Y %H_%M')}.csv'
            )
            generate_csv(
                out_path=res_path,
                data=generate_data(self.file_path.get())
            )
            CTkMessagebox(
                self,
                title='Barcodes Generated',
                message='Done',
                icon='check'
                )
        except Exception as err:
            CTkMessagebox(self,
                          title='Uh Oh something went wrong!',
                          message=err, icon='cancel'
                          )

    def _set_out_dir(self):
        dir = filedialog.askdirectory()
        print(dir)
        if dir:
            self.out_path.set(dir)
        self._validate_paths()

    def _get_file_path(self):
        fp = filedialog.askopenfilename()
        print(fp)
        if fp:
            self.file_path.set(fp)
        self._validate_paths()

    def _validate_paths(self):
        if self.out_path.get() != 'Select Folder' and self.file_path.get() != 'Select File':  # noqa: E501
            self.generate_button.configure(
                fg_color='green',
                hover=True,
                hover_color='darkgreen'
            )


if __name__ == "__main__":
    app = Application()
    app.mainloop()
