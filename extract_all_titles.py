#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提取所有53个案例的标题
"""

import re

source_file = 'source_file/中国法院2025年度案例_婚姻家庭与继承纠纷.md'

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 查找目录部分（从"## 目 录"到"## 一、婚姻家庭纠纷"）
dir_start = content.find('## 目 录 Contents')
dir_end = content.find('## 一、婚姻家庭纠纷')

if dir_start == -1 or dir_end == -1:
    print("无法找到目录部分")
    exit(1)

dir_content = content[dir_start:dir_end]

# 提取所有案例编号和标题
# 格式可能是：
# 1. 标题 页码
# 2. 标题 ——当事人 页码
case_pattern = r'^(\d+)\.\s+([^\n]+?)(?:\s+——[^\n]+?)?\s+\d+\s*$'
matches = re.findall(case_pattern, dir_content, re.MULTILINE)

print(f"找到 {len(matches)} 个案例\n")

case_title_map = {}
for match in matches:
    case_num = int(match[0])
    case_title = match[1].strip()
    # 清理标题
    case_title = re.sub(r'\s+', ' ', case_title)
    # 移除可能的"——"和当事人信息
    if '——' in case_title:
        case_title = case_title.split('——')[0].strip()
    case_title_map[case_num] = case_title
    print(f"{case_num}. {case_title}")

print(f"\n总共提取到 {len(case_title_map)} 个案例标题")

