import os
import re
import time
import xlwt
import json
import requests
from urllib import parse

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from urllib.request import urlretrieve


class Music_Dowload:
    def __init__(self):
        self.ui = QUiLoader().load('dowload.ui')#关联ui界面文件
        self.ui.output_index_Edit.setReadOnly(True)  # 设置为只读模式
        self.ui.output_name_Edit.setReadOnly(True)
        self.ui.output_singer_Edit.setReadOnly(True)
        self.ui.output_album_Edit.setReadOnly(True)
        self.ui.top_textEdit.setReadOnly(True)
        self.ui.comment_textEdit.setReadOnly(True)
        self.ui.lyrics_textEdit.setReadOnly(True)
        self.ui.comment_textEdit.setReadOnly(True)
        self.ui.textBrowser.setReadOnly(True)
        self.ui.textBrowser_2.setReadOnly(True)
        self.ui.seek_Button.clicked.connect(self.inpput)#搜索网易云
        self.ui.seek_Button_2.clicked.connect(self.inpput_qq)#搜索QQ音乐
        self.ui.download_Button.clicked.connect(self.download_music)  # 下载按钮
        self.ui.open_Button.clicked.connect(self.open_file)  # 打开保存音乐的文件夹
        self.ui.open_Button_2.clicked.connect(self.open_file)  # 打开保存音乐的文件夹
        self.ui.comment_pushButton.clicked.connect(self.look_comments)#查看评论
        self.ui.comment_pushButton_2.clicked.connect(self.in_excel)#生成excel文件
        self.ui.comment_pushButton_3.clicked.connect(self.open_excel)#打开excel文件
        self.ui.lyrics_pushButton.clicked.connect(self.lyrics)#查看歌词
        self.ui.lyrics_pushButton_2.clicked.connect(self.lyrics_T)#查看歌词时间版
        self.ui.comboBox.currentIndexChanged.connect(self.top)#排行榜
        self.ui.top_pushButton.clicked.connect(self.music_top_dowload)#下载排行榜里面的音乐




    def open_file(self):#打开文件夹
        try:
            os.startfile('Music')
        except FileNotFoundError:
            self.ui.show_label.setText('你还没下载呢！')

    def top(self):#网易云排行榜
        text = self.ui.comboBox.currentText()
        if text == "云音乐飙升榜":
            self.music_top("https://music.163.com/discover/toplist?id=19723756")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "云音乐新歌榜":
            self.music_top("https://music.163.com/discover/toplist?id=3779629")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "网易原创歌曲榜":
            self.music_top("https://music.163.com/discover/toplist?id=2884035")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "云音乐热歌榜":
            self.music_top("https://music.163.com/discover/toplist?id=3778678")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "云音乐说唱榜":
            self.music_top("https://music.163.com/discover/toplist?id=991319590")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "云音乐古典音乐榜":
            self.music_top("https://music.163.com/discover/toplist?id=71384707")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "云音乐电音榜":
            self.music_top("https://music.163.com/discover/toplist?id=1978921795")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "抖音排行榜":
            self.music_top("https://music.163.com/discover/toplist?id=2250011882")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "新声榜":
            self.music_top("https://music.163.com/discover/toplist?id=2617766278")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "云音乐ACG音乐榜":
            self.music_top("https://music.163.com/discover/toplist?id=71385702")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "云音乐韩语榜":
            self.music_top("https://music.163.com/discover/toplist?id=745956260")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "云音乐国电榜":
            self.music_top("https://music.163.com/discover/toplist?id=10520166")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "英国Q杂志中文版周榜":
            self.music_top("https://music.163.com/discover/toplist?id=2023401535")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "电竞音乐榜":
            self.music_top("https://music.163.com/discover/toplist?id=2006508653")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "UK排行榜周榜":
            self.music_top("https://music.163.com/discover/toplist?id=180106")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "美国Billboard周榜":
            self.music_top("https://music.163.com/discover/toplist?id=60198")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "Beatport全球电子舞曲榜":
            self.music_top("https://music.163.com/discover/toplist?id=3812895")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "KTV唛榜":
            self.music_top("https://music.163.com/discover/toplist?id=21845217")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "iTunes榜":
            self.music_top("https://music.163.com/discover/toplist?id=11641012")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "日本Oricon周榜":
            self.music_top("https://music.163.com/discover/toplist?id=60131")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "Hit FM Top榜":
            self.music_top("https://music.163.com/discover/toplist?id=120001")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "台湾Hito排行榜":
            self.music_top("https://music.163.com/discover/toplist?id=112463")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "云音乐欧美热歌榜":
            self.music_top("https://music.163.com/discover/toplist?id=2809513713")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "法国 NRJ Vos Hits 周榜":
            self.music_top("https://music.163.com/discover/toplist?id=27135204")
            self.ui.top_show_label.setText(f'《{text}》')
        elif text == "中国新乡村音乐排行榜":
            self.music_top("https://music.163.com/discover/toplist?id=3112516681")
            self.ui.top_show_label.setText(f'《{text}》')

    def music_top_dowload(self):#排行榜音乐下载
        try:
            num = int(self.ui.top_lineEdit.text())

            id_num = self.ui.top_id_Edit.toPlainText()
            id_info = id_num.split()

            name = self.ui.top_textEdit.toPlainText()
            name_info = re.findall(r'《(.*)》', name)

            song_id = id_info[num - 1]
            song_name = name_info[num - 1]
            song_url = f"http://music.163.com/song/media/outer/url?id={song_id}.mp3"

            os.makedirs("Music", exist_ok=True)
            path = "Music\%s.mp3" % song_name

            urlretrieve(song_url, path)
            self.ui.top_show_label.setText('下载完成！')
        except:
            self.ui.top_show_label.setText("你还没有输入序号哦！")

    def music_top(self,url):#网易云音乐排行榜显示
        self.ui.top_textEdit.clear()
        self.ui.top_id_Edit.clear()

        try:
            headers = {
                'authority': 'music.163.com',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'sec-fetch-dest': 'iframe',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'referer': 'https://music.163.com/',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'cookie': '_ga=GA1.2.1412864897.1553836840; _iuqxldmzr_=32; _ntes_nnid=b757609ed6b0fea92825e343fb9dfd21,1568216071410; _ntes_nuid=b757609ed6b0fea92825e343fb9dfd21; WM_TID=Pg3EkygrDw1EBAVUVRIttkwA^%^2Bn1s1Vww; P_INFO=183605463^@qq.com^|1581593068^|0^|nmtp^|00^&99^|null^&null^&null^#not_found^&null^#10^#0^|^&0^|^|183605463^@qq.com; mail_psc_fingerprint=d87488b559a786de4942ad31e080b75f; __root_domain_v=.163.com; _qddaz=QD.n0p8sb.xdhbv8.k75rl6g4; __oc_uuid=2f4eb790-6da9-11ea-9922-b14d70d91022; hb_MA-BFF5-63705950A31C_source=blog.csdn.net; UM_distinctid=171142b7a6d3ba-0fbb0bf9a78375-4313f6a-144000-171142b7a6e30b; vinfo_n_f_l_n3=6d6e1214849bb357.1.0.1585181322988.0.1585181330388; JSESSIONID-WYYY=jJutWzFVWmDWzmt2vzgf6t5RgAaMOhSIKddpHG9mTIhK8fWqZndgocpo87cjYkMxKIlF^%^2BPjV^%^2F2NPykYHKUnMHkHRuErCNerHW6DtnD8HB09idBvHCJznNJRniCQ9XEl^%^2F7^%^2Bovbwgy7ihPO3oJIhM8s861d^%^2FNvyRTMDjVtCy^%^5CasJPKrAty^%^3A1585279750488; WM_NI=SnWfgd^%^2F5h0XFsqXxWEMl0vNVE8ZjZCzrxK^%^2F9A85boR^%^2BpV^%^2BA9J27jZCEbCqViaXw6If1Ecm7okWiL^%^2BKU2G8frpRB^%^2BRRDpz8RNJnagZdXn6KNVBHwK2tnvUL^%^2BxWQ^%^2BhGf2aeWE^%^3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee84b64f86878d87f04fe9bc8fa3c84f878f9eafb65ab59498cccf48f7929fb5e72af0fea7c3b92a91b29987e670edeba8d1db4eb1af9899d64f8fb40097cd5e87e8968bd949baaeb8acae3383e8fb83ee5ae9b09accc4338aeef98bd94987be8d92d563a388b9d7cc6ef39bad8eb665a989a7adaa4197ee89d9e57ab48e8eccd15a88b0b6d9d1468ab2af88d9709cb2faaccd5e8298b9acb180aeaa9badaa74958fe589c66ef2bfabb8c837e2a3; playerid=67583529',
            }

            res = requests.get(url, headers=headers)
            res.encoding = res.apparent_encoding
            res.raise_for_status()
        except:
            self.ui.top_show_label.setText('网页提取出现问题！')
        text = res.text
        try:
            all = re.findall(r'<Ul Class="F-Hide">(.*?)</Ul>', text, re.I)
            str = all[0]
            strlist = re.findall(r'">(.*?)</a>', str)
            idlist = re.findall(r'\d+', str)
            for i in range(100):
                self.ui.top_textEdit.insertPlainText(f"{i+1} 《{strlist[i]}》\n")
                self.ui.top_id_Edit.insertPlainText(f"{idlist[i]}\n")
        except:
            self.ui.top_show_label.setText('提取文章出错！')


    def lyrics_T(self):#歌词显示

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        self.ui.lyrics_textEdit.clear()

        count = self.ui.output_index_Edit.toPlainText()
        count_list = count.split()
        if len(count_list)>10:
            id_num = self.ui.id_Edit.toPlainText()
            id_info = id_num.split()

            name = self.ui.output_name_Edit.toPlainText()
            name_info = name.split()

            d_num = int(self.ui.lyrics_Edit.text())
            song_name = name_info[d_num - 1]
            song_id = id_info[d_num - 1]

            lrc_url = f'http://music.163.com/api/song/lyric?id={song_id}&lv=1&kv=1&tv=-1'
            lyric = requests.get(lrc_url,headers = headers)
            json_obj = lyric.text  # 网页源码
            j = json.loads(json_obj)
            lrc = j['lrc']['lyric']
            # pat = re.compile(r'\[.*\]')
            # lrc = re.sub(pat, "", lrc)
            # lrc = lrc.strip()
            self.ui.lyrics_textEdit.insertPlainText(lrc)

            self.ui.lyrics_show_label.setText(f"《{song_name}》")
        elif 9<len(count_list)<20:
            self.ui.lyrics_show_label.setText("只支持网易云音乐哦！")
        else:
            self.ui.lyrics_show_label.setText("没有找到音乐信息,请先搜索吧！")

    def lyrics(self):#歌词显示 时间版
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        self.ui.lyrics_textEdit.clear()

        count = self.ui.output_index_Edit.toPlainText()
        count_list = count.split()
        if len(count_list) > 10:
            id_num = self.ui.id_Edit.toPlainText()
            id_info = id_num.split()

            name = self.ui.output_name_Edit.toPlainText()
            name_info = name.split()

            d_num = int(self.ui.lyrics_Edit.text())
            song_name = name_info[d_num - 1]
            song_id = id_info[d_num - 1]

            lrc_url = f'http://music.163.com/api/song/lyric?id={song_id}&lv=1&kv=1&tv=-1'
            lyric = requests.get(lrc_url,headers = headers)
            json_obj = lyric.text  # 网页源码
            j = json.loads(json_obj)
            lrc = j['lrc']['lyric']
            pat = re.compile(r'\[.*\]')
            lrc = re.sub(pat, "", lrc)
            lrc = lrc.strip()
            self.ui.lyrics_textEdit.insertPlainText(lrc)

            self.ui.lyrics_show_label.setText(f"《{song_name}》")
        else:
            self.ui.lyrics_show_label.setText("只支持网易云音乐哦！")

    def in_excel(self):#把评论写入excel
        headers = {
            'Host': 'music.163.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        """
        获取评论信息
        """
        id = self.ui.comment_id_Edit.toPlainText()
        name = self.ui.comment_name_textEdit.toPlainText()
        list_info_ct = []
        try:
            for page in range(0,1020,20):
                url = f'http://music.163.com/api/v1/resource/comments/R_SO_4_{id}?limit=20&offset=' + str(page)
                response = requests.get(url=url, headers=headers)
                # 将字符串转为json格式
                result = json.loads(response.text)
                items = result['comments']
                for item in items:
                    info = []
                    # 用户名
                    user_name = item['user']['nickname'].replace(',', '，')
                    # 评论内容
                    comment = item['content'].strip().replace('\n', '').replace(',', '，')
                    # 评论点赞数
                    praise = str(item['likedCount'])
                    # 评论时间
                    date = time.localtime(int(str(item['time'])[:10]))
                    date = time.strftime("%Y-%m-%d %H:%M:%S", date)
                    info.append(user_name)
                    info.append(praise)
                    info.append(date)
                    info.append(comment)
                    list_info_ct.append(info)
            book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建workbook对象
            sheet = book.add_sheet("网易云评论", cell_overwrite_ok=True)  # 创建工作表
            col = ("用户昵称","点赞数","发布时间","评论")
            for i in range(4):
                sheet.write(0, i, col[i])  # 列名
            for i in range(len(list_info_ct)):
                data = list_info_ct[i]
                for j in range(4):
                    sheet.write(i + 1, j, data[j])  # 数据
            book.save(f"{name}.xls")

            self.ui.comment_show_label.setText("生成完毕！")
        except KeyError:
            self.ui.comment_show_label.setText("没有找到音乐信息哦，请先搜索吧！")


    def open_excel(self):#打开excel文件
        try:
            name = self.ui.comment_name_textEdit.toPlainText()
            os.startfile(f'{name}.xls')
        except FileNotFoundError:
            self.ui.comment_show_label.setText("没有找到Excel文件哦，请先生成吧！")

    def singer_show(self,name,id):#评论部分信息显示
        self.ui.comment_id_Edit.clear()
        self.ui.comment_name_textEdit.clear()
        self.ui.comment_show_label.setText(f'《{name}》')
        self.ui.comment_id_Edit.insertPlainText(f'{id}')
        self.ui.comment_name_textEdit.insertPlainText(f'{name}')

    def look_comments(self):#查看网易云歌曲评论
        self.ui.comment_textEdit.clear()
        self.ui.comment_id_Edit.clear()
        self.ui.comment_name_textEdit.clear()
        try:
            count = self.ui.output_index_Edit.toPlainText()
            count_list = count.split()
            if len(count_list) > 10:
                id_num = self.ui.id_Edit.toPlainText()
                id_info = id_num.split()

                name = self.ui.output_name_Edit.toPlainText()
                name_info = name.split()

                d_num = int(self.ui.comment_Edit.text())
                song_name = name_info[d_num - 1]
                song_id = id_info[d_num - 1]
                self.output_comments(song_id)
                self.singer_show(song_name,song_id)
            elif 9<len(count_list)<20:
                self.ui.comment_show_label.setText("只支持网易云音乐哦！")
            else:
                self.ui.comment_show_label.setText("请先搜索音乐哦！")
        except ValueError:
            self.ui.comment_Edit.setText("序号在哪里？")

    def output_comments(self,id):#显示爬取的评论

        try:
            for i in range(0, 400, 20):
                self.ui.comment_textEdit.insertPlainText('---------------第 ' + str(i // 20 + 1) + ' 页---------------\n\n')
                list_info = self.get_comments(i,id)
                for j in range(20):
                    self.ui.comment_textEdit.insertPlainText(
                        f'评论:[ {list_info[j][1]} ]-----用户昵称:({list_info[j][0]})-----点赞数:{list_info[j][2]}-----时间:{list_info[j][3]}\n\n')
        except IndexError:
            self.ui.comment_textEdit.insertPlainText("---------------全部评论已经爬取完毕！---------------")

    def get_comments(self, page, id):
        headers = {
            'Host': 'music.163.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        """
        获取评论信息
        """
        url = f'http://music.163.com/api/v1/resource/comments/R_SO_4_{id}?limit=20&offset=' + str(page)
        response = requests.get(url=url, headers=headers)
        # 将字符串转为json格式
        result = json.loads(response.text)
        try:
            items = result['comments']
            list_info_ct = []
            for item in items:
                info = []
                # 用户名
                user_name = item['user']['nickname'].replace(',', '，')
                # 评论内容
                comment = item['content'].strip().replace('\n', '').replace(',', '，')
                # 评论点赞数
                praise = str(item['likedCount'])
                # 评论时间
                date = time.localtime(int(str(item['time'])[:10]))
                date = time.strftime("%Y-%m-%d %H:%M:%S", date)
                info.append(user_name)
                info.append(comment)
                info.append(praise)
                info.append(date)
                list_info_ct.append(info)
            return list_info_ct
        except KeyError:
            self.ui.show_label.setText('这不是网易云的歌哦！')

    def inpput_qq(self):#显示QQ音乐歌曲信息
        self.ui.id_Edit.clear()
        self.ui.show_label.setText('搜索完成！')
        self.ui.output_index_Edit.clear()
        self.ui.output_name_Edit.clear()
        self.ui.output_singer_Edit.clear()
        self.ui.output_album_Edit.clear()
        name = self.ui.input_Edit.text()
        name_z = parse.urlencode({'w': name})
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=63229658163010696&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&%s&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0' % (
            name_z)
        content = requests.get(url=url)
        text = content.text
        info_list = json.loads(text)
        song_list = info_list['data']['song']['list']
        # print(song_list)
        str_3 = '''https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey5559460738919986&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"1825194589","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"1825194589","songmid":["%s"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}'''

        music_info = []
        count = 1
        for i in range(len(song_list)):
            song = []
            song.append(song_list[i]['name'])
            song.append(song_list[i]['singer'][0]['name'])
            song.append(song_list[i]['album']['title'])
            song.append(str_3 % (song_list[i]['mid']))
            music_info.append(song)
        try:
            for i in range(10):
                self.ui.output_index_Edit.insertPlainText(f" 音悦{count}\n")
                self.ui.output_name_Edit.insertPlainText(f" {music_info[i][0]}\n")
                self.ui.output_singer_Edit.insertPlainText(f" {music_info[i][1]}\n")
                if len(music_info[i][2]) > 13:
                    self.ui.output_album_Edit.insertPlainText(f"《{music_info[i][2][0:12]+'...'}》\n")
                else:
                    self.ui.output_album_Edit.insertPlainText(f"《{music_info[i][2]}》\n")
                self.ui.id_Edit.insertPlainText(f"{music_info[i][3]}\n")
                count += 1
        except:
            self.ui.output_index_Edit.clear()
            self.ui.show_label.clear()
            self.ui.input_Edit.setText("请输入歌曲名或歌手名！！！")

    def inpput(self):#显示网易云音乐
        self.ui.id_Edit.clear()
        self.ui.show_label.setText('搜索完成！')
        self.ui.output_index_Edit.clear()
        self.ui.output_name_Edit.clear()
        self.ui.output_singer_Edit.clear()
        self.ui.output_album_Edit.clear()
        name = self.ui.input_Edit.text()

        url = "https://music.zhuolin.wang/api.php?callback=Java_S100764385210076438510076438521007643"
        data = {
            'types': 'search',
            'count': '20',
            'source': 'netease',
            'pages': '1',
            'name': name
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }


        list_info = self.musicSpider(url, data, headers)
        count = 1



        for i in range(len(list_info)):
            self.ui.output_index_Edit.insertPlainText(f" 音悦{count}\n")

            if len(list_info[i][1])>20:
                self.ui.output_name_Edit.insertPlainText(f" {list_info[i][1][0:15]+'...'}\n")
            else:
                self.ui.output_name_Edit.insertPlainText(f" {list_info[i][1]}\n")

            self.ui.output_singer_Edit.insertPlainText(f" {list_info[i][2]}\n")
            if len(list_info[i][3]) > 13:
                self.ui.output_album_Edit.insertPlainText(f"《{list_info[i][3][0:12]+'...'}》\n")
            else:
                self.ui.output_album_Edit.insertPlainText(f"《{list_info[i][3]}》\n")
            self.ui.id_Edit.insertPlainText(f"{list_info[i][0]}\n")

            count += 1


    def musicSpider(self,url, data, headers):#网易云音乐爬取
        rsp = requests.post(url, data=data, headers=headers)
        content = rsp.text
        info = content[content.index('('):content.index('])')] + '])'
        info_list = eval(info[1:-1])
        music_info_list = []
        for i in info_list:
            id = i.get('id')
            name = i.get('name')
            artist = i.get('artist')
            album = i.get('album')
            info_info = []
            info_info.append(id)
            info_info.append(name.replace(' ', ''))
            info_info.append(artist[0])
            info_info.append(album.replace(' ', ''))
            music_info_list.append(info_info)
        return music_info_list

    def download_music(self):#音乐下载
        count = self.ui.output_index_Edit.toPlainText()
        count_list = count.split()
        try:
            if len(count_list)>10:
                id_num = self.ui.id_Edit.toPlainText()
                id_info = id_num.split()

                name = self.ui.output_name_Edit.toPlainText()
                name_info = name.split()

                d_num = int(self.ui.input_Edit_2.text())


                song_id = id_info[d_num - 1]
                song_name = name_info[d_num - 1]
                song_url = f"http://music.163.com/song/media/outer/url?id={song_id}.mp3"

                os.makedirs("Music",exist_ok=True)
                path = "Music\%s.mp3"%song_name

                urlretrieve(song_url,path)
                self.ui.show_label.setText('下载完成！')

            elif 2<len(count_list)<11:
                id_num = self.ui.id_Edit.toPlainText()
                id_info = id_num.split()

                name = self.ui.output_name_Edit.toPlainText()
                name_info = name.split()

                d_num = int(self.ui.input_Edit_2.text())

                song_id = id_info[d_num - 1]
                song_name = name_info[d_num - 1]

                content_json = requests.get(url=song_id)

                dict_2 = json.loads(content_json.text)

                url_ip = dict_2['req']['data']['freeflowsip'][1]

                purl = dict_2['req_0']['data']['midurlinfo'][0]['purl']

                download = url_ip + purl
                try:
                    os.makedirs("Music", exist_ok=True)
                    path = "Music\%s.mp3" % song_name
                    urlretrieve(download, path)
                    self.ui.show_label.setText('下载完成！')
                except Exception:
                    self.ui.show_label.setText('这首难搞哦！')
        except:
            self.ui.input_Edit_2.setText("请先搜索音乐")

if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('./Image/song.png'))
    music_dowload = Music_Dowload()
    music_dowload.ui.show()
    app.exec_()