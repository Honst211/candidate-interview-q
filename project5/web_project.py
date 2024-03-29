"""
5. 并发处理实现
假设你负责开发一个Web服务的后端，该服务需要处理来自客户端的大量请求。每个请求将执行以下操作之一：

1.数据检索：从某个API获取数据，这个操作可能需要一些时间来完成。
2.数据处理：对检索到的数据进行一些计算密集型的处理。
3.日志记录：将处理结果记录到日志文件中。 由于请求量很大，你需要利用Python的多并发特性来优化这三个操作的执行，以提高系统的吞吐量和响应能力。
任务要求

1.设计一个多并发解决方案：根据上述操作的特点，使用Python编写一个多并发的解决方案。你可以选择使用线程（threading）、进程（multiprocessing）或异步（asyncio）中的一种或几种方法来实现。
2.解决方案说明：解释你的设计选择。你为何选择特定的并发模型？考虑到操作的特性（如CPU密集型、IO密集型等），这种选择有何优势？
3.异常处理：展示在你的解决方案中如何处理可能出现的异常情况，例如API请求失败、数据处理错误等。
4.性能考虑：讨论你的解决方案可能面临的性能瓶颈以及可能的优化方法。
"""

# =========================================================================================================

"""
先说明思路:
1.数据检索 数据检索从API中获取数据，一般用于爬虫之类的系统，可以使用async来进行处理，因为这个操作可能需要一些时间来完成，使用async可以在等待数据到达前，执行其他任务
2.数据处理 数据处理是计算密集型操作，一般用于较为复杂的计算等处理，当数据量非常大且服务器属于多核心的时候，这里应该考虑多进程来进行处理，在python中使用多进程
可以保证多个核心都可以利用起来
3.日志记录 日志记录其实是IO密集的操作，一般也是用于爬虫系统，为了避免阻塞主线程或过多的IO操作，可以采用异步的方式来进行日志记录，可以利用异步IO库asyncio来实现异步日志记录

在当前云原生的架构之下，利用pod + Beanie + async的方式处理其实是更加理想的。

个人在设计这种系统的时候不是很喜欢使用多线程的方式，从理论上说使用多线程来处理数据检索（从某个API获取数据）是一个不错的选择。
由于数据检索通常是IO密集型的操作，而不是CPU密集型的操作，因此可以使用多线程来并发执行多个数据检索操作，从而提高系统的吞吐量和响应能力。
但是个人在实际项目测试中的表现来看，多线程的收益很低，而且还存在线程切换等性能损耗，个人在设计这种系统时不喜欢使用多线程来进行这种处理。

PS: 本题回答将利用喜马拉雅的数据爬取作为demo进行回答
"""

import time
import threading

import asyncio
import aiohttp
import aiofiles
from concurrent.futures import ProcessPoolExecutor


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}
base_url = "https://www.ximalaya.com"
timeout = 10


class XimalayaDownloader:
    def __init__(self):
        # 专辑api接口
        self.albumId_url = "https://www.ximalaya.com/revision/album/v1/getTracksList"
        # 音频下载api接口
        self.soundapi_url = (
            "https://mobile.ximalaya.com/mobile-playpage/track/v3/baseInfo"
        )

    async def get_album_tracks_list(
        self, session: aiohttp.ClientSession, album_id, page_num
    ):
        """
        获取专辑列表
        """
        params = {"albumId": album_id, "pageNum": page_num}

        async with session.get(
            self.albumId_url, headers=headers, params=params
        ) as response:
            album_tracks_list = await response.json(
                content_type="text/plain", encoding="utf-8"
            )
            return album_tracks_list

    async def process_data(self, data):
        await asyncio.sleep(2)  # 模拟处理延迟
        return f"处理后的数据: {data}"

    def process_data_sync(self, data):
        # 这里将协程方法转换为普通方法
        loop = asyncio.get_event_loop()
        processed_data = loop.run_until_complete(self.process_data(data))
        return processed_data

    async def process_data_multiprocessing(self, data):
        with ProcessPoolExecutor() as pool:
            processed_data = await asyncio.get_running_loop().run_in_executor(pool, self.process_data_sync, data)
        return processed_data

    async def save_log(self, content: str, log_filename, output_path):
        """
        保存日志
        """
        async with aiofiles.open(f"{output_path}/{log_filename}", "a") as f:
            await f.write(content)
            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            await f.write(f"\n创建时间: {now}\n")
            print(f"日志文件 {log_filename} 保存完成!")


async def main():
    downloader = XimalayaDownloader()

    # 创建一个AIOHTTP客户端会话
    async with aiohttp.ClientSession() as session:
        # 模拟获取专辑列表
        album_id = 123456  # 专辑ID
        page_num = 1  # 页码
        album_tracks_list = await downloader.get_album_tracks_list(session, album_id, page_num)

        # 并行处理专辑列表中的数据
        tasks = []
        for data in album_tracks_list:
            task = asyncio.create_task(downloader.process_data_multiprocessing(data))
            tasks.append(task)

        # 等待所有任务完成
        processed_data_list = await asyncio.gather(*tasks)

        # 打印处理后的数据
        for processed_data in processed_data_list:
            print(processed_data)


"""
从理论上来讲，web项目的满足wsgi协议，多用户并发请求时是多线程的这种类型，这里就不在外面套一层web的壳子，直接用多线程来进行模拟。
问题4：性能考虑
一般而言，压力来源于CPU密集处理在单机结构下难以扩容，性能跑满之后，难以继续提升，采用云原生的pod + Beanie + async效果其实会更好，
在架构层面可以做到随时忙时扩容，闲时缩容等方面设计
"""


def run_multiple_main():
    threads = [threading.Thread(target=asyncio.run, args=(main(),)) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    t1 = time.time()
    # 运行主函数
    run_multiple_main()
    print(f"总共耗时: {time.time() - t1}")
