# -*- encoding: GBK -*-
from os.path import exists, join
from datetime import datetime
from csv import writer
from re import findall
from processing_bar import ProcessingBar


def process(path_: str, output_name: str = None) -> None:
    if exists(path_):
        input_file_ = open(path_, "r", errors='ignore', encoding="GBK")
        file = open(output_name, "w", newline='', errors='ignore', encoding="GBK")
        write = writer(file, dialect='excel')
        write.writerow(
            ["Դip", "Դip�˿�", "Ŀ��ip", "Ŀ��ip�˿�", "ipЭ��", "Э��", "����", "ʱ��", "���ݴ�С", "����",
             "������Ϣ", "��������"])
        with open(path_, "r", errors='ignore', encoding="GBK") as f:
            bar = ProcessingBar(sum(1 for line in f), "��������:")
        bar.start()
        while True:
            temp = input_file_.readline()
            if "********" in temp:
                continue
            if not temp:
                break
            temp = temp.removesuffix("\n").split("; ")
            writen = []
            try:
                result: list[tuple[str]] = findall(
                    r"((((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?):(6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{1,3}|\d))|((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?))",
                    temp[2] if len(temp) == 4 else temp[4])
                if result:
                    for ip in result:
                        if ip[0].find(":") == -1:
                            writen.append(ip[0])
                            writen.append("��")
                        else:
                            writen.append(ip[0][:ip[0].find(":")])
                            writen.append(ip[0][ip[0].find(":") + 1:])
                    writen.append("ipv4")
                else:
                    result: list[tuple[str]] = findall(
                        r"(([\da-fA-F]{1,4}:){6}((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|::([\da-fA-F]{1,4}:){0,4}((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|([\da-fA-F]{1,4}:):([\da-fA-F]{1,4}:){0,3}((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|([\da-fA-F]{1,4}:){2}:([\da-fA-F]{1,4}:){0,2}((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|([\da-fA-F]{1,4}:){3}:([\da-fA-F]{1,4}:)?((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|([\da-fA-F]{1,4}:){4}:((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}|:((:[\da-fA-F]{1,4}){1,6}|:)|[\da-fA-F]{1,4}:((:[\da-fA-F]{1,4}){1,5}|:)|([\da-fA-F]{1,4}:){2}((:[\da-fA-F]{1,4}){1,4}|:)|([\da-fA-F]{1,4}:){3}((:[\da-fA-F]{1,4}){1,3}|:)|([\da-fA-F]{1,4}:){4}((:[\da-fA-F]{1,4}){1,2}|:)|([\da-fA-F]{1,4}:){5}:([\da-fA-F]{1,4})?|([\da-fA-F]{1,4}:){6}:)|((([\da-fA-F]{1,4}:){6}((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|::([\da-fA-F]{1,4}:){0,4}((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|([\da-fA-F]{1,4}:):([\da-fA-F]{1,4}:){0,3}((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|([\da-fA-F]{1,4}:){2}:([\da-fA-F]{1,4}:){0,2}((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|([\da-fA-F]{1,4}:){3}:([\da-fA-F]{1,4}:)?((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|([\da-fA-F]{1,4}:){4}:((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}|:((:[\da-fA-F]{1,4}){1,6}|:)|[\da-fA-F]{1,4}:((:[\da-fA-F]{1,4}){1,5}|:)|([\da-fA-F]{1,4}:){2}((:[\da-fA-F]{1,4}){1,4}|:)|([\da-fA-F]{1,4}:){3}((:[\da-fA-F]{1,4}){1,3}|:)|([\da-fA-F]{1,4}:){4}((:[\da-fA-F]{1,4}){1,2}|:)|([\da-fA-F]{1,4}:){5}:([\da-fA-F]{1,4})?|([\da-fA-F]{1,4}:){6}:):(6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{1,3}|\d))",
                        temp[2] if len(temp) == 4 else temp[4])
                    if result:
                        for ips in result:
                            for ip in ips:
                                if ip == "":
                                    continue
                                writen.append(ip)
                                writen.append("�޷�����")
                                break
                        writen.append("ipv6")
                writen.append(temp[1])
                temp_ = datetime.strftime(datetime.strptime(temp[0], "%a %b %d %H:%M:%S %Y"), '%Y-%m-%d %H:%M:%S')
                writen.append(temp_[:temp_.find(" ")])
                writen.append(temp_[temp_.find(" ") + 1:])
                writen.append("��" if len(temp) == 4 else temp[3])
                writen.append("��" if len(temp) == 4 else temp[2])
                if len(temp) == 4 and temp[2].find("timed out"):
                    writen.append("Connection time out")
                    writen.append(temp[3])
                elif len(temp) >= 6:
                    writen.append(temp[5])
                    if len(temp) == 7:
                        writen.append(temp[6])
                    else:
                        writen.append("��")
                else:
                    writen.append("��")
                    writen.append("��")
                write.writerow(writen)
            except Exception as err:
                bar.error(err)
                bar.warn(temp)
            finally:
                bar.next()
        bar.stop()
        input_file_.close()
        file.close()


if __name__ == "__main__":
    print("�������ڶ�iptraf��¼����־���н���")
    while True:
        print("��������־�ļ���(Q���˳�):")
        input_file = input()
        if input_file == "Q" or input_file == "q":
            exit()
        if not exists(join("./", input_file)):
            print(f"{join('./', input_file)}�ļ�������")
        else:
            if input_file.endswith(".log"):
                break
            else:
                print("��������ȷ���ļ�������.log��β��")
    while True:
        print("����������ļ���(Q���˳�):")
        output_file = input()
        if output_file == "Q" or output_file == "q":
            exit()
        if output_file.endswith(".csv"):
            break
        else:
            print("ֻ֧����csv��ʽ���")
    process(input_file, output_file)
    print("��������˳�")
    input()
    