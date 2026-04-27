#!/usr/bin/env python3
"""
new_member.py — 互動式新增成員 Markdown 檔案
用法：python scripts/new_member.py
輸出：content/members/{students|alumni}/m-{lastname}-{firstname}.md
"""

import os
import re
import sys
from pathlib import Path
from datetime import date

# ── 路徑設定 ────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent
MEMBERS_DIR = REPO_ROOT / "content" / "members"

CATEGORIES = {
    "1": ("students", "PhD Student"),
    "2": ("students", "MS Student"),
    "3": ("students", "Undergraduate Student"),
    "4": ("alumni",   "Alumni"),
}

TEMPLATE = """\
---
title: "{full_name}"
role: "{role}"
year: {year}
category: "{category_folder}"
email: "{email}"
github: "{github}"
avatar: ""  # 照片路徑，例如 images/members/your-photo.jpg
draft: false
---

## Research Topic

<!-- 一到兩句話描述研究方向 -->

## Additional Information

<!-- 學術背景、研究興趣等 -->

## Contact

- Email: {email}
"""


def slugify(text: str) -> str:
    """轉換為小寫 kebab-case 合法檔名"""
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    return text


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt}{suffix}: ").strip()
    return value if value else default


def main():
    print("=" * 50)
    print("  DCNS Lab 新增成員工具")
    print("=" * 50)

    # 身份別
    print("\n身份別：")
    for key, (_, role) in CATEGORIES.items():
        print(f"  {key}. {role}")
    cat_key = ask("請選擇", "2")
    if cat_key not in CATEGORIES:
        print(f"無效選項 '{cat_key}'，請重新執行。")
        sys.exit(1)
    category_folder, role = CATEGORIES[cat_key]

    # 基本資料
    print()
    full_name = ask("全名（英文，例如 Ming-Xiao Wang）")
    if not full_name:
        print("姓名不能為空。")
        sys.exit(1)

    github    = ask("GitHub 帳號（可留空）", "")
    email     = ask("Email（可留空）", "")
    year      = ask("入學/加入年度（西元，例如 2025）", str(date.today().year))

    # 檔名
    slug_default = "m-" + slugify(full_name)
    slug = ask(f"檔名（不含 .md，建議 m-lastname-firstname）", slug_default)

    output_dir  = MEMBERS_DIR / category_folder
    output_path = output_dir / f"{slug}.md"

    output_dir.mkdir(parents=True, exist_ok=True)

    if output_path.exists():
        overwrite = ask(f"檔案已存在：{output_path}\n覆寫？(y/N)", "N")
        if overwrite.lower() != "y":
            print("已取消。")
            sys.exit(0)

    content = TEMPLATE.format(
        full_name=full_name,
        role=role,
        year=year,
        category_folder=category_folder,
        email=email,
        github=github,
    )

    output_path.write_text(content, encoding="utf-8")

    print(f"\n✓ 已建立：{output_path.relative_to(REPO_ROOT)}")
    print("\n後續步驟：")
    print("  1. 開啟檔案填寫研究方向、個人簡介")
    print(f"  2. 如有照片，複製到 static/images/members/{slug}.jpg")
    print(f"     並在 front matter 填入：avatar: \"images/members/{slug}.jpg\"")
    print("  3. git add → git commit → git push → 在 GitHub 開 Pull Request")


if __name__ == "__main__":
    main()
