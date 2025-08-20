# Projekat kurs_dolara

## Primary goal of this project

Learn and setup python publish workflow on pypi


## Program features

Create python TUI application which will get current rate of USD from Centralna BiH.
Current rate is published on page https://cbbh.ba/CurrencyExchange/

I have checked reading that url with curl and have got this result:

```
curl -s https://cbbh.ba/CurrencyExchange/ | grep 840 -A2 -B2
                    </td>
                    <td class="tbl-smaller tbl-center">1</td>
                    <td class="tbl-smaller tbl-center">840</td>
                            <td class="tbl-smaller tbl-center buysell-column" style="display:none;">1.670039</td>
                            <td class="tbl-smaller tbl-highlight tbl-center middle-column">1.674225</td>
```


According to the result, todays USD course (code 840) is 1.670039 KM.

So the program should say:

Današnji kurs USD je 1.670039 KM.

## Tech stack

- Python
- UI: textual https://textual.textualize.io/


## Further instructions

### README.md

After any substantional change,  efore every commit, 

### Cover every feature with pytest

### Create github actions in project

- Test check
- After check passed, new version set, publish to pypi


## Tools and resources

- use gihtub `gh` tool for github operations
- project github repository: github.com/bringout/kurs_dolara
- pypi account: hernad
- rye for python project management

## Secrets

Use `pass` command for getting my secrets:
 
With `pass pypi/hernad@bring.out.ba/api_token_github` you get pypi api token.
That token is needed in github actions for publishing project. Setup github actions secret with this.

## General instructions

### .gitignore
- __pycache__
- .venv

### github README

- add pypi badge



