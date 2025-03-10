"""
MIT License

Copyright (c) 2025 Jason Sun

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
from dotenv import load_dotenv

# 加载环境变量（如果有.env文件）
load_dotenv()

# 强制设置EVENT_FOLDER环境变量
os.environ["EVENT_FOLDER"] = "AIevents"

# API相关配置
API_KEY = os.getenv("R1_API_KEY", "")  # 从环境变量获取API密钥
API_ENDPOINT = os.getenv("R1_API_ENDPOINT", "")  # 从环境变量中获取ENDPOINT

# Obsidian仓库配置
OBSIDIAN_VAULT_PATH = os.getenv("OBSIDIAN_VAULT_PATH", "")  # Obsidian仓库路径
EVENT_FOLDER = os.getenv("EVENT_FOLDER", "AIevents")  # 事件文件夹名称

# 模型配置
MODEL_NAME = "deepseek-ai/DeepSeek-V3"  # 官方模型名称
MAX_TOKENS_PER_REQUEST = 1000  # 单次请求最大token数量
MAX_TOKENS_TOTAL = 5000  # 总共允许生成的最大token数量

# 请求配置
REQUEST_TIMEOUT = 60  # 请求超时时间（秒）
RETRY_ATTEMPTS = 3  # 重试次数

# 日志配置
LOG_FILE = "event_bot.log"
