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

論文資料統一存放在 `data/publications.yaml`，網站頁面自動讀取輸出。

**新增一篇論文的步驟：**

1. 開啟 `data/publications.yaml`
2. 在對應章節（`journal_articles` 或 `conference_papers`）新增一筆：

```yaml
- year: 2026
  authors: "Author A, Author B"
  title: "Paper Title"
  venue: "Conference or Journal Name"
  link: "https://doi.org/..."   # 無連結可省略此行
```

3. `hugo --minify` 確認建構成功後 push。

**不需要** 修改任何 HTML 模板或 `content/publications/_index.md`。

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

## 11) 大型檔案分流 SOP（GitHub Releases）

**原則**：PDF 投影片、影片、大型資料集不放在 git repo，改放 GitHub Releases，網站只保留連結。

**步驟：**

1. 到 GitHub Repository 頁面 → **Releases** → **Draft a new release**
2. 建立新 tag（例如 `files-2026`），上傳大型檔案
3. 複製下載連結（格式：`https://github.com/DCNS-Lab-FJU/lab-website/releases/download/<tag>/<filename>`）
4. 在成員頁面或 publications 中使用一般 Markdown 連結：

```markdown
[Thesis PDF](https://github.com/DCNS-Lab-FJU/lab-website/releases/download/files-2026/thesis.pdf)
```

**不要這樣做：**
- 不要把 PDF/影片直接 commit 進 `static/files/` 超過 10 MB
- 不要使用 Git LFS（會增加複雜度）

---

## 12) 後續升級規劃（非立即）

## 12) 後續升級規劃（非立即）

1. Publications 轉 BibTeX 格式（現已有 YAML 資料基礎）
2. 補 members / publications 搜尋與 filter
3. 新增 CSV/Excel 匯出腳本（Python）
4. 雙語化（中英文並陳）
