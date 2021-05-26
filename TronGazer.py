import re
import requests


class TronGazer:
    apiPrev = 'https://ilearn.ttu.edu.tw/api/'

    def __init__(self):
        self.session = requests.session()
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36"
        }
        self.session.headers.update(headers)

    def login_ttu(self, uid: str, password: str) -> bool:
        # 設定好登入資訊
        login_info = {
            "ID": uid,
            "PWD": password,
            "Submit": "%B5n%A4J%A8t%B2%CE",  # 登入系統
        }
        r = self.session.post(
            'https://stucis.ttu.edu.tw/login.php', data=login_info)

        self.check_login = self.session.get(
            'https://stucis.ttu.edu.tw/menu/TronClass.php')

        if self.check_login.text == 'Not login or session expire!':
            return False
        return True

    def getUserInfo(self):
        self.userName = re.findall(
            '<root-scope-variable name="currentUserName" value="(.*)"></root-scope-variable>', self.check_login.text)[0]
        self.userId = re.findall(
            'id="userId" data-id="(\d+)"', self.check_login.text)[0]

    def getAllCourse(self):
        r = self.session.get('%susers/%s/courses' %
                             (TronGazer.apiPrev, self.userId))
        course_list = r.json()
        self.all_course = [{
            'id': i['id'],
            'name': i['name']
        } for i in course_list['courses']]

    def getVideos(self, cid: int):
        action_json_url = '%scourses/%s/activities' % (TronGazer.apiPrev, cid)
        r = self.session.get(action_json_url)
        course_resources = r.json()
        videos = []
        video_iter = filter(lambda i: i['type'] == "online_video",
                            course_resources['activities'])
        # Tronclass上的影片分為兩種，一種是上傳至Tronclass，另一種為外部影片(Youtube)
        # 因此影片長度的儲存位置就被放到不同地方
        # 1. 上傳至Tronclass的影片
        # 影片資訊會放在uploads欄位，而影片會被系統重新編碼為不同解析度
        # 所以uploads裡可能會有多個影片檔，但實為同一部影片
        # 因此找index=0的影片資訊即可
        # 2. 連結至Youtube的影片
        # Tronclass僅把Youtube影片的標題與片長放在data欄位，直接讀取即可
        for v in video_iter:
            # 讀取影片片長
            if len(v['uploads']) == 0:
                # 自己測試時，點選舊課程發現若影片連結至yt時，該影片已被下架，則會缺少片長欄位
                # 既然影片無法觀看，直接跳過該部影片
                if 'duration' not in v['data']:
                    continue
                duration = v['data']['duration']
            else:
                # 依yt影片的方式，假定影片被教師刪除之類的因素，但不確定欄位的存放狀態，因此以try做處理
                try:
                    duration = v['uploads'][0]['videos'][0]['duration']
                except:
                    continue
            videos.append({
                'id': v['id'],
                'title': v['title'],
                'duration': duration
            })
        self.videos = videos

    def watchVideo(self, video):
        self.session.post('%scourse/activities-read/%d' %
                          (TronGazer.apiPrev, video['id']),
                          json={
                              "start": 0,
                              "end": video['duration']
                          })
