# jd
京东商品详情+评论爬虫（Scrapy、Redis）

基于Python+scrapy+redis+mongodb的分布式爬虫实现框架

scrapy runspider jdredisurl.py 主要功能是抓取种子url，保存到redis

scrapy runspider jdmongodb.py 主要是从redis里面读url，解析数据保存到mongodb （拓展到其他机器,修改REDIS_HOST = "主机ip"，都是从redis里面读url,MONGODB_HOST = "存储服务器ip"）

middlewares.ProxyMiddleware 使用阿布云代理服务器轮换请求IP

每页60条数据，源码仅有30条，解决下拉时刷新的剩余30条数据抓取。
