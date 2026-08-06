# Haifei's Home

This repository contains the Hugo source for
[haifei.pro](https://haifei.pro/). The site uses the LoveIt theme, is built
locally, and publishes generated files to the `gh-pages` branch. GitHub Pages
serves that branch without running a GitHub Actions workflow.

## Local development

Run the one-time setup:

```powershell
.\initialize.bat
```

Start a local preview:

```powershell
hugo server -D
```

### Private drafts

Keep unpublished post bundles under `private-content/` using the same layout as
the public `content/` directory. For example:

```text
private-content/
└── posts/
    └── post_YYYYMMDD_example/
        ├── index.zh-cn.md
        └── files/
```

The entire directory is ignored by Git. Preview public posts and private drafts
together with:

```powershell
.\preview-drafts.bat
```

On macOS or Linux, run `./preview-drafts.sh`. These commands enable Hugo drafts
and explicitly load `hugo.private.toml`; regular production builds continue to
read only `content/`. The test suite rejects `draft: true` files in `content/`
to prevent an unpublished source file from being committed by mistake.

When a draft is ready, move its complete page bundle from
`private-content/posts/` to `content/posts/`, set `draft: false`, review it, and
publish through the normal update workflow. Because ignored drafts are local
files, back them up separately or keep them in a private repository.

Create a production build:

```powershell
hugo --minify
```

### Local publication

GitHub Pages is configured to serve the root of the `gh-pages` branch. Run the
complete local validation, build, and deployment without changing source files:

```powershell
.\deploy-pages.bat
```

The deployment script builds with `https://haifei.pro/` as the production URL,
adds `CNAME` and `.nojekyll`, rejects source-like files in the generated output,
and pushes only the generated site to `gh-pages`. The temporary Git worktree is
isolated from this source checkout.

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

Imported posts always use `draft: false`, so a production build includes them.
Importing without `--publish` changes only the local worktree. Adding
`--publish` validates the site, commits and pushes the imported bundle, then
builds locally and pushes the generated website to `gh-pages`:

```powershell
.\updates.bat "https://zhuanlan.zhihu.com/p/ARTICLE_ID" --publish
```

The importer refuses to overwrite an existing bundle unless `--force` is
provided. Forced refreshes identify the existing bundle by its Zhihu article
or answer ID, so a later title edit does not create a duplicate directory.
They replace the Chinese source and localized images while preserving aliases,
taxonomy metadata, the existing English translation, and other local bundle
files. Publish mode also stops when the Git staging area already contains other
changes, preventing an unrelated staged change from entering the post commit.

Running the update wrapper without a Zhihu URL runs unit tests and the formula
audit, stages all current repository changes, creates a `daily updates` commit
when needed, pushes `master`, then builds locally and pushes the generated site
to `gh-pages`:

```powershell
.\updates.bat
```

The shell wrapper has the same two modes:

```bash
./updates.sh
./updates.sh "https://zhuanlan.zhihu.com/p/ARTICLE_ID" --publish
```

## Synchronizing the CV from Overleaf

The authoritative CV source is the private Overleaf project at
`https://git@git.overleaf.com/6a60bd158a3c2cea9ab34b7e`. Its local checkout
is stored in `.external/overleaf-cv`, which is ignored by this public
repository. The current website CV is generated from `resume.tex`.

Pull the newest Overleaf revision and regenerate the shared structured CV data.
The `/cv/` and `/en/cv/` pages keep their own language navigation and render
the same English CV body from `data/cv.json`:

```powershell
.\sync-cv.bat
```

To regenerate from the existing checkout while offline:

```powershell
.\sync-cv.bat --no-pull
```

To pull, regenerate, validate the whole Hugo site, commit all current website
changes, and push:

```powershell
.\sync-cv.bat --publish
```

Overleaf authentication is handled by Git Credential Manager; never put an
Overleaf token in this repository or in the clone URL. The public web CV omits
the phone numbers present in the TeX source. If `latexmk` and XeLaTeX are
available, the sync also compiles `resume.tex` and copies the PDF to
`static/cv/Haifei-Wang-CV.pdf`. Use `--require-pdf` when a missing or failed PDF
build should stop the sync.

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

To regenerate every English version sourced from a Zhihu column article while
leaving original blog posts and Zhihu answers untouched:

```powershell
.\.venv\Scripts\python.exe .\scripts\translate_posts.py batch submit `
  --scope zhihu-articles

# After the Batch completes:
.\.venv\Scripts\python.exe .\scripts\translate_posts.py batch apply --force
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

Verify existing translations without calling the API:

```powershell
.\.venv\Scripts\python.exe .\scripts\translate_posts.py verify `
  --scope zhihu-articles
```

The verifier compares source URLs, heading levels, local images, and the
presence of every protected formula, code block, link, and URL. Very long
articles are translated as cached, keyed paragraphs so the model retains enough
context for natural English. Protected objects use translation placeholders and
are restored by identity on the local machine, while Markdown heading, quote,
and list markers are restored from the source. Suspicious model control markers
or structurally invalid paragraphs are rejected and retried instead of being
written into the post.

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

KaTeX block environments must not be nested directly inside `\(...\)` or
`\[...\]`. The importer therefore rewrites `align`, `alignat`, and `equation`
to embeddable display forms such as `aligned`. The test suite also scans every
post for invalid legacy nesting before deployment.

LaTeX line breaks therefore remain `\\`. The legacy whole-file MathJax
replacement and undo scripts have been removed. Historical posts retain their
existing `$ ... $` syntax for backward compatibility.

Use `\lt` and `\gt` instead of literal `<` and `>` inside native passthrough
math. In particular, a literal `<` can be interpreted as the beginning of an
HTML tag before KaTeX receives the formula. The importer normalizes these
relations automatically.

The production math audit builds the site, extracts every formula from the
rendered HTML, and parses it with the same bundled KaTeX version used by the
theme:

```powershell
.\.venv\Scripts\python.exe scripts\audit_math.py
```

`updates.bat`, `updates.sh`, `deploy-pages.bat`, and `deploy-pages.sh` run this
audit before publication.

## Repository layout

- `content/`: posts, CV, publications, and other source content;
- `themes/LoveIt/`: the theme Git submodule;
- `zhihu-download/`: the third-party Zhihu downloader Git submodule;
- `scripts/import_zhihu.py`: import orchestration, math and image handling,
  validation, and optional publishing;
- `scripts/audit_math.py`: rendered-HTML delimiter and KaTeX validation for all
  website formulas;
- `scripts/translate_posts.py`: protected Markdown translation through the
  OpenAI Responses and Batch APIs;
- `scripts/migrate_post_names.py`: post bundle naming migration with old URL
  aliases;
- `scripts/sync_zhihu_dates.py`: apply reviewed Zhihu publication metadata to
  historical posts;
- `scripts/deploy_pages.py`: isolated local Hugo build and `gh-pages`
  publication;
- `deploy-pages.bat` and `deploy-pages.sh`: validate and publish without
  committing source changes.
