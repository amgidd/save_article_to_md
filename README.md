# save_article_to_md
save_article_to_md is a python programm that saves article from internet to md file

input info:
- URL of the site
- tag name and class of the article

output:
- md file named as title(if found) or as 'title' if title of the article is not found. Md is saved in the working directory

**requirements:**
- bs4 python lib
- requests python lib
- markdownify python lib

**направления изменений**
- внести автоматическое определение тега статьи. Пока что тег статьи приходится искать вручную.
- связать с браузером, чтобы сохранять можно было одной кнопкой. Пока что приходится запускать скрипт отдельно, переключаться на другое окно.
- решить проблемы при конечном форматировании

**желаемый результат**
Удобно сохранять статьи с помощью кнопки закладки, но они не позволяют менять файл и сайт приходится снова загружать.

В идеале нужно средство для сохранения файла для последующей обработки информации или для хранения на компьютере, независимо от доступа к интернету или к оригиналу статьи. 

Формат md удобен тем, что текст однообразен, легко читаем, в отличие от стилей некоторых сайтов.
