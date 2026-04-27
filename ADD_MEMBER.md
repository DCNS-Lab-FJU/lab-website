# 新增 / 更新成員 SOP

> 本指南適用於想**更新個人頁面**或**新增成員**的人，不需要懂 Hugo 或程式。  
> 技術開發細節請見 [HANDOVER.md](HANDOVER.md)。

---

## 方法一：只更新個人資料（最簡單，不需安裝任何工具）

1. 前往 https://github.com/DCNS-Lab-FJU/lab-website
2. 點進 `content/members/students/`，找到你的 `m-xxx-xxx.md` 檔案
3. 點右上角的 **鉛筆圖示（Edit this file）**
4. 修改你想更新的內容（研究方向、聯絡資訊、照片路徑等）
5. 畫面最下方 → **Propose changes** → 填寫說明（例如：`update: 更新 王小明 個人資料`）
6. 點 **Create pull request**
7. 等管理員（廷宇）審核合併即可

---

## 方法二：新增全新成員（腳本自動建檔）

適合**維護者**幫新人建立頁面，或新人自己有設定好開發環境。

```bash
python scripts/new_member.py
```

腳本會互動式詢問：
- 姓名
- 身份別（PhD / MS / 大學生 / 畢業生）
- 入學年度
- Email
- GitHub 帳號

自動產生格式正確的 `.md` 檔到 `content/members/students/`（或 `alumni/`）。

產生後，依方法三提交 PR。

---

## 方法三：本機編輯後 Push（想先在本機預覽）

```bash
# 1. Clone repo（第一次才需要）
git clone https://github.com/DCNS-Lab-FJU/lab-website.git
cd lab-website

# 2. 建立自己的分支
git checkout -b update/your-name-profile

# 3. 編輯或新增你的 md 檔，儲存後預覽
hugo server -D
# 瀏覽器開 http://localhost:1313/lab-website/

# 4. 確認沒問題後提交
git add content/members/students/m-xxx-xxx.md
git commit -m "update: 更新 姓名 個人資料"
git push origin update/your-name-profile

# 5. 在 GitHub 開 Pull Request，指定 Reviewer 為廷宇
```

---

## 如何加上照片

1. 將照片命名為 `your-name.jpg`（建議 400×400 px 以上，正方形）
2. 放到 `static/images/members/your-name.jpg`
3. 在你的 `.md` front matter 填入：

```yaml
avatar: "images/members/your-name.jpg"
```

沒有填 `avatar` 的成員，網站會自動顯示名字首字母圓形圖示。

---

## 審核清單（管理員用）

合併 PR 前確認：
- [ ] CI（GitHub Actions）建構通過
- [ ] 照片路徑正確（`images/members/xxx.jpg`）
- [ ] 沒有硬寫 `/lab-website/...` 路徑
- [ ] front matter 格式完整（`title`, `role`, `year`, `category`, `avatar`, `draft: false`）
