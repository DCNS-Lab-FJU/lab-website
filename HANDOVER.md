# DCNS Lab 網站交接文件（最小可交付版）

## 1) 專案總覽

- 框架：Hugo + PaperMod
- 部署：GitHub Pages（project site）
- 網址：https://dcns-lab-fju.github.io/lab-website/
- Repository：DCNS-Lab-FJU/lab-website

本網站使用 project-site 子路徑（`/lab-website/`）。
內容中的連結不要手動硬寫 `"/lab-website/"`。

---

## 2) 本機開發

### 需求環境

- Hugo Extended（建議最新版）
- Git

### 本機啟動

```bash
hugo server -D
```

本機預覽網址通常是：

```text
http://localhost:1313/lab-website/
```

### 正式建構檢查

```bash
hugo --minify
```

建構輸出在 `public/`，不應提交到 git。

---

## 3) 內容結構

```text
content/
  _index.md
  members/
    _index.md
    faculty/
      _index.md
      lu-shu-ping.md
    students/
      _index.md
      student-template.md
      m-xxx-xxx.md
    alumni/
      _index.md
      m-xxx-xxx.md
  publications/
    _index.md

static/
  images/
    members/
  files/
    students/
```

---

## 4) 新增或更新成員

### 新增教師（Faculty）

1. 在 `content/members/faculty/` 新增檔案。
2. 填寫 front matter 與頁面內容。
3. 照片放在 `static/images/members/`。
4. 用 shortcode 插入圖片：

```markdown
{{< img src="images/members/example.jpg" alt="Example" w="220" >}}
```

### 新增學生（Students）

1. 複製 `content/members/students/student-template.md` 成新檔。
2. 填寫欄位與內容。
3. PDF 檔放在 `static/files/students/<student-id>/`。
4. 用 shortcode 連結檔案：

```markdown
{{< filelink path="files/students/<student-id>/report.pdf" text="Project Report" >}}
```

---

## 5) 新增 Publications

編輯 `content/publications/_index.md`。

每筆建議使用固定格式：

```markdown
- **Year:** 2026  
  **Authors:** A, B, C  
  **Title:** Paper title  
  **Venue:** Conference/Journal  
  **Link:** https://...
```

章節建議維持：

- Journal Articles
- Conference Papers
- Patents
- Technical Reports

這樣未來要轉 YAML / BibTeX 會比較容易。

---

## 6) 路徑與連結規則（Project Site 安全）

### 站內頁面連結

使用 `relref`：

```markdown
[Members]({{< relref "/members/_index.md" >}})
```

### 靜態檔案連結

使用 `filelink` shortcode（內部用 `relURL`）：

```markdown
{{< filelink path="files/students/demo/report.pdf" text="Project Report" >}}
```

### 不要這樣做

- 不要手寫 `/lab-website/...`
- 不要在 Markdown 直接用根路徑 `/members/` 這類寫法

---

## 7) Mandatory Credits

Credits 目前在 `hugo.toml` 的 `params.footer.text` 設定。

Last Updated 由 `layouts/partials/extend_footer.html` 使用頁面的 `Lastmod` 顯示。

已啟用 `enableGitInfo = true`，可提升最後更新時間的可靠度。

---

## 8) 部署流程

GitHub Actions workflow：

- `.github/workflows/pages.yml`

流程：

1. Push 到 `main`
2. Action 建構 Hugo 網站
3. 部署到 GitHub Pages

若部署失敗，優先檢查：

- Hugo 版本
- baseURL
- 相對路徑是否失效
- submodule 是否正確 checkout

---

## 9) 常見問題

1. **部署後 404**
   多半是路徑被手寫成 root 路徑。
2. **圖片不顯示**
   確認圖片放在 `static/images/...` 並使用 shortcode。
3. **PDF 連結失效**
   確認檔案在 `static/files/...` 並使用 `filelink`。
4. **Members 首頁顯示不想要的卡片**
   `content/members/_index.md` 應使用 `layout: "members-home"`。

---

## 10) PR 維護 SOP（建議）

每次成員更新 PR 建議：

1. 一個 PR 只處理一件主題（成員或 publication）
2. 只包含必要 Markdown 與資產檔案
3. Reviewer 檢查清單：
   - 連結可開啟
   - 圖片 / PDF 路徑正確
   - 沒有硬寫 `/lab-website/`
   - `hugo --minify` 在本機或 CI 通過

---

## 11) 後續升級規劃（非立即）

1. Publications 轉為資料驅動（YAML / BibTeX）
2. 補 members / publications 搜尋
3. 新增 CSV/Excel 匯出腳本（Python）
4. 大型 PDF / 投影片改放 GitHub Releases，網站保留索引與連結
