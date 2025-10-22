# Basic Usage

## Initialize submodules

`initialize.bat`

## Add new posts

`hugo new content posts/your-post/index.en.md`

## Build draft

`hugo server -D` or `hugo serve`

## Build

`hugo`

## Update

`updates.bat`

# Hugo theme usage

## Add figure

```
{{< figure src="image/HBT_g2.png" title="Hanbury Brown and Twiss Experiment  " >}}
```

### Convert md to mathjax md

`python .\mathjax_md.py .\content\posts\some_post\index.zh-cn.md`

### Undone convert md to mathjax md

`python .\mathjax_md_undo.py .\content\posts\some_post\index.zh-cn.md -o C:\Users\hfwan\Downloads\undone.md --force`