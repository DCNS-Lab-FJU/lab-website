# DCNS Lab Website

- **Live site**: https://dcns-lab-fju.github.io/lab-website/
- **Framework**: Hugo + PaperMod
- **Deployment**: GitHub Pages (auto-deploy on push to `main`)

開發維護細節請見 [HANDOVER.md](HANDOVER.md)。

---

## 目錄

- [更新個人頁面](#更新個人頁面)
- [新增全新成員](#新增全新成員)
- [加上照片](#加上照片)
- [上傳檔案並在個人頁面顯示 Resources 連結](#上傳檔案並在個人頁面顯示-resources-連結)
- [審核清單（管理員）](#審核清單管理員)

---

## 更新個人頁面

### 方法 A：在 GitHub 網頁直接編輯（最簡單，不需安裝任何工具）

1. 前往 https://github.com/DCNS-Lab-FJU/lab-website
2. 點進 `content/members/students/`，找到你的 `m-xxx-xxx.md` 檔案
3. 點右上角的 **鉛筆圖示（Edit this file）**
4. 修改內容（研究方向、聯絡資訊等）
5. 畫面最下方 → **Propose changes** → 填寫說明（例如：`update: 更新 王小明 個人資料`）
6. 點 **Create pull request**
7. 等管理員（廷宇）審核合併

### 方法 B：本機編輯後 Push（想先在本機預覽）

```bash
# 第一次 clone
git clone https://github.com/DCNS-Lab-FJU/lab-website.git
cd lab-website

# 建立自己的分支
git checkout -b update/your-name-profile

# 編輯 md 檔，儲存後預覽
hugo server -D
# 瀏覽器開 http://localhost:1313/lab-website/

# 確認後提交
git add content/members/students/m-xxx-xxx.md
git commit -m "update: 更新 姓名 個人資料"
git push origin update/your-name-profile

# 在 GitHub 開 Pull Request，指定 Reviewer 為廷宇
```

---

## 新增全新成員

### 選項一：執行腳本自動建檔（推薦）

```bash
python scripts/new_member.py
```

腳本互動式詢問姓名、身份別、年度、Email、GitHub 帳號，自動產生格式正確的 `.md` 檔。

### 選項二：手動複製模板

複製 `content/members/students/student-template.md`，填寫所有欄位後提交 PR。

---

## 加上照片

1. 將照片命名為 `your-name.jpg`（建議 400×400 px 以上，正方形）
2. 放到 `static/images/members/your-name.jpg`
3. 在你的 `.md` front matter 填入：

```yaml
avatar: "images/members/your-name.jpg"
```

沒有填 `avatar` 的成員，網站會自動顯示名字首字母圓形圖示。

---

## 上傳檔案並在個人頁面顯示 Resources 連結

> 論文 PDF、投影片、程式碼壓縮包等大型檔案，**不要直接放進 git repo**，請用 GitHub Releases 上傳，再把連結放到你的個人頁面。網站成員卡片會自動出現 📄 Resources 按鈕。

### 步驟一：上傳檔案到 GitHub Releases

1. 前往 https://github.com/DCNS-Lab-FJU/lab-website/releases
2. 點右上角 **Draft a new release**
3. **Choose a tag** → 輸入 `files-yourname-2026` → 點 **Create new tag**
4. **Release title** → 填說明，例如 `Wang Xiaoming — Thesis & Slides`
5. 拖曳你的 PDF / 投影片到 **Attach binaries** 區塊
6. 點 **Publish release**

> 之後想加新檔案：找到你的 Release → 點 **Edit（鉛筆圖示）** → 上傳新檔案 → **Update release**。  
> 不需要建新 tag，同一個 Release 可以放多個檔案。

### 步驟二：複製下載連結

發佈後在 Assets 區塊找到你的檔案，**右鍵 → 複製連結網址**：

```
https://github.com/DCNS-Lab-FJU/lab-website/releases/download/files-yourname-2026/thesis.pdf
```

> ⚠️ 連結裡的檔名必須和上傳的檔名**完全一致**，否則會 404。

### 步驟三：在個人頁面加 Resources 欄位

在你的 `.md` front matter 加入 `resources` 欄位（填 Release 頁面的網址）：

```yaml
---
title: "王小明"
role: "MS Student"
year: "115"
category: "研究生"
avatar: ""
resources: "https://github.com/DCNS-Lab-FJU/lab-website/releases/tag/files-wang-xiaoming-2026"
draft: false
---
```

儲存後，成員卡片底部會自動出現 **📄 Resources** 按鈕，點了會連到你的 Release 頁面，訪客可以從那裡下載所有檔案。

### 也可以在頁面內文直接貼連結

```markdown
## Research Topic / Project
智慧中醫: AI視覺

[專題報告 PDF](https://github.com/DCNS-Lab-FJU/lab-website/releases/download/files-wang-xiaoming-2026/report.pdf)

[簡報投影片](https://github.com/DCNS-Lab-FJU/lab-website/releases/download/files-wang-xiaoming-2026/slides.pdf)
```

### Tag 命名建議

| 情境 | 建議 tag |
|---|---|
| 個人所有資料 | `files-yourname-2026` |
| 某篇論文補充資料 | `paper-icassp2026-supp` |
| 某年度共用資源 | `resources-2026` |

---

## 審核清單（管理員）

合併 PR 前確認：
- [ ] CI（GitHub Actions）建構通過
- [ ] 照片路徑正確（`images/members/xxx.jpg`）
- [ ] 沒有硬寫 `/lab-website/...` 路徑
- [ ] front matter 格式完整（`title`, `role`, `year`, `category`, `avatar`, `draft: false`）
- [ ] `resources` 連結可正常開啟（若有填寫）
