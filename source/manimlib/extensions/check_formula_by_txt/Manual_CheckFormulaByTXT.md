# Format:
Copy the code from [here](https://github.com/Elteoremadebeethoven/MyAnimations/blob/master/check_formula_by_txt/check_formula_by_txt.py) and paste it in your project, and create an scene like this:
```python3
class CheckFormula(CheckFormulaByTXT):
    CONFIG={
      "text":TexMobject("...") # or TextMobject
    }
```

You have to render it with `-ps`

## Example:
```python3
class CheckFormula(CheckFormulaByTXT):
    CONFIG={
    "text":TexMobject(
        "\\sqrt{",
        "\\left(",
        "x",
        "+",
        "{",
        "b",
        "\\over",
        "2",
        "a",
        "}",
        "\\right)",
        "^",
        "2",
        "}",
        "=",
        "\\pm",
        "\\sqrt{",
        "{",
        "b",
        "^",
        "2",
        "-",
        "4",
        "a",
        "c",
        "\\over",
        "4",
        "a",
        "^",
        "{.}",
        ")",
        )
    }
```
The result is:

<p align="center"><img src ="/check_formula_by_txt/images/im1.png" /></p>
## Remove elements:
If you want to remove some elements you can use:
```python3
class CheckFormulaRemove(CheckFormulaByTXT):
    CONFIG={
    "text":TexMobject(
        "\\sqrt{","\\left(","x","+","{","b","\\over","2","a","}",
        "\\right)","^","2","}","=","\\pm","\\sqrt{","{","b","^",
        "2","-","4","a","c","\\over","4","a","^","{.}",")",
        ), # <- Add a comma
    "remove":[4,13,9,11,17,19,28] # <- Add here the list
    }
```
Result:

<p align="center"><img src ="/check_formula_by_txt/images/im2.png" /></p>
If you remove a element that appears in the formula, then that element shows in red:
```python3
class CheckFormulaBadRemove(CheckFormulaByTXT):
    CONFIG={
    "text":TexMobject(
        "\\sqrt{","\\left(","x","+","{","b","\\over","2","a","}",
        "\\right)","^","2","}","=","\\pm","\\sqrt{","{","b","^",
        "2","-","4","a","c","\\over","4","a","^","{.}",")",
        ),
    "remove":[4,13,9,11,19,17,28,7] # <- The element 7 missing
    }
```
Result:

<p align="center"><img src ="/check_formula_by_txt/images/im3.png" /></p>
## Highlight elements:
```python3
class CheckFormulaHightlight(CheckFormulaByTXT):
    CONFIG={
    "text":TexMobject(
        "\\sqrt{","\\left(","x","+","{","b","\\over","2","a","}",
        "\\right)","^","2","}","=","\\pm","\\sqrt{","{","b","^",
        "2","-","4","a","c","\\over","4","a","^","{",")",
        ),
    "remove":[4,13,9,11,17,19,28,7], # Add a comma
    "show_elements":[7,10,18] # <- Add the list
    }
```
Result:

<p align="center"><img src ="/check_formula_by_txt/images/im4.png" /></p>
## Change the direction and size of the numbers:
```python3
class CheckFormulaDirectionNumber(CheckFormulaByTXT):
    CONFIG={
    "text":TexMobject(
        "\\sqrt{","\\left(","x","+","{","b","\\over","2","a","}",
        "\\right)","^","2","}","=","\\pm","\\sqrt{","{","b","^",
        "2","-","4","a","c","\\over","4","a","^","{.}",")",
        ),
    "remove":[4,13,9,11,17,19,28,7],
    "show_elements":[7,10,18],
    "direction_numbers":DOWN,       # <- Direction
    "numbers_scale":0.9,            # <- Scale of the numbers
    "space_between_numbers":0.2     # <- Buff
    }
```
Result:

<p align="center"><img src ="/check_formula_by_txt/images/im5.png" /></p>
# If you want to export the numbers as a list in a .csv file check [this](https://github.com/Elteoremadebeethoven/MyAnimations/blob/master/export_csv_file/export_csv_file.md)

