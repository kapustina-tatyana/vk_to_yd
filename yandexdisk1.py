
import requests
import os

# name = os.path.basename(path_to_file)
# print(name)


class YaUpload:
    def __init__(self, token: str):
        self.token = token
        self.host = "https://cloud-api.yandex.net"
        self.headers = {"Content-Type": "application/json",
                        "Authorization": f"OAuth {self.token}"
                        }

    def get_link(self, path):
        url = f"{self.host}/v1/disk/resources/upload/"
        headers = self.headers
        params = {"path": path, "overwrite": True}
        response = requests.get(url, params=params, headers=headers)
        return response.json()["href"]

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_link = self.__get_link(os.path.basename(path_to_file))
        response = requests.put(upload_link, data=open(
                file_path, "rb"), headers=self.headers)
        if response.status_code == 201:
            print("Completed")


if __name__ == '__main__':
    path_to_file = "/home/ismoilov_m_f/Python/qwer.py"
    token = "AQAAAABYkyT0AADLW1nIumRgkEmRiaLby5adORg"
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
    # print(uploader._get_link(path_to_file))