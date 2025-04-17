# TO DO

- [x] Download texts from new_journal
- [x] OCR on embedded text example
- [ ] Build reconstruction pipeline!
- [ ] OCR on non-embedded PDF (do we need?)
- [ ] Figure out how to chunk text properly -> research vector DB
- [ ] Implement chunking pipeline (WILL TAKE A WHILE)
- [ ] Chunks -> embeddings
- [ ] Build out vectorDB retrieval
- [ ] Find LLM / API to do generation and QA



# Notes on embedded text:
- In some articles, it may say 'continued on page x' at the end of a paragraph. To preserve context we would want to attach the two ends of the article. Where the article picks up, it will say 'continued from page y,' so that should be helpful.
- There seem to be problems on pages in some issues where, if there is an image in the middle of the page, the columns on either side get combined, and the embedded lines go all the way across the page, which is wrong.
- There are at least a few sideways-scanned pages with completely wrong embeddings.
- We have to ignore advertisements, whose text is usually also embedded
- The masthead, which lists staff and other descriptive information about the issue, is always in the first page or two

Main issues:
- ignoring ads
- parsing articles split across multiple pages
- a few select pages are screwed up by images or by bad scanning
- parsing the masthead is hard


# Heuristics for name extraction
- By, "-"
- **Author**
- Line breaks 



# Prompts
- Extract table of contents from 2nd/3rd page

# Old prompt
- 