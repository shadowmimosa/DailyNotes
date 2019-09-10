import os
import re
import fileinput
folderpath = "C:\\Users\\ShadowMimosa\\Documents\\GitRepository\\DailyNotes\\Linux\\liuliuliu"


def remove_double_pdf(path):
    for root, dirs, files in os.walk(path):
        for value in files:
            filename, filetype = value.split('.')[0], value.split('.')[-1]
            if filetype == 'pdf':
                pdf_list = []
                for value1 in files:
                    if filename == value1.split('.')[0]:
                        pdf_list.append(value1)

                if len(pdf_list) == 2:
                    if value.split('.')[-1] == 'pdf':
                        os.remove(os.path.join(root, value))


def change_signature():
    for root, dirs, files in os.walk(folderpath):
        if len(files) != 0:
            for value in files:
                filename, filetype = value.split('.')[0], value.split('.')[-1]
                if filetype == 'md':
                    os.chdir(root)
                    # path = os.path.join(root, value).encode('utf-8')
                    for line in fileinput.input(files="yuyuyu.md", inplace=1):
                        pattern = re.compile(
                            r"\*+[0-9]{2,4}\.[0-9]{1,2}\.[0-9]{1,2}\*+")
                        if re.search(pattern, line):
                            line_copy = line.replace('*', '')
                            line = "</font>\n\n<font size=4 face='楷体'>\n<div style=\"text-align: right\"> ShadowMimosa </div>\n</font>\n<font size=3 face='楷体'>\n<div style=\"text-align: right\"> {} </div>\n</font>\n".format(
                                line_copy)

                    # with open(os.path.join(root, value), 'a') as fn:
                    #     raw_text = fn.readlines()
                    #     date_line = raw_text[-1]
                    #     init_line = -1
                    #     pattern = re.compile(
                    #         r"\*+[0-9]{2,4}\.[0-9]{1,2}\.[0-9]{1,2}\*+")
                    #     while True:
                    #         if date_line == '\n':
                    #             init_line -= 1
                    #             date_line = raw_text[init_line]
                    #             continue
                    #         elif re.search(pattern, date_line):
                    #             break
                    #         else:
                    #             print(filename, date_line)
                    #             break

def remove_pdf(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            filetype =filename.split('.')[-1]
            if filetype == 'pdf':
                os.remove(os.path.join(root, filename))

# change_signature()

if __name__ == "__main__":
    pass
