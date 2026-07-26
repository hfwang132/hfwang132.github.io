# Haifei's Home

This repository contains the Hugo source for
[hfwang132.github.io](https://hfwang132.github.io/). The site uses the LoveIt
theme and is built and deployed by GitHub Actions.

## Local development

Run the one-time setup:

```powershell
.\initialize.bat
```

Start a local preview:

```powershell
hugo server -D
```

Create a production build:

```powershell
hugo --minify
```

## Importing a post from Zhihu

The importer downloads one Zhihu article or answer, localizes its images,
preserves native LaTeX, creates a published Hugo page bundle, and validates the
full site:

```powershell
.\.venv\Scripts\python.exe .\scripts\import_zhihu.py `
  "https://zhuanlan.zhihu.com/p/ARTICLE_ID" `
  --tag "Quantum Optics" `
  --category "Quantum Information"
```

New bundle directories follow `Post_ZHIHU-PUBLICATION-DATE_ARTICLE-TITLE`.
Files inside the bundle keep Hugo's standard names such as `index.zh-cn.md` and
`index.en.md`. The importer reads Zhihu's `datePublished` metadata rather than
the edit date, and converts spaces and unsafe punctuation in the title to
hyphens:

```text
content/posts/Post_20251025_阻抗匹配-信号完整性速成-实验室版/
```

Use `--slug impedance-matching` to provide a shorter title component, producing
`Post_20251025_impedance-matching`. If a Zhihu page has no publication metadata,
the importer stops instead of guessing. After verifying the source date, use
`--published-date 2025-10-25` as an explicit fallback.

Imported posts always use `draft: false`, so a normal GitHub Pages deployment
includes them. Importing without `--publish` changes only the local worktree.
Adding `--publish` validates the site, commits only the imported bundle, and
pushes it:

```powershell
.\updates.bat "https://zhuanlan.zhihu.com/p/ARTICLE_ID" --publish
```

The importer refuses to overwrite an existing bundle unless `--force` is
provided. Publish mode also stops when the Git staging area already contains
other changes, preventing an unrelated staged change from entering the post
commit.

Running the update wrapper without a Zhihu URL validates the production site,
stages all current repository changes, creates a `daily updates` commit when
needed, and pushes the current branch:

```powershell
.\updates.bat
```

The shell wrapper has the same two modes:

```bash
./updates.sh
./updates.sh "https://zhuanlan.zhihu.com/p/ARTICLE_ID" --publish
```

## English translation with OpenAI

The translation pipeline uses the OpenAI Responses API for a newly imported
post and the Batch API for historical backfills. Before sending an article, it
replaces LaTeX, fenced and inline code, links, image paths, and Hugo shortcodes
with deterministic protected tokens. The result is rejected unless every token,
formula, code block, URL, image reference, and heading level passes validation.

The recommended local secret is `.secrets/openai-api-key.txt`. This entire
directory is ignored by Git. Configure it through the hidden terminal prompt;
the key is not displayed and is never passed as a command-line argument:

```powershell
.\.venv\Scripts\python.exe .\scripts\translate_posts.py key set
.\.venv\Scripts\python.exe .\scripts\translate_posts.py key status
```

Alternatively, create the file manually, paste only the API key (without quotes
or an `OPENAI_API_KEY=` prefix), and save it.

The loader first checks the `OPENAI_API_KEY` environment variable and then the
local secret file. To store the key in the current PowerShell process instead:

```powershell
$secureKey = Read-Host "OpenAI API Key" -AsSecureString
$env:OPENAI_API_KEY = [System.Net.NetworkCredential]::new("", $secureKey).Password
Remove-Variable secureKey
```

Do not put the key directly in a command-line argument, GitHub source file,
issue, commit, or screenshot. The default model is `gpt-5.6-terra`; override it
for one command with `--translation-model MODEL`, or for all commands with
`OPENAI_TRANSLATION_MODEL`.

Import, translate, validate, commit, and push one new post in a single command:

```powershell
.\updates.bat "https://zhuanlan.zhihu.com/p/ARTICLE_ID" `
  --translate en `
  --publish
```

Without `--publish`, both `index.zh-cn.md` and `index.en.md` remain as local
changes. If translation fails, the Chinese bundle is kept locally for diagnosis
but nothing is committed or pushed.

List or synchronously translate historical content:

```powershell
.\.venv\Scripts\python.exe .\scripts\translate_posts.py missing
.\.venv\Scripts\python.exe .\scripts\translate_posts.py translate `
  ".\content\posts\Post_YYYYMMDD_TITLE"
```

Submit all currently missing English articles as one Batch API job:

```powershell
.\.venv\Scripts\python.exe .\scripts\translate_posts.py batch submit
```

The command records the Batch ID under the ignored
`.secrets/openai-batches/` directory. Batch jobs can finish out of order and
may take up to 24 hours. Check and apply the latest recorded job with:

```powershell
.\.venv\Scripts\python.exe .\scripts\translate_posts.py batch status
.\.venv\Scripts\python.exe .\scripts\translate_posts.py batch apply
```

For an unattended local run, `batch run` submits, polls, validates, and writes
all translations. Applying a Batch refuses to use a result when the matching
Chinese source changed after submission.

```powershell
.\.venv\Scripts\python.exe .\scripts\translate_posts.py batch run
```

After reviewing historical translations, `.\updates.bat` validates the site,
commits the current changes, and pushes them to GitHub.

## Post folder naming

Existing post bundles use the same `Post_YYYYMMDD_TITLE` directory convention.
The Markdown filenames inside each bundle remain unchanged. Old routes are
stored as Hugo `aliases`, so links created before the migration continue to
work.

Preview or apply the naming migration with:

```powershell
.\.venv\Scripts\python.exe .\scripts\migrate_post_names.py
.\.venv\Scripts\python.exe .\scripts\migrate_post_names.py --apply
```

Verified historical Zhihu timestamps are stored in the reviewable
`data/zhihu-publication-dates.json` mapping. Article `datePublished` and answer
`dateCreated` metadata are normalized into the mapping's `datePublished`
field. After reviewing that file, preview or apply it with:

```powershell
.\.venv\Scripts\python.exe .\scripts\sync_zhihu_dates.py
.\.venv\Scripts\python.exe .\scripts\sync_zhihu_dates.py --apply
```

The sync updates `date` and `originalURL` in every language file, adjusts the
bundle's date prefix, and adds the previous canonical route to `aliases`.

## Images

The importer prefers Zhihu's high-resolution `data-original` image URL and
saves each image under the post bundle's `images/` directory. It rewrites each
standalone Markdown image as the site's `figure` shortcode:

```markdown
{{< figure src="images/FILENAME.png" >}}
```

The local shortcode displays figures at 80% of the article width on larger
screens and 100% on narrow mobile screens. An individual figure can override
the default with `width="65%"`. The importer also detects PNG/JPEG/GIF/WebP
from the file contents and corrects misleading extensions.

Before completing an import, it verifies that every local Markdown image
reference exists and that the number of references matches the number of saved
images. An incomplete image download fails the import instead of publishing a
partially broken post.

## Zhihu cookies

Cookie sources are checked in this order:

1. `--cookie` (not recommended because shell history records it);
2. the `ZHIHU_COOKIE` environment variable;
3. `--cookie-from-browser chrome|edge|firefox|auto`;
4. the file passed to `--cookie-file`;
5. `.secrets/zhihu-cookie.txt`;
6. a hidden terminal prompt.

The recommended fallback is `.secrets/zhihu-cookie.txt`. The `.secrets/`
directory is ignored by Git:

```powershell
New-Item -ItemType Directory -Force .secrets
notepad .secrets\zhihu-cookie.txt
```

Store only the raw HTTP `Cookie` header value in that file, for example
`name=value; another_name=another_value`. Do not include a `Cookie:` prefix.
After that, the default import command finds the file automatically:

```powershell
.\updates.bat "https://zhuanlan.zhihu.com/p/ARTICLE_ID" --publish
```

Alternatively, after signing in to Zhihu in a supported browser, explicitly
authorize local cookie extraction:

```powershell
.\updates.bat "https://zhuanlan.zhihu.com/p/ARTICLE_ID" `
  --cookie-from-browser edge `
  --publish
```

Browser cookie extraction requires explicit `--cookie-from-browser`
authorization and can still fail because of browser encryption or file locking.
Use the ignored cookie file or hidden prompt in that case. Treat a Zhihu cookie
as a login credential: never place it in an issue, commit, or terminal
screenshot.

## Native LaTeX

Hugo Goldmark's passthrough extension preserves math during Markdown parsing,
and the LoveIt theme renders it with KaTeX. New posts use standard delimiters:

```markdown
Inline math: \(E = mc^2\)

\[
\begin{aligned}
a &= b \\
c &= d
\end{aligned}
\]
```

LaTeX line breaks therefore remain `\\`. The legacy whole-file MathJax
replacement and undo scripts have been removed. Historical posts retain their
existing `$ ... $` syntax for backward compatibility.

## Repository layout

- `content/`: posts, CV, publications, and other source content;
- `themes/LoveIt/`: the theme Git submodule;
- `zhihu-download/`: the third-party Zhihu downloader Git submodule;
- `scripts/import_zhihu.py`: import orchestration, math and image handling,
  validation, and optional publishing;
- `scripts/translate_posts.py`: protected Markdown translation through the
  OpenAI Responses and Batch APIs;
- `scripts/migrate_post_names.py`: post bundle naming migration with old URL
  aliases;
- `scripts/sync_zhihu_dates.py`: apply reviewed Zhihu publication metadata to
  historical posts;
- `.github/workflows/hugo.yml`: GitHub Pages build and deployment.
